#Hardcoded Variables
import matplotlib.pyplot as plt
import numpy as np

a = 1
b = 3
c = -6

def weather_model(x):
    return a*x**2 + b*x + c

x = np.linspace(-10, 10, 400)
y = weather_model(x)

plt.plot(x, y)
plt.title('Weather Model')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.grid(True)
plt.show()