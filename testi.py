import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

R_earth = 2
R_mars = 3

# Create planets
earth, = ax.plot([], [], 'bo', markersize=5)
mars, = ax.plot([], [], 'ro', markersize=3)
sun, = ax.plot([0], [0], 'yo', markersize=10)

# Create line-of-sight
line_of_sight, = ax.plot([], [], color='yellow', alpha=0.5)

def animate(frame):
    earth_angle = frame * 0.0564
    mars_angle  = frame * 0.03

    earth_x = R_earth * np.cos(earth_angle)
    earth_y = R_earth * np.sin(earth_angle)

    mars_x = R_mars * np.cos(mars_angle)
    mars_y = R_mars * np.sin(mars_angle)

    # Update planets
    earth.set_data([earth_x], [earth_y])
    mars.set_data([mars_x], [mars_y])

    # Update line-of-sight
    line_of_sight.set_data([earth_x, mars_x], [earth_y, mars_y])

    return earth, mars, line_of_sight

anim = FuncAnimation(fig, animate, frames=360, interval=50, blit=True)
plt.show()