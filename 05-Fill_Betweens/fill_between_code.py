import pandas as pd
from matplotlib import pyplot as plt

data = pd.read_csv('data.csv')
ages = data['Age']
dev_salaries = data['All_Devs']
py_salaries = data['Python']
js_salaries = data['JavaScript']

plt.plot(ages, dev_salaries, color='#444444',linestyle='--', label='All Devs')
plt.plot(ages, py_salaries, label='Python')

overall_median = 57287

#Fill  color from python values to y2=0
plt.fill_between(ages, py_salaries, alpha=0.25)

#Fill  color from py_salaries values to y=0
plt.fill_between(ages, py_salaries, overall_median, alpha=0.25)

#Fill Green color when py_salaries > overall_median
plt.fill_between(ages, py_salaries, overall_median, where=(py_salaries > overall_median) , interpolate=True, color='green', alpha=0.25)

#Fill Red color when py_salaries < overall_median
plt.fill_between(ages, py_salaries, overall_median, where=(py_salaries < overall_median) , interpolate=True, color='red', alpha=0.25)

#Fill color between dev_salaries and py_salaries
plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries > dev_salaries) , interpolate=True, color='green', alpha=0.25, label='Above Avg')
plt.fill_between(ages, py_salaries, dev_salaries, where=(py_salaries <= dev_salaries), interpolate=True, color='red'  , alpha=0.25, label='Below Avg')

plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD)')

plt.tight_layout()
plt.show()