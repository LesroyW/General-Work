import unittest
from hn_submissions import returnStatusCode, returnDictLen

class TestCaseA(unittest.TestCase):
    def test_Case_A(self):
        self.assertEqual(returnStatusCode(), 200)

    def test_Case_B(self):
        self.assertEqual(returnDictLen(),30)
unittest.main()