import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/sample_data.csv")
data['date'] = pd.to_datetime(data['date'])

plt.plot(data['date'], data['footfall'])
plt.title("Temple Footfall Trend")
plt.show()
