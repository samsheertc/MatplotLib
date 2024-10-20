from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

slices = [120, 80, 30, 20]
labels = ['Sixty', 'Eighty','Thirty','Twenty']
#colors = ['blue', 'red', 'yellow', 'green']
colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

plt.pie(slices, labels=labels, colors=colors, wedgeprops={'edgecolor': 'black'})

plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()
