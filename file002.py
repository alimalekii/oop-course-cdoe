

class Employee:
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@test.com"
        self.pay = pay

    def full_name (self):
        return "{} {}".format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * 1.04)



person_1 = Employee("Ali","Maleki",5000)
person_2 = Employee("Jhon","Doe",6000)

print(person_1.email)

print(person_1.full_name())
print(person_2.email)
print(person_2.full_name())