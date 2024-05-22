#To estimate the No of paddling done and the number of brakes applied in a bicycle.Also estimate the old
#and new speed of bicycle when paddle or brake is applied.

class Cycle:
    #To estimate the colour and initial speed  of the bicycle.
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed 

    def getSpeed(self):
        return self.speed

    #To set the speed of the bicycle to be increased
    def setSpeed(self,deltaSpeed):
        self.speed = self.getSpeed() + deltaSpeed

    #To increase the speed of bicycle using a for loop   
    def applyPaddle(self,np):
        self.np= np             # number of times we paddle
        #speedIncreament = int(input("How much acceleration do you want to make?"))     #Increase speed by 2 unit
        for j in range(0,np):
            #To print the old speed of bicycle.
            print("Old Speed was  : " + str(myCycle.getSpeed()))
            #Function from line no 13.
            speedIncreament = int(input("How much acceleration do you want to make?"))
            self.setSpeed(speedIncreament)
            #To print the new speed of bicycle.
            print("New Speed is   : " + str(self.getSpeed()))
            #To print the number of paddling done
            print("Paddling done : " + str(j+1) + "times")
             
myCycle = Cycle ("Red", 0)  #initial speed is set to 0

np=int(input("Enter a number of paddles done: ")) #Taking input about the number of paddles done.

myCycle.applyPaddle(np) #This function is used for  aplying the paddle according to input from user.


class Brake:
    #To estimate the colour and current speed  of the bicycle.
    def __init__(self, colour, speedb):
        self.colour = colour
        self.speedb = speedb

    def getSpeed1(self):
        return self.speedb
    
    #To set the speed of the bicycle to be decreased   
    def setSpeed1(self, deltaSpeedb):
        self.speedb = self.getSpeed1() - deltaSpeedb 

     #Function to apply brakes
    def applyBrake(self, bnp):
        self.bnp= bnp 
        #speedDecrement = int(input("How much deceleration do you want to make?"))
        #Loop to decrease speed of the bicycle and determine the old speed and new speed.
        for z in range(0, bnp):
            #Printing the current speed of bicycle(from line 68 and line 43)
            if myBrake.getSpeed1()>0:
                print("Old Speed was  : " + str(myBrake.getSpeed1()))
            else:
                print("Old Speed is:",0)  
            speedDecrement = int(input("How much deceleration do you want to make?"))      
            self.setSpeed1(speedDecrement)
            #Printing the new speed of bicycle after applying brakes
            if self.getSpeed1() > 0:
                print("New speed is :" + str(self.getSpeed1()))
            else:
                print("New speed is :",0)
                break
            #Printing the number of brakes applied.
            print("Brake applied : " + str(z+1) + "times")
            
#Taking the colour and current speed of the bicycle            
myBrake = Brake("Blue", 8)

#Taking input the no of brakes to be applied
bnp=int(input("Enter no of brakes applied:"))

#Applying brakes
myBrake.applyBrake(bnp)