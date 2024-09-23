//Created on 22.9.24
//Creating a differential equation solver using C++

#include <iostream>
using namespace std;


class DYDX {
private:
    // Function representing the differential equation dy/dx = x+ y^2
    float func(float x, float y) {
        return (x +  y * y);
    }

public:
    // Solving the differential equation using eulers method
    void solverbyeuler(float x0, float y0, float h, float x) {
        float y = y0;  // Initial value of y

        // Iterating until the target x is reached
        while (x0 < x) {
            y = y + h * func(x0, y);  // Applying Euler's formula
            x0 = x0 + h;  // Increment x0 by step size h
        }

        // Output the approximation at x
        cout << "Approximate solution at x = " << x << " is " << y << endl;
    }
};

// Main function
int main() {
    
    float x0,x,y0,h;

        // Input values from the user
    cout << "Enter the value of x0: ";
    cin >> x0;

    cout << "Enter the value of x: ";
    cin >> x;

    cout << "Enter the value of y0: ";
    cin >> y0;

    cout << "Enter the value of h: ";
    cin >> h;

    // Create an object of the DYDX class
    DYDX solver;
    // Calling the solverbyeuler method via the solver object
    solver.solverbyeuler(x0, y0, h, x);

    return 0;
}





