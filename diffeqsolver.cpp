//Created on 18-9-2024

//This is a differential equation solver that take input the initial values of a differential equation 
//and finds the solution of a differential equation.

//Example:- 
//Differential equation is dy/dx=x-y
//Initial Value of x0 taken as  1
//Initial Value of y0 taken as  2
//The value of x for calculating the no of iterations is taken as 3
//The value of h used in runge-kutta method is taken as 0.5
//The final solution of the differential equation is 2.2553

#include <iostream>
using namespace std;

//Function which defines the differential equation
float dydx(float x0, float y0){
    return x0-y0;//This is the differential equation dy/dx=x-y
}

//This is the function for calculating the solution of the differential equation using 
//Runge-Kutta method
float diffeqsolve(float x0, float y0, float x, float h){
    int iteration=int((x-x0)/h);
    float k1, k2, k3, k4;
    float y=y0;
    for(int i=1; i<=iteration; i++){
        k1=h*dydx(x0, y);
        k2=h*dydx(x0+h/2, y+k1/2);
        k3=h*dydx(x0+h/2, y+k2/2);
        k4=h*dydx(x0+h, y+k3);
        y+=0.16*(k1+2*k2+2*k3+k4);
        x0+=h;
    }
    return y;    
}

//This is the driver code for taking input the different values from the user
int main()
{
    cout<<"Enter the initial value x0: "; 
    float x0;
    cin >> x0;
    cout<<"Enter the initial value y0: ";
    float y0;
    cin >> y0;
    cout<<"Enter the value of x: ";
    float x;
    cin>>x;
    cout<<"Enter the value of h: ";
    float h;
    cin>>h;
    cout<<"Answer to differential equation: "<< diffeqsolve(x0, y0, x, h);
    

}