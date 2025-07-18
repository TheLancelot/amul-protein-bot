import os
from products import ID_TO_NAME, ID_TO_ALIAS
from dotenv import load_dotenv
load_dotenv(".env")
from notify import send_email  # import your send_email function

BASE_URL = "https://shop.amul.com/en/product"

def test_send_product_alert(product_ids: list[str], test_email: str):
    """
    Sends a test email to `test_email` listing the given product_ids
    with both plain-text and HTML (with hyperlinks).
    """
    # Map IDs to names and aliases
    matched_names = [ID_TO_NAME[_id] for _id in product_ids if _id in ID_TO_NAME]
    matched_aliases = [ID_TO_ALIAS[_id] for _id in product_ids if _id in ID_TO_ALIAS]

    # Build plain-text body
    lines = ["🚨 Test Alert! 🚨", "The following products are back in stock:\n"]
    for name in matched_names:
        lines.append(f"• {name}")
    body = "\n".join(lines)

    # Build HTML body with clickable links
    html_lines = "<br>".join([
        f'<strong>• <a href="{BASE_URL}/{alias}" target="_blank">{name}</a></strong>'
        for name, alias in zip(matched_names, matched_aliases)
    ])
    html_body = f"""
    <html>
      <body>
        <h2>🚨 Test Alert! 🚨</h2>
        <p>The following products are back in stock:</p>
        {html_lines}
      </body>
    </html>
    """

    # Send the test email
    send_email(
        smtp_user="theamulbot@gmail.com",
        app_password=os.environ["app_password"],
        subject="[TEST] Amul Stock Alert",
        body=body,
        recipients=[test_email],
        html=html_body
    )
    print(f"Test email sent to {test_email} for products: {matched_names}")

test_send_product_alert(product_ids=["13","12","17","15"],test_email="nkcubing1@gmail.com")