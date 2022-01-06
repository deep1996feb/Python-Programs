#Write a Custom Decorator?

'''Custom Decorator: Decorators in python are essentially function that add functionality to an existing 
function without changing the structure of the function itself.
'''

#For example

def deco1(func1):
    def create():
        print("Hello Python")
        func1()
        print("Programming")
    return create

#Add Decorator

@deco1
def language():
    print("Python is awesome.")

language()
