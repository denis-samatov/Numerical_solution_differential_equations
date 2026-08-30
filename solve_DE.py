import numpy as np
import matplotlib.pyplot as plt
from math import *
import pandas as pd

def show_plot(t, ans_rightDecision, ans_numericalMethod, labels, name):
    """Displays a plot comparing the exact solution with a numerical method.

    Args:
        t (list): A list of time points.
        ans_rightDecision (list): A list of the exact solution values.
        ans_numericalMethod (list): A list of the numerical solution values.
        labels (list): A list of labels for the plot legends.
        name (str): The title of the plot.
    """
    plt.figure()
    plt.plot(t, ans_rightDecision, 'o-k', alpha = 0.7, label = labels[0], lw = 2, mec = 'k', mew = 3, ms = 3)
    plt.plot(t, ans_numericalMethod, 'h-m', alpha = 0.7, label = labels[1], lw = 2, mec = 'k', mew = 3, ms = 3)
    plt.xlabel('Value of t')
    plt.ylabel('Value of x')
    plt.title(name)
    plt.legend()
    plt.grid(True)
    plt.show()

def print_info(t, answer, name, z='nothing'):
    """Prints the coordinates and solution values.

    Args:
        t (list): A list of time points.
        answer (list): A list of the solution values.
        name (str): The name of the method.
        z (str, optional): Additional values to print. Defaults to 'nothing'.
    """
    print(f'\\n\\n---------- {name} ----------')
    print(f'Координаты t: {t}')
    # print(f"Значения y'(t): {z}")
    print(f'Значение x(t): {answer}')
    print('#'*60)

def calc_absolute_error(x, y, n):
    """Calculates the absolute error between two lists of values.

    Args:
        x (list): A list of the first set of values.
        y (list): A list of the second set of values.
        n (int): The number of points to compare.

    Returns:
        list: A list of the absolute errors.
    """
    result = [abs(x[i]-y[i]) for i in range(n+1)]
    return result

def create_only_plot_error(t, error, labels, name):
    """Displays a plot of the absolute error.

    Args:
        t (list): A list of time points.
        error (list): A list of the absolute error values.
        labels (str): The label for the plot legend.
        name (str): The title of the plot.
    """
    plt.figure()
    plt.plot(t, error, 'o-k', alpha = 0.7, label = labels, lw = 2, mec = 'k', mew = 3, ms = 3)
    plt.xlabel('Value of t')
    plt.ylabel('Error')
    plt.title(name)
    plt.legend()
    plt.grid(True)
    plt.show()
    print('\\n\\n')

def show_all_plots(t, ans_rightDecision, ans_numericalMethod, labels, name):
    """Displays a plot comparing the exact solution with multiple numerical methods.

    Args:
        t (list): A list of time points.
        ans_rightDecision (list): A list of the exact solution values.
        ans_numericalMethod (list): A list of lists of the numerical solution values.
        labels (list): A list of labels for the plot legends.
        name (str): The title of the plot.
    """
    plt.figure(figsize=(9,5))
    plt.plot(t, ans_rightDecision, 'o-k', alpha = 0.7, label = labels[0], lw = 2, mec = 'k', mew = 3, ms = 3)
    plt.plot(t, ans_numericalMethod[0], 'h-m', alpha = 0.7, label = labels[1], lw = 2, mec = 'k', mew = 3, ms = 3)
    plt.plot(t, ans_numericalMethod[1], 'x--b', alpha = 0.7, label = labels[2], lw = 2, mec = 'k', mew = 3, ms = 3)
    plt.plot(t, ans_numericalMethod[2], '+-.r', alpha = 0.7, label = labels[3], lw = 2, mec = 'k', mew = 3, ms = 3)
    plt.plot(t, ans_numericalMethod[3], 'd:g', alpha = 0.7, label = labels[4], lw = 2, mec = 'k', mew = 3, ms = 3)
    plt.xlabel('Value of t')
    plt.ylabel('Value of x')
    plt.title(name)
    plt.legend()
    plt.grid(True)
    plt.show()

t0 = 1
x0 = 1
z0 = -1
tn = 3
h = 0.2

n = int((tn - t0) / h)
t_list = np.arange(t0, tn + h, h)
z = np.zeros([n+1])
x = np.zeros([n+1])
t = np.zeros([n+1])
z[0] = z0
x[0] = x0
t[0] = t0

