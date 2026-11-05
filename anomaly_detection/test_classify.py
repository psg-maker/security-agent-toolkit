import unittest
from pathlib import Path

import pandas as pd

from classify import classify_event, count_types


class ClassifyTests(unittest.TestCase):
    def test_classifies_login_admin_other_failure_and_success(self):
        cases = [
            ("POST /login", "실패", "비정상 로그인"),
            ("GET /admin", "실패", "비인가 접근"),
            ("GET /admin/users", "실패", "비인가 접근"),
            ("GET /.env", "실패", "기타 실패"),
            ("POST /login", "성공", "정상"),
        ]
        for action, result, expected in cases:
            with self.subTest(action=action, result=result):
                self.assertEqual(classify_event(action, result), expected)

    def test_counts_sample_events(self):
        path = Path(__file__).with_name("normalized_events.json")
        events = pd.read_json(path)

        self.assertEqual(
            count_types(events),
            {"비정상 로그인": 5, "비인가 접근": 3, "기타 실패": 15, "정상": 34},
        )


if __name__ == "__main__":
    unittest.main()
