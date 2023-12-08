import matplotlib.pyplot as plt
import numpy as np

# Variables input from keyboard
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# Quadratic function
def weather_model(x):
    return a*x**2 + b*x + c

# Generate data
x = np.linspace(-10, 10, 400)
y = weather_model(x)

# Plot data
plt.plot(x, y)
plt.title('Weather Model')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.grid(True)
plt.show()