'''Точное решение ОДУ'''
ans_rightDecision = [round(1/12 * exp(-3 - t) * (15 * exp(4) + exp(4*t) - 4 * exp(3 + t)), 2) for t in t_list]

print_info(t_list, ans_rightDecision, name = "Точное решение ДУ")

def euler_method(t, x, z, h, n):
    """Solves the ODE using the Euler method.

    Args:
        t (np.ndarray): An array of time points.
        x (np.ndarray): An array to store the solution values.
        z (np.ndarray): An array to store the derivative values.
        h (float): The step size.
        n (int): The number of steps.

    Returns:
        np.ndarray: The solution values.
    """
    for i in range(n):
        t[i+1] = t[i] + h
        z[i+1] = z[i] + h * (2 * z[i]  + 3 * x[i] + 1)
        x[i+1] = x[i] + h * z[i]
    return x.copy()

ans_eulerMethod = euler_method(t.copy(), x.copy(), z.copy(), h, n)
print_info(t_list, ans_eulerMethod, name="Решение методом Эйлера")
show_plot(t_list, ans_rightDecision, ans_eulerMethod, labels=["Built-in method", "Euler method"], name="Решение методом Эйлера")

def modified_euler_method(t, x, z, h, n):
    """Solves the ODE using the Modified Euler method.

    Args:
        t (np.ndarray): An array of time points.
        x (np.ndarray): An array to store the solution values.
        z (np.ndarray): An array to store the derivative values.
        h (float): The step size.
        n (int): The number of steps.

    Returns:
        np.ndarray: The solution values.
    """
    for i in range(n):
        t[i+1] = t[i] + h
        z[i+1] = z[i] + h * (2 * (z[i] + h/2 * (2 * z[i] + 3 * x[i] + 1))  + 3 * (x[i] + h/2 * (2 * z[i]  + 3 * x[i] + 1)) + 1)
        x[i+1] = x[i] + h * (z[i] + h/2 * z[i])
    return x.copy()

ans_modifiedEulerMethod = modified_euler_method(t.copy(), x.copy(), z.copy(), h, n)
print_info(t_list, ans_modifiedEulerMethod, name="Решение модифицированным методом Эйлера")
show_plot(t_list, ans_rightDecision, ans_modifiedEulerMethod, labels=["Built-in method", "modified Euler method"], name="Модифицированный Эйлер")

def runge_kutta_method(t, x, z, h, n):
    """Solves the ODE using the Runge-Kutta method.

    Args:
        t (np.ndarray): An array of time points.
        x (np.ndarray): An array to store the solution values.
        z (np.ndarray): An array to store the derivative values.
        h (float): The step size.
        n (int): The number of steps.

    Returns:
        tuple: A tuple containing the solution values and the derivative values.
    """
    for i in range(n):
        h2 = h / 2
        t[i+1] = t[i] + h
        m1 = z[i]
        k1 = 2 * z[i]  + 3 * x[i] + 1
        m2 = z[i] + h2 * k1
        k2 = 2 * (z[i] + h2 * k1) + 3 * (x[i] + h2 * m1) + 1
        m3 = z[i] + h2 * k2
        k3 = 2 * (z[i] + h2 * k2)  + 3 * (x[i] + h2 * m2) + 1
        m4 = z[i] + h * k3
        k4 = 2 * (z[i] + h * k3)  + 3 * (x[i] + h * m3) + 1
        z[i+1] = z[i] + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x[i+1] = x[i] + (h / 6) * (m1 + 2 * m2 + 2 * m3 + m4)
    return x.copy(), z.copy()

ans_rungeKuttaMethod, z_rungeKuttaMethod = runge_kutta_method(t.copy(), x.copy(), z.copy(), h, n)
print_info(t_list, ans_rungeKuttaMethod, name="Решение методом Рунге-Кутта")
show_plot(t_list, ans_rightDecision, ans_rungeKuttaMethod, labels=["Built-in method", "Runge–Kutta method"], name="Решение методом Рунге-Кутта")

z = np.zeros([n+1])
z_p = np.zeros([n+1])
x = np.zeros([n+1])
x_p = np.zeros([n+1])
t = np.zeros([n+1])
z[:4] = z_rungeKuttaMethod[:4]
z_p[:4] = z_rungeKuttaMethod[:4]
x[:4] = ans_rightDecision[:4]
x_p[:4] = ans_rightDecision[:4]
t[:4] = t_list[:4]

