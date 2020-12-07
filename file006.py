#class method 
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

# person_1 = Employee("Ali","Maleki",5000)
# person_2 = Employee("Jhon","Doe",6000)

emp_1_str = "Jhon-Doe-8000"
emp_2_str = "Jane-Doe-7000"
emp_3_str = "Steve-Smith-6500"

new_emp_1 = Employee.from_str(emp_1_str)
new_emp_2 = Employee.from_str(emp_2_str)
new_emp_3 = Employee.from_str(emp_3_str)

print(new_emp_1.first)
print(new_emp_2.__dict__)
print(new_emp_3.email)
