# Example 

# Define a class called "Person"
class Person:
    def _init_(self,name,age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name}.")

# Create an object of the person class
person = Person("John",25)

# Access the objects attributes
print(person.name) # Output: John
print(person.age) #Output: 25

# call the objects method
person.greet()
#Output: Hello, my name is John.

