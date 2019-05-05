class EmployeeStaff():

    def __init__(self, firstname, lastname, annualSalary):
        self.firstname = firstname
        self.lastname = lastname
        self.annualSalary = annualSalary

    def give_raise(self,amountToAdd=0):
        if amountToAdd > 0:
            self.annualSalary += amountToAdd
        else:
            self.annualSalary += 5000
