from products import NAME_TO_ID
import os
def names_to_ids(names: list[str]) -> list[str]:
    """
    Given a list of full product names, return the corresponding IDs.
    Ignores any names not in the mapping.
    """
    return [NAME_TO_ID[name] for name in names if name in NAME_TO_ID]
from supabase import create_client

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(
    smtp_user: str,
    app_password: str,
    subject: str,
    body: str,
    recipients: list[str],
    html: str | None = None
):
    """
    Send an email via Gmail SMTP.

    :param smtp_user: Your Gmail address (e.g., you@gmail.com)
    :param app_password: 16‑char Gmail App Password
    :param subject: Email subject line
    :param body: Plain-text body
    :param recipients: List of recipient email addresses
    :param html: Optional HTML body (better for rich formatting)
    """
    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = smtp_user
    msg["To"] = ", ".join(recipients)

    # Attach plain-text body
    msg.attach(MIMEText(body, "plain"))
    # Attach HTML body if provided
    if html:
        msg.attach(MIMEText(html, "html"))

    # Secure SSL context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(smtp_user, app_password)
        server.sendmail(smtp_user, recipients, msg.as_string())
        print(f"✅ Email sent to {len(recipients)} recipient(s).")


# initialize once
SUPABASE_URL=os.environ["SUPABASE_URL"]
SUPABASE_KEY=os.environ["SUPABASE_KEY"]
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def fetch_subscribers_for(new_ids: list[str]) -> list[dict]:
    """
    Returns a list of rows { email, whatsapp_number, products } 
    for users whose `products` array overlaps new_ids.
    """
    if not new_ids:
        return []
    resp = (
        supabase
        .table("subscriptions")
        .select("email, whatsapp_number, products")
        .overlaps("products", new_ids)   # Postgres array overlap
        .execute()
    )
    return resp.data or []

from products import ID_TO_NAME, ID_TO_ALIAS
BASE_URL = "https://shop.amul.com/en/product"
def dispatch_notifications(new_ids: list[str]):
    subs = fetch_subscribers_for(new_ids)

    print(f"Sending {len(subs)} emails")
    for row in subs:
        matched_ids = set(row["products"]) & set(new_ids)
        # Map back to full names (or your short‐name mapping)
        matched_names = [ID_TO_NAME[_id] for _id in matched_ids]
        
        # Craft a simple email body
        lines = ["Good news! \nThe following products you subscribed to are back in stock: \n"]
        lines += [f"• {name}" for name in matched_names]
        body = "\n".join(lines)
        

        # html_lines = "<br>".join([f"<strong>• {name}</strong>" for name in matched_names])
        # html_body = f"""
        # <p>
        # Good news!<br>
        # The following products you subscribed to are back in stock:<br><br>
        # {html_lines}
        # </p>
        # """

        # HTML email with hyperlinks
        html_lines = "<br>".join([
            f'<strong>• <a href="{BASE_URL}/{ID_TO_ALIAS[_id]}" '
            f'target="_blank">{ID_TO_NAME[_id]}</a></strong>'
            for _id in matched_ids
        ])
        html_body = f"""
        <p>
          Good news!<br>
          The following products you subscribed to are back in stock:<br><br>
          {html_lines}

          Click on the products to get them ASAP!
        </p>
        """

        if row["email"]:
            # print(f"sending email to {row['email']}")
            # print(body)

            send_email(
            smtp_user="theamulbot@gmail.com",
            app_password=os.environ["app_password"],
            subject="Amul Stock Update 🎉",
            body=body,
            recipients=[row["email"]],
            html=html_body
            )
            
        if row["whatsapp_number"]:
            
            print(f"sending whatsapp to {row['whatsapp_number']}")
            # send_whatsapp(row["whatsapp_number"], body)
    
