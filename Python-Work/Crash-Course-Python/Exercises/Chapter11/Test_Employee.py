import unittest
from Employee import EmployeeStaff

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.firstname = "Jack"
        self.lastname = "Sam"
        self.annualSalary = 22000
        self.e = EmployeeStaff(self.firstname,self.lastname,self.annualSalary)

    def test_default_raise(self):
        self.e.give_raise()
        self.assertEqual(self.e.annualSalary, 22000 + 5000)

    def test_give_custom_raise(self):
       self.e.give_raise(20)
       self.assertEqual(self.e.annualSalary, 22000 + 20)

unittest.main()
