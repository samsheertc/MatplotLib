TS 3:30
Figure is the container holding our plots

Axis are the actual plots

A figure can have multiple plots

one figure + one plot  means one figure and one axis 

we can have more than 1 axis per figure

TS 5:00
plt.gcf() ->get current figure
plt.gca() ->get current axis

fig, ax = plt.subplots() #One Plot/axis and one figure

For the above eg:
axis(ax) or plot is only set to single axis at this moment or a single plot.

By default subplots creates a figure and then specify a certain number of rows and columns of axis

if we don't pass in out number of rows and columns then it just defaults to a one X one i.e.
one row and one column which is simply one axis

fig, ax = plt.subplots(nrows=2, ncols=1) #2 Plot/axis and one figure
fig, ax = plt.subplots(nrows=2, ncols=2) #4 Plot/axis and one figure
