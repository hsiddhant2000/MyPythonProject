//Created on 1-10-2024
//Modified 3-10-2024
//To creare a 1-D Wave equation solver

#include <iostream>
#include <vector>
#include <cmath>

// Function for initial conditions
double U_T1(double x) {
    // Define the initial displacement at time T1, U(T1, X)
    float pi=3.14;
    return sin(pi * x); // Example: sinusoidal initial condition
}

double UT_T1(double x) {
    // Define the initial velocity at time T1, Ut(T1, X)
    return 0.0; // Example: zero initial velocity
}

// Function for boundary conditions
double U_X1(double t) {
    return 0.0; // Boundary condition at X1
}

double U_X2(double t) {
    return 0.0; // Boundary condition at X2
}

int main() {
// Constants and parameters
    const double c = 1.0;    // Wave propagation speed
    const double dx = 0.01;  // Spatial step size
    const double dt = 0.005; // Time step size
    const int nx = 100;      // Number of spatial points
    const int nt = 200;      // Number of time steps

    //condition check for stability
    if (c * dt / dx > 1) {
        std::cerr << "Stability condition violated!" << std::endl;
        return -1;
    }
    

    // Initialize solution arrays
    std::vector<double> U_previous(nx, 0.0); // U at previous time step (T - dt)
    std::vector<double> U_current(nx, 0.0);  // U at current time step (T)
    std::vector<double> U_next(nx, 0.0);     // U at next time step (T + dt)

    // Set initial conditions
    for (int i = 0; i < nx; i++) {
        double x = i * dx;
        U_previous[i] = U_T1(x);  // U(T1, X)
        U_current[i] = U_previous[i] + dt * UT_T1(x); // Approximate using initial velocity Ut(T1, X)
    }

    // Time-stepping loop
    for (int t = 1; t <= nt; t++) {
        double currentTime = t * dt;

        // Apply boundary conditions
        U_next[0] = U_X1(currentTime);  // U(T, X1)
        U_next[nx - 1] = U_X2(currentTime);  // U(T, X2)

        // Update interior points using the finite difference method
        for (int i = 1; i < nx - 1; i++) {
            U_next[i] = 2 * (1 - pow(c * dt / dx, 2)) * U_current[i]
                        - U_previous[i]
                        + pow(c * dt / dx, 2) * (U_current[i + 1] + U_current[i - 1]);
        }

        // Update the solution for the next time step
        U_previous = U_current;
        U_current = U_next;
    }

    // Output the final solution (or you can save to a file)
    for (int i = 0; i < nx; i++) {
        double x = i * dx;
        std::cout << "U(" << x << ") = " << U_current[i] << std::endl;
    }

    return 0;
}















