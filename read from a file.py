import matplotlib.pyplot as plt
import numpy as np

with open('variables.txt', 'r') as file:
    a, b, c = map(float, file.readline().split())

def weather_model(x):
    return a*x**2 + b*x + c

x = np.linspace(-10, 10, 400)
y = weather_model(x)

plt.figure(figsize=(6, 4))
plt.plot(x, y, label=f'{a}x^2 + {b}x + {c}')
plt.title('Plot of the quadratic function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
    
