import pandas as pd
from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]

# Define a bin of range (10-20, 20-30, 30-40, 40-50, 50-60)
bins = [10, 20, 30, 40, 50, 60]

# Define a bin of range (20-30, 30-40, 40-50, 50-60)
bins = [20, 30, 40, 50, 60]

plt.hist(ages, bins=bins, edgecolor='black')

plt.title('Ages of Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')
plt.tight_layout()


plt.show()
