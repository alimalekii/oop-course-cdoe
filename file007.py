#static method

class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__ (self, first, last , pay):
        self.first = first 
        self.last = last    
        self.email = first + "." + last + "@company.com"
        self.pay = pay
        Employee.num_of_emps += 1

    def full_name (self):
        return "{} {}".format(self.first , self.last)

    def apply_raise (self):
        self.pay = int(self.pay * self.raise_amount )

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount

    @classmethod
    def from_str(cls, emp_str):
        first, last , pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 6 or day.weekday() == 5:
            return False
        return True


import datetime

mydate = datetime.date(2020,2,3)

print(Employee.is_workday(mydate))