def adams_moulton_method(t, x, z, h, n):
    """Solves the ODE using the Adams-Moulton method.

    Args:
        t (np.ndarray): An array of time points.
        x (np.ndarray): An array to store the solution values.
        z (np.ndarray): An array to store the derivative values.
        h (float): The step size.
        n (int): The number of steps.

    Returns:
        np.ndarray: The solution values.
    """
    x_p = x.copy()
    z_p = z.copy()
    for i in range(3, n):
        t[i+1] = t[i] + h
        z_p[i+1] = z[i] + h/24 * (55 * (2 * z[i]  + 3 * x[i] + 1) - 59 * (2 * z[i-1]  + 3 * x[i-1] + 1) + 37 * (2 * z[i-2]  + 3 * x[i-2] + 1) - 9 * (2 * z[i-3]  + 3 * x[i-3] + 1))
        x_p[i+1] = x[i] + h/24 * (55 * z[i] - 59 * z[i-1] + 37 * z[i-2] - 9 * z[i-3])
        z[i+1] = z[i] + h/24 * (9 * (2 * z_p[i+1] + 3 * x_p[i+1] + 1) + 19 * (2 * z[i] + 3 * x[i] + 1) - 5 * (2 * z[i-1] + 3 * x[i-1] + 1) + (2 * z[i-2] + 3 * x[i-2] + 1))
        x[i+1] = x[i] + h/24 * (9 * z_p[i+1] + 19 * z[i] - 5 * z[i-1] + z[i-2])
    return x.copy()

ans_adamsMoultonMethod = adams_moulton_method(t.copy(), x.copy(), z.copy(), h, n)
print_info(t_list, ans_adamsMoultonMethod, name="Решение методом Адамса-Мультона")
show_plot(t_list, ans_rightDecision, ans_adamsMoultonMethod, labels=["Built-in method", "Adams-Moulton method"], name="Решение методом Адамса-Мультона")

error_eulerMethod = calc_absolute_error(ans_rightDecision, ans_eulerMethod, n)
error_modifiedEulerMethod = calc_absolute_error(ans_rightDecision, ans_modifiedEulerMethod, n)
error_rungeKuttaMethod = calc_absolute_error(ans_rightDecision, ans_rungeKuttaMethod, n)
error_adamsMoultonMethod = calc_absolute_error(ans_rightDecision, ans_adamsMoultonMethod, n);

create_only_plot_error(t_list, error = error_eulerMethod, labels =  "Euler method", name = "Абсолютная погрешность метода Эйлера")
create_only_plot_error(t_list, error = error_modifiedEulerMethod, labels = "modified Euler method", name = "Абсолютная погрешность модифицированного методом Эйлер")
create_only_plot_error(t_list, error = error_rungeKuttaMethod, labels = "Runge–Kutta method", name = "Абсолютная погрешность метода Рунге-Кутта")
create_only_plot_error(t_list, error = error_adamsMoultonMethod, labels = "Adams-Moulton method", name = "Абсолютная погрешность метода Адамса-Мультона")

data = { 't': t_list,
        'Точное решение': ans_rightDecision,
        'Метод Эйлера': ans_eulerMethod,
        'Модифицированный метод Эйлера': ans_modifiedEulerMethod,
        'Метод Рунге-Кутта': ans_rungeKuttaMethod,
        'Метод Адамса-Мультона': ans_adamsMoultonMethod
        }
np.round(pd.DataFrame(data), 4)

data = { 't': t_list,
        'Δ метод Эйлера': error_eulerMethod,
        'Δ модифицированный метод Эйлера': error_modifiedEulerMethod,
        'Δ метод Рунге-Кутта': error_rungeKuttaMethod,
        'Δ метод Адамса-Мультона': error_adamsMoultonMethod
        }
np.round(pd.DataFrame(data), 4)

solutions = [ans_eulerMethod, ans_modifiedEulerMethod, ans_rungeKuttaMethod, ans_adamsMoultonMethod]
labels = ['Точное решение', 'Метод Эйлера', 'Модифицированный метод Эйлера', 'Метод Рунге-Кутта', 'Метод Адамса-Мултона']
show_all_plots(t_list, ans_rightDecision, solutions, labels, name='Сравнение решений')
