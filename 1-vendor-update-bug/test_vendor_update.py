"""Acceptance test for the candidate vendor release."""

import unittest

from vendor_v2 import RefundRequest, build_refund_batch


class VendorUpdateAcceptanceTest(unittest.TestCase):
    def test_retry_message_does_not_create_a_second_refund(self) -> None:
        retry_messages = [
            RefundRequest(order_id="ORDER-1001", amount_hkd=8_000),
            RefundRequest(order_id="ORDER-1001", amount_hkd=8_000),
        ]

        refund_batch = build_refund_batch(retry_messages)

        self.assertEqual(1, len(refund_batch), "one order must be refunded once")


if __name__ == "__main__":
    unittest.main()
