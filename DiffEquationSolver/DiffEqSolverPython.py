# Created on 20.9.24
# Creating a differential equation solver using Python


class DYDX:

    #Constructor to initialize the variables like x0,x,y0,h
    def __init__(self, x0, x, y0, h):
        self.x0=x0
        self.x=x
        self.y0=y0
        self.h=h

    #Method equation which defines the equation.
    def equation(self):
        return self.x0 + self.y0**2
    
    #Method eulersolver which solves the differential equation.
    def eulersolver(self):
            
            while self.x0<self.x:
                self.y0=self.y0+self.h*self.equation()
                self.x0=self.x0+self.h
            print("The approximate solution at x at",x,"is", self.y0)  
            

#Taking input from the user the initial values of the variables
x0=float(input("Enter the value of x0: "))
x=float(input("Enter the value of x: "))
y0=float(input("Enter the value of y0: "))
h=float(input("Enter the value of h: "))

#Creating an object solver          
solver =DYDX(x0,x,y0,h)
#Calling the eulersolver method via the solver object
solver.eulersolver()
       
        

    

        
        

