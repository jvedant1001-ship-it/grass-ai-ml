import pandas as pd
import matplotlib.pyplot as plt
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-arya/main/temperature_data.json"
df = pd.read_json(url)
 
# drop row 3 -> day = wednesday
df.dropna(subset=["temperature_c"],inplace=True)
df
 
# fill average value -> humidity -> nan
df.fillna(df['humidity_pct'].mean(),inplace=True)
df
 
# new cols -> farenheit   | cell*1.8 -> + 32
df['temperature_f'] = (df['temperature_c'] * 1.8)+32
df
# subplots -> 1d -> line chart | pie chart
fig,aux = plt.subplots(1,2)
aux[0].plot(df["humidity_pct"],df["temperature_c"])
aux[0].set_xlabel("humidity")
aux[0].set_ylabel("temperature in celsius")
aux[0].set_title("humidity with celsius")
 
aux[1].pie(df["temperature_f"],labels=df["day"],autopct="%1.1f%%")
aux[1].set_title("humidity with farenheit")
 
# save image data
plt.show()

#make a project involving numpy matplotlib pandas