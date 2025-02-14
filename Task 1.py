

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('/content/API_SP.POP.TOTL_DS2_en_csv_v2_23.csv', skiprows=4)

plt.figure(figsize=(12, 8))
plt.bar(df['Country Name'], df['2020'])
plt.xlabel('Country Name')
plt.ylabel('Population in 2020')
plt.title('Population by Country in 2020')
plt.xticks(rotation=45)
plt.show()
