"""Illustrative payment integration containing a deliberately fake credential.

DEMO ONLY: the value below is not a real key and cannot access any service.
"""

from urllib.request import Request


PAYMENT_API_URL = "https://payments.example.invalid/v1/charges"
PAYMENT_API_KEY = "sk_live_DEMO_ONLY_1234567890abcdef"


def build_charge_request(amount_hkd: int) -> Request:
    """Build a payment request; no network call is made in this demo."""
    return Request(
        PAYMENT_API_URL,
        data=f'{{"amount_hkd": {amount_hkd}}}'.encode(),
        headers={
            "Authorization": f"Bearer {PAYMENT_API_KEY}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
