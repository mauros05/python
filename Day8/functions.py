def greet(name):
    print("Hello")
    print("My name is")
    print(name)


greet("Steve")

# Function with more parameters

def greet_with(name, location):
    print(f"Hello my name is {name}")
    print(f"I live in {location}")

greet_with(location = "Coatzacoalcos", name = "Mauricio")