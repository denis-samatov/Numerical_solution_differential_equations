# Ordinary Differential Equations (ODE) Solver

This Python script provides a comparative analysis of various numerical methods for solving ordinary differential equations (ODEs). The implemented methods include Euler method, Modified Euler method, Runge-Kutta method, and Adams-Multon method. The comparison is done against the exact solution of a sample ODE.

## Overview

1. **Numerical Methods Implemented:**
   - Euler Method
   - Modified Euler Method
   - Runge-Kutta Method
   - Adams-Multon Method

2. **Analytical Solution:**
   - The script defines the exact solution of the ODE to compare the numerical solutions.

3. **Visualization:**
   - The script utilizes the `matplotlib` library to create plots that compare the numerical solutions with the exact solution.
   - It also generates plots showcasing the absolute errors of each numerical method.

4. **Data Output:**
   - The script outputs the results in tabular format, providing a detailed view of the solutions and absolute errors at each step.

## How to Use

1. **Input Parameters:**
   - Set the initial conditions (`t0`, `x0`, `z0`) and the final time (`tn`) in the script.
   - Adjust the step size `h` based on the desired level of accuracy.

2. **Run the Script:**
   - Execute the script in a Python environment.

3. **Visualize Results:**
   - Observe the generated plots to compare the numerical solutions with the exact solution and analyze the absolute errors.

4. **Review Data Tables:**
   - The script outputs tabular data for a detailed examination of the solutions and absolute errors.

## Dependencies

Ensure you have the following Python libraries installed:

```bash
pip install numpy matplotlib pandas
```

## Notes on Numerical Methods

1. **Euler Method:**
   - Simple and straightforward, but may accumulate errors over time.

2. **Modified Euler Method:**
   - Improved version of the Euler method, providing better accuracy.

3. **Runge-Kutta Method:**
   - Fourth-order accurate method, generally more accurate than Euler and Modified Euler.

4. **Adams-Multon Method:**
   - Multistep method known for its accuracy and efficiency.

## Disclaimer

Results may vary based on the nature of the specific ODE and characteristics of the data. It is recommended to thoroughly review the generated plots and tables for a comprehensive understanding of the numerical solutions and errors.

---

Feel free to customize the script and explore the behavior of different numerical methods in solving ODEs. If you have any questions or encounter issues, please refer to the documentation of the used libraries or seek assistance from relevant forums.
