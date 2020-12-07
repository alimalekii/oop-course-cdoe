


class Employee():
    pass

person_1 = Employee()
person_2 = Employee()

person_1.first = "Ali"
person_1.last = "Maleki"
person_1.email = "Ali.Maleki@test.com"

person_2.first = "User"
person_2.last = "Test"
person_2.email = "User.Test@test.com"

print(person_1.email)
print(person_2.email)