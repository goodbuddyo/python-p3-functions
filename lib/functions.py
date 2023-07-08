#!/usr/bin/env python3

def greet_programmer():
    # pass
    return print("Hello, programmer!") 
greet_programmer()

def greet(name):
    # pass
    return print(f"Hello, {name}!")
greet("Naureen")

def greet_with_default(name="programmer"):
    return print(f"Hello, {name}!")
greet_with_default("Sunny")
    

def add(num1, num2):
    return num1 + num2
add(1, 2)

def halve(number):
    #if not isinstance(number, int) or not isinstance(number, float):
    #    pass
    #elif isinstance(number, int) or isinstance(number, float):
    #    print(number / 2)
    if type(number) is float or type(number) is int:
        return(number / 2)
    else:
        pass



