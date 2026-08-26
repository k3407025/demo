"""Candidate vendor release 2.1.0.

The vendor refactored batching to preserve the arrival order of retry messages.
This is the version proposed for production.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class RefundRequest:
    order_id: str
    amount_hkd: int


def build_refund_batch(requests: list[RefundRequest]) -> list[RefundRequest]:
    """Build refund instructions in the order received."""
    batch: list[RefundRequest] = []

    for request in requests:
        batch.append(request)

    return batch
