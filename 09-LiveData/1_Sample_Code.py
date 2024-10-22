import matplotlib.pyplot as plt

plt.style.use('fivethirtyeight')

x_vals = [0, 1, 2, 3, 4, 5]
y_vals = [0, 1, 3, 2, 3, 5]

plt.plot(x_vals, y_vals)

plt.tight_layout()
plt.show()
