import pandas as pd

data = pd.read_csv("./E150.csv", sep=';', index_col="Local_Time")
data.index = pd.to_datetime(data.index)
data = data[data.id != 56076883]
data.InvervalValue = pd.to_numeric(data.InvervalValue)
filtered = data.InvervalValue.resample('1d').sum().ewm(alpha=0.4).mean().reset_index()
filtered = filtered[filtered.Local_Time > "2018-08-03"]
filtered.to_csv("./E150_daily.csv", sep=";", index=False)
