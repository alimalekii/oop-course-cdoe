

class Employee:
    
    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@test.com"
        self.pay = pay
        Employee.num_of_emps += 1


    def full_name (self):
        return "{} {}".format(self.first,self.last)


    def apply_raise(self):
        # self.pay = int(self.pay * Employee.raise_amount)
        self.pay = int(self.pay * self.raise_amount)


person_1 = Employee("Ali","Maleki",5000)
person_2 = Employee("Jhon","Doe",6000)



print(person_1.raise_amount)
print(person_2.raise_amount)
print(Employee.raise_amount)