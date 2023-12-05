import math

def add(a, b):
    return a + b
def substract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b
print("Select choice")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide") 
print("5.Logarithm") 
print("6.Sine")
print("7.cos")
print("8.Tan")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8): ")

    if choice in ('1', '2', '3', '4'):
        try:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
        except ValueError:
            print("Valid options are 1/2/3/4") 
            continue   

        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))
 
        elif choice =='2':        
            print(num1, "-", num2, "=", substract(num1,num2))

        elif choice =='3':
            print(num1, "*", num2, "=", multiply(num1,num2)) 

        elif choice =='4':        
            print(num1, "/", num2, "=", divide(num1,num2))
        
        else:
            print("Invalid input")
    elif choice in ('5'):
        try:
            num3=float(input("Enter a number"))
            print(math.log(num3))
        except ValueError:
            print("Invalid input.Valid one is 5") 
            continue   
    elif choice in ('6'):
        try:
            num4=float(input("Enter a number"))  
            print(math.sin(num4)) 
        except ValueError:
            print("Invalid input.Valid one is 6") 
            continue     
    elif choice in ('7'):
        try:
            num5=float(input("Enter a number"))  
            print(math.cos(num5)) 
        except ValueError:
            print("Invalid input.Valid one is 7") 
            continue
    elif choice in ('8'):
        try:
            num6=float(input("Enter a number"))  
            print(math.tan(num6)) 
        except ValueError:
            print("Invalid input.Valid one is 8") 
            continue         
    
                
     




