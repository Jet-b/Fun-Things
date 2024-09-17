import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

x0 = 0.5

def calc(x, r):
    return r * x * (1 - x)

def generate_population_growth(r, n):
    x = [x0]
    for i in range(n):
        x.append(calc(x[i], r))
    return x

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n_generations = 100
r_values = np.linspace(0, 3.0, 50)  # More r values to get smooth separation

for r in r_values:
    population = generate_population_growth(r, n_generations)
    generations = np.arange(n_generations + 1)
    r_series = np.full_like(generations, r*100)
    
    # Plot with r on Y-axis, generations on X-axis, and population on Z-axis
    ax.plot(generations, r_series, population)


ax.set_title('Population Growth')
ax.set_xlabel('Generations')
ax.set_ylabel('r/100')
ax.set_zlabel('Population')

# Adjust the view angle for better visualization
ax.view_init(elev=30, azim=120)

plt.show()
