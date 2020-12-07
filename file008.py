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

class Developer (Employee):
    raise_amount = 1.08

    def __init__ (self, first, last , pay, prog_lang):
        super().__init__(first, last , pay)
        self.prog_lang = prog_lang



# print(help(Developer))


# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

dev_1 = Developer("Jhon","Doe",8000, "Python")
dev_2 = Developer("Jane","Doe",9000, "Java")
dev_3 = Developer("Steve","Smith",7000 ,"Go")

# print(dev_1.email)
# print(dev_1.prog_lang)

class Manager(Employee):
    
    raise_amount = 1.08

    def __init__ (self, first, last , pay, employees=None):
        super().__init__(first, last , pay)
        if employees == None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp (self, emp):
        if emp not in self.employees :
            self.employees.append(emp)
    
    def remove_emp (self, emp):
        if emp in self.employees :
            self.employees.remove(emp)

    def print_emps (self):
        for emp in self.employees:
            print("-->",emp.full_name())

manag_1 = Manager("Hana","Gomez",10000,[dev_1,dev_2])

# print(manag_1.email)

manag_1.add_emp(dev_3)

# manag_1.print_emps()

print(isinstance(manag_1,Manager))
print(isinstance(manag_1,Employee))
print(isinstance(manag_1,Developer))

print("#"*20)
print(issubclass(Developer,Employee))
print(issubclass(Manager,Employee))
print(issubclass(Developer,Manager))
