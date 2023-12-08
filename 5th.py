import matplotlib.pyplot as plt
import numpy as np

# Hardcoded variables
a = 1
b = 3
c = -6

def weather_model(x, a, b, c):
    return a*x**2 + b*x + c

x = np.linspace(-10, 10, 400)
y = weather_model(x, a, b, c)

plt.plot(x, y, label=f'Hardcoded: a={a}, b={b}, c={c}')

# Variables input from keyboard
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

y = weather_model(x, a, b, c)

plt.plot(x, y, label=f'Input: a={a}, b={b}, c={c}')

plt.title('Weather Model')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.grid(True)
plt.legend()
plt.show()
