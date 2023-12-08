import matplotlib.pyplot as plt
import numpy as np

# Multiple sets of inputs
sets = [(1, 3, -6), (2, -4, 5), (-1, 2, 1)]

def weather_model(x, a, b, c):
    return a*x**2 + b*x + c

x = np.linspace(-10, 10, 400)

for a, b, c in sets:
    y = weather_model(x, a, b, c)
    plt.plot(x, y, label=f'a={a}, b={b}, c={c}')

plt.title('Weather Model')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.grid(True)
plt.legend()
plt.show()