"""Simple release gate demonstrating a secret-pattern check."""

from pathlib import Path
import re
import unittest


class SecretScanTest(unittest.TestCase):
    def test_source_contains_no_live_style_payment_key(self) -> None:
        source = Path("payment_gateway.py").read_text(encoding="utf-8")
        live_style_key = re.compile(r"sk_live_[A-Za-z0-9_]{16,}")

        self.assertIsNone(
            live_style_key.search(source),
            "live-style payment key must not be stored in source code",
        )


if __name__ == "__main__":
    unittest.main()
