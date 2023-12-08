#Defining the function
def func(x):
    return 1+x**2
#performing two operations using the above function
print("select choice:")
print("1.Simpsons38")
print("2.Simpsons13")

while True:
    choice = input("Enter choice 1/2:")
    #performing integration using simpsons3/8 rule using above function
    if choice == '1':
        #Defining function for simpsons3/8 rule
        def simpsons38(x0,xn,n):
            #performing operation
            h = (xn - x0) / n
            integration = func(x0) + func(xn)
           
            for i in range(1,n):
                k = x0 + i*h

                if i%3 == 0:
                    integration = integration + 2 * func(k)
                else:
                    integration = integration + 3 * func(k)  

            integration = integration * 3 * h / 8   

            return integration   

        lower_limit = float(input("Enter lower limit of integration: "))
        upper_limit = float(input("Enter upper limit of integration: "))
        sub_interval = int(input("Enter number of sub intervals: "))

        result = simpsons38(lower_limit, upper_limit, sub_interval)
        #finally getting the result
        print("Integration result by Simpson's 3/8 method is:",result) 
    #performing integration using simpsons1/3 rule using above function
    elif choice == '2':
        #Defining function for simpsons1/3 rule
        def simpsons13(x1,xm,m):
            #performing operation
            l = (xm - x1) / m
            integration1 = func(x1) + func(xm)

            for j in range(1,m):
                q = x1 + j*l

                if j%2 == 0:
                    integration1 = integration1 + 2 * func(q)
                else:
                    integration1 = integration1 + 4 * func(q)  

            integration1 = integration1 *  l / 3   

            return integration1  

        lower_limit1 = float(input("Enter lower limit of integration: "))
        upper_limit1 = float(input("Enter upper limit of integration: "))
        sub_interval1 = int(input("Enter number of sub intervals: "))

        result1 = simpsons13(lower_limit1, upper_limit1, sub_interval1)
        #finally getting the result
        print("Integration result by Simpson's 1/3 method is:",result1) 

    else:
        print("Invalid input")    
