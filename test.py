import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
#background
fig.patch.set_facecolor('black')
ax.patch.set_facecolor('black')
#max points and 1:1 ratio
ax.set_aspect('equal') 
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

#Planets and the Sun 
sun, = ax.plot(0,0, 'yo', markersize=20)  # 'yo' = yellow circle, markersize = size
earth, = ax.plot(2,0, 'bo', markersize=5)
mars, = ax.plot(3,0, 'ro', markersize=2.5)

#Orbit points
theta = np.linspace(0, 2*np.pi, 365)
ax.plot(2 * np.cos(theta), 2 * np.sin(theta), color='white', linestyle='--', alpha=0.3)
ax.plot(3 * np.cos(theta), 3 * np.sin(theta), color='white', linestyle='--', alpha=0.3)


#Line of sight
line_sight = ax.plot([], [], color='white', alpha=0.3)


#Earth animation
def move_planets(frame):
    earth_x_angle = frame * 0.0564 #these 2 numbers need to exactly 1.88x faster than mars
    earth_y_angle = frame * 0.0564

    mars_x_angle = frame * 0.03
    mars_y_angle = frame * 0.03

    earth_x_frame = 2 * np.cos(earth_x_angle)
    earth_y_frame = 2 * np.sin(earth_y_angle)

    mars_x_frame = 3 * np.cos(mars_x_angle) 
    mars_y_frame = 3 * np.sin(mars_y_angle)

    mars.set_data([mars_x_frame], [mars_y_frame])
    earth.set_data([earth_x_frame], [earth_y_frame])


    #line of sight anim


    return earth, mars
anim = FuncAnimation(fig, move_planets, frames=360, interval=50)



plt.show()