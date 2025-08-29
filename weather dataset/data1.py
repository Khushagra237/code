import pandas as pd
import seaborn as sns
sns.set_theme(color_codes=True)
weather = pd.read_csv('weather.csv')
weather.head()
weather.info()
sns.barplot('humidity', 'temperature', data=weather)
sns.displot(weather['humidity'])
sns.histplot(weather['humidity'], kde = False, rug = True)