import unittest

import pandas as pd

from login_detection import pick_alert_ips, pick_login_failures


class LoginDetectionTests(unittest.TestCase):
    def test_picks_only_failed_login_events(self):
        events = pd.DataFrame(
            [
                {"action": "POST /login", "result": "실패", "ip": "a"},
                {"action": "POST /login", "result": "성공", "ip": "b"},
                {"action": "GET /login", "result": "실패", "ip": "c"},
            ]
        )

        actual = pick_login_failures(events)

        self.assertEqual(actual.to_dict("records"), [events.iloc[0].to_dict()])

    def test_alerts_keep_counts_at_or_above_limit(self):
        counts = pd.Series([4, 5, 6], index=["a", "b", "c"])

        actual = pick_alert_ips(counts, 5)

        self.assertEqual(actual.to_dict(), {"b": 5, "c": 6})


if __name__ == "__main__":
    unittest.main()
