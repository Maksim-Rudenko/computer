# importing numpy package from
# python library
import numpy as np
 
# importing matplotlib.pyplot package from 
# python 
import matplotlib.pyplot as plt
 
# Creating an empty figure
# or plot 
fig = plt.figure()
 
# Defining the axes as a 
# 3D axes so that we can plot 3D 
# data into it.
ax, ax1 = plt.axes(projection="3d")

#ax1 = ax.twinx()

# creating a wide range of points x,y,z 
x = [0,1,2,3,4,5,6]
y = [0,1,4,9,16,25,36]
z = [0,1,4,9,16,25,36]

x1 = [0,3,4,7,8,9,10]
y1 = [0,2,3,5,14,20,30]
z1 = [0,2,3,5,14,20,30]
 
# plotting a 3D line graph with X-coordinate,
# Y-coordinate and Z-coordinate respectively
ax.plot3D(x, y, z, 'red')

ax1.plot3D(x1, y1, z1, 'green')

# plotting a scatter plot with X-coordinate,
# Y-coordinate and Z-coordinate respectively
# and defining the points color as cividis
# and defining c as z which basically is a 
# definition of 2D array in which rows are RGB
#or RGBA
#ax.scatter3D(x, y, z, c=z, cmap='cividis')

# Showing the above plot
plt.show()