class Person:
    # class attribute
        # name = "Skinny"
        # age = 75
        # nationality = "SA"

    # constructor concept
    def __init__(self, name, age, nationality, status="Single"):
        # print("This is constructor")
        self.name = name
        self.age = age
        self.nationality = nationality
        self.status = status

    # method
    def full_details(mypar):
        return f"Name: {mypar.name}  Age: {mypar.age} Nationality: {mypar.nationality}"
    
    def marital_status(self):
        return f"Status: {self.status}"
    


#print(Person.name)

person1 = Person("Skinny", 75, "SA") #obj1
person2 = Person("Mutemi", 85, "Kanyan", status="Talking stage") #obj2


# print(details.name)
# print(details.age)
# print(details.nationality)
print(person1.full_details())
print("Before deleting: ", person1.name) # Skinny
# del person1.name # deleting an attribute
# print("After deleting: ", person1.name) # Error


print(person1.marital_status())
del person2
print(person2.full_details())
print(person2.marital_status())
