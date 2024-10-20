import csv
import numpy as np
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv('data.csv')
ids = data['Responder_id']
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()

for response in lang_responses:
    language_counter.update(response.split(';'))

#Option-1
languages = []
popularity = []
for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

#Option-2
#languages, popularity = zip(*language_counter.most_common(15))
#languages, popularity =  list(languages), list(popularity)

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)
plt.title("Most Popular Languages")
# plt.ylabel("Programming Languages")
plt.xlabel("Number of people who use")

plt.tight_layout()
plt.show()
