r=float(input("Enter the radius: "))
def circle_circumference(r):
    return 2*3.14*r
print(circle_circumference(r))

def weather_condition():
    print("weather is warm in",spring)
    print("weather is cold in",autumn)
spring="summer"
autumn="winter"
weather_condition()

def add(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
#take input from the user
print("Please select the operation")
print("a. Addition")
print("b. Subtraction")
print("c. Multiplication")
print("d. Division")
choice=input("please enter the choice here(a/b/c/d)")
num1=int(input("please enter the first number: "))
num2=int(input("please enter the second number: "))

if choice=='a':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='b':
    print(num1,"-",num2,"=",subtraction(num1,num2))
elif choice=='c':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='d':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("This is an invalid input")