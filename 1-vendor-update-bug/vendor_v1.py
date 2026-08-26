"""Approved vendor release 2.0.0.

The refund processor receives retry messages, so one order can appear more than once.
Only one refund may be sent for each order.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class RefundRequest:
    order_id: str
    amount_hkd: int


def build_refund_batch(requests: list[RefundRequest]) -> list[RefundRequest]:
    """Return at most one refund instruction for each order."""
    batch: list[RefundRequest] = []
    seen_order_ids: set[str] = set()

    for request in requests:
        if request.order_id in seen_order_ids:
            continue
        seen_order_ids.add(request.order_id)
        batch.append(request)

    return batch
