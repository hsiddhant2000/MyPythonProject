#Creating a program to perform basic calculator functions.
#Created on 5.9.2023
#function for addition of two numbers
def add(a, b):
    return a + b
#function for substraction of two numbers    
def substract(a, b):
    return a - b
#function for multiplication of two numbers    
def multiply(a, b):
    return a * b
#function for division of two numbers    
def divide(a, b):
    return a / b
    
print("Select choice")
print("1.Add")
print("2.Substract")
print("3.Multiply")
print("4.Divide")  
#Asking preference from the user to perform various operations    
while True:
    choice = input("Enter choice(1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        try:
            num1=float(input("Enter first number:"))
            num2=float(input("Enter second number:"))
        except ValueError:
            print("Invalid input.Please enter a number.") 
            continue   
        #Performing addition operation
        if choice == '1':
            print(num1, "+", num2, "=", add(num1,num2))
        #Performing substraction operation
        elif choice =='2':        
            print(num1, "-", num2, "=", substract(num1,num2))
        #Performing multiplication operation
        elif choice =='3':
            print(num1, "*", num2, "=", multiply(num1,num2)) 
        #Performing division operation
        elif choice =='4':        
            print(num1, "/", num2, "=", divide(num1,num2))
        
        else:
            print("Invalid input")

