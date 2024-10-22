import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates

#plt.style.use('seaborn')
plt.style.use('fivethirtyeight')

dates = [
    datetime(2019, 5, 24),
    datetime(2019, 5, 25),
    datetime(2019, 5, 26),
    datetime(2019, 5, 27),
    datetime(2019, 5, 28),
    datetime(2019, 5, 29),
    datetime(2019, 5, 30)
]

y = [0, 1, 3, 4, 6, 5, 7]

plt.plot(dates, y, linestyle='solid')
plt.gcf().autofmt_xdate()                          #Change X-axis value to slanting
date_format = mpl_dates.DateFormatter('%b, %d %Y') #Convert Date format from YYYY-MM-DD to Month, Day  year
plt.gca().xaxis.set_major_formatter(date_format)   #Apply formatter to X axis


plt.tight_layout()
plt.show()