import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

file = "/home/tomas/school/ai/semestralka/analysis/BB_3k.csv"


df = pd.read_csv(file)
df.rename(columns={"count patches with [pcolor = white]":"n_alive","count patches with [pcolor = red]":"n_dying","[step]":"step"},inplace=True)
print(df)

# Selecting only the columns of interest
df = df[["initial-density", "n_alive", "n_dying","step"]]

df_mean = df.groupby(
    by="initial-density")[["n_alive", "n_dying","step"]].mean().reset_index()


# Calculating some ratios, may be included in the report 
ratio = []

for ix in df_mean.index:
    alive = df_mean.loc[ix,"n_alive"]
    dying = df_mean.loc[ix, "n_dying"]
    dead = 10005 - alive - dying
    ratio.append(round(alive/dying,ndigits=3))
df_mean["ratio"] = ratio

#Setting the Figure to i by j subplots, creating common values for X axis
fig, ax = plt.subplots(2, 2)
X = df_mean.index

# Plot 1 - avg Step until equlibrium ?
Y_step = df_mean["step"]
graph_step = ax[0][0].plot(X, Y_ratio)

#plot 2 ? 
""" X_mean_alive = df_mean.index
Y_mean_alive = df_mean["n_alive"]
graph_ratio = ax[0][1].plot(X_mean_alive, Y_mean_alive) """

plt.show()
