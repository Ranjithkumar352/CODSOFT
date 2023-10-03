#function for add
def add(x,y):
    return x+y
#function for sub 
def sub(x,y):
    return x-y
#function for multi
def multi(x,y):
    return x*y
#function for division
def divi(x,y):
    if y==0:
        return "cannot divide by zero"
    return x/y
a=int(input("enter a number:"))
b=int(input("enter a number:"))
choice=input("choose an operation(+,-,*,/):")
# by using conditional statements
if choice == '+':
        result = add(a,b)
        print("Result: ", result)
elif choice == '-':
        result = sub(a,b)
        print("Result: ", result)
elif choice == '*':
        result = multi(a,b)
        print("Result: ", result)
elif choice == '/':
        result = divi(a/b)
        print("Result: ", result)
