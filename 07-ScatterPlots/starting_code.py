import pandas as pd
from matplotlib import pyplot as plt

#plt.style.use('seaborn')
plt.style.use('fivethirtyeight')

x =      [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y =      [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
colors = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
sizes = [209, 486, 381, 255, 191, 315, 185, 228, 174, 538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]

plt.scatter(x, y)                                #Basic scatter plot
plt.scatter(x, y, s=100)                         #Change the size of dots
plt.scatter(x, y, c='green')                     #Change the Color of dots
plt.scatter(x, y, marker='X')                    #Change the Marker to X from dot. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html
plt.scatter(x, y, edgecolor='black', alpha=0.75) #edgecolor is edges of circle marker, alpha make it softness
plt.scatter(x, y, linewidth=1)                   #line with of circle marker
plt.scatter(x, y, s=100, c='green', edgecolor='black', linewidth=1, alpha=0.75)

plt.scatter(x, y, s=sizes, c=colors, cmap='Greens', edgecolor='black',linewidth=1, alpha=0.75)

#cmap attributes
#https://matplotlib.org/3.1.0/tutorials/colors/colormaps.html
cbar = plt.colorbar()
cbar.set_label('Satisfaction')

plt.tight_layout()
plt.show()