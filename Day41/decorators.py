import time
# Python Decorator function
# A decorator function is just another function that wrapps another function and gives that function and aditional functionality

def delay_decorator(function):
    def wrapper_function():
        time.sleep(3)
        function()
        function()
    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")

@delay_decorator
def say_bye():
    print("Bye")

def say_greeting():
    print("How are you?")


say_hello()