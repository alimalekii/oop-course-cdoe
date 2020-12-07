class Employee:

    raise_amount = 1.04

    def __init__ (self, first, last , pay):
        self.first = first 
        self.last = last    
        self.email = first + "." + last + "@company.com"
        self.pay = pay

    def full_name (self):
        return "{} {}".format(self.first , self.last)

    def apply_raise (self):
        self.pay = int(self.pay * self.raise_amount )

    def __repr__(self):
        return "Employee('{}','{}'.{})".format(self.first,self.last,self.pay)
    
    def __str__(self):
        return "{} - {}".format(self.full_name(),self.email)

    def __add__(self,other):
        if isinstance(other,Employee):
            return self.pay + other.pay
        else:
            return NotImplemented
    def __len__(self):
        return len(self.full_name())

emp_1 = Employee("Ali","Maleki",5000)
emp_2 = Employee("Jhon","Doe",6000)

print(repr(emp_1))
print(str(emp_1))
print(emp_1)

print(emp_1 + emp_2)
# print(emp_1 + 1322)
print(len(emp_1))
print(emp_1.__len__())