"""Candidate feature: build a list for a customer email campaign.

The approved business purpose is to contact customers who consented to email.
"""

import csv
from pathlib import Path
from typing import Any


def build_marketing_export(customers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Prepare the customer rows requested by the marketing feature."""
    return [
        {
            "full_name": customer["full_name"],
            "hkid": customer["hkid"],
            "date_of_birth": customer["date_of_birth"],
            "email": customer["email"],
            "mobile": customer["mobile"],
            "bank_account": customer["bank_account"],
        }
        for customer in customers
        if customer["email_consent"]
    ]


def save_marketing_export(rows: list[dict[str, Any]]) -> Path:
    """Save the export as a normal CSV file for transfer to marketing."""
    output_path = Path("marketing-customer-export.csv")
    with output_path.open("w", newline="", encoding="utf-8") as output_file:
        writer = csv.DictWriter(output_file, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return output_path
