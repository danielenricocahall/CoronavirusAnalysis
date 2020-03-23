import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import numpy as np


def func(x, a, b, c):
    return a * b**x + c

df = pd.read_csv('./time_series_2019-ncov-Confirmed.csv')
italian_data = df[df['Country/Region'] == 'Italy']
us_data = df[df['Country/Region'] == 'US']
nj_data = us_data[us_data['Province/State'] == 'New Jersey']
x = []
y = []

counter = 1
for column in nj_data.columns:
    if '/20' in column:
        x.append(counter)
        y.append(nj_data[column].iloc[0].item())
        counter += 1


popt, pcov = curve_fit(func, np.array(x), y)
plt.plot(x, y, label='true')
a, b, c = tuple(popt)
plt.plot(x, func(np.array(x), *popt), 'g--', label=f'{a} * ${b}^x$ + {c}')
plt.title("NJ Confirmed Cases")
plt.legend()
plt.show()
