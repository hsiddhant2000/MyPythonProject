//Created on 25.5.2024
//Modified

//#include  is a preprocessor directive that tells the compiler to include the contents of the C++ library
//iostream which provides input output functionality
// String library allows you to use the string class
#include <iostream>
#include <string>

//This line allows usage of every functionality of std(standard) namespace instead of prefixing std:: before them 
using namespace std;
//Defining a class
//string is a datatype from <string> library
class Cycle {
    string color;
    int speed;

//If the member is declared public it can be accessed from within as well as outside the class.
public:
    Cycle(string c, int s) : color(c), speed(s) {}
    //Cycle(string c, int s) is a constructor that gets called when an object Cycle myCycle("Red", 0) of the class is created
    //These are the initializer that initializes the color and speed attributes with values c and s

    //int function returns an int value
    int getSpeed() {
        return speed;
    }

    //void function dont return any value
    void setSpeed(int deltaSpeed) {
        speed += deltaSpeed;
    }

    //void function dont return any value
    void applyPaddle(int np) {
        for (int j = 0; j < np; j++) {
            cout << "Old Speed was: " << getSpeed() << endl;


            int speedIncrement;
            cout << "How much acceleration do you want to make? ";
            cin >> speedIncrement;

            setSpeed(speedIncrement);

            cout << "New Speed is: " << getSpeed() << endl;
            cout << "Paddling done: " << (j + 1) << " times" << endl;
        }
    }
};

//Creating a seperate class for applying brakes
class Brake {
    string colour;
    int speedb;
 
public:
    //Creating a constructor Brake(string co, int sb )
    Brake(string co, int sb ): colour(co), speedb(sb) {}

    //int function returns an int value
    int getspeed1(){
        return speedb;
    }
    //void function dont return any value
    void setspeed1(int deltaspeedb){
        speedb -= deltaspeedb;
    }

    void applyBrake(int bnp){
        for (int z=0; z < bnp; z++) {
            cout << "Old speed was: "<< getspeed1() << endl;

            int speedDecrement;
            cout << "How much deceleration you want to make?";
            cin >> speedDecrement;
            setspeed1(speedDecrement);

            cout << "New speed is: "<< getspeed1() << endl;
            cout << "Paddling done: "<< (z+1) << "times" << endl;
        }

    }
};    



int main() {
    //An object myCycle is created here.
    Cycle myCycle("Red", 0);

    int np;
    cout << "Enter the number of paddles done: ";
    cin >> np;

    myCycle.applyPaddle(np);

    Brake myBrake("Red", 8);

    int bnp;
    cout << "Enter the no of brakes applied: ";
    cin >> bnp;

    myBrake.applyBrake(bnp);

    return 0;
}



































































































































































