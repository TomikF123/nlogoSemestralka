import pandas as pd
import matplotlib
from matplotlib import pyplot as plt

file = "/home/tomas/school/ai/semestralka/analysis/BB_3k.csv"

#Prislo mi to nejlepsi udelat na format "[run number]","[step]","initial-density","count patches with [pcolor = white]","count patches with [pcolor = red]"
# tzn jeden radek jedna hotova simulace o jednom n tickach ale hodnoty pouze z posledniho ticku.
# takze predmetem je zkoumat jak se to podle initial dens. prumerne chova v ntym ticku u 300k simulacich je graf smooth xd



df = pd.read_csv(file)
df.rename(columns={"count patches with [pcolor = white]":"n_alive","count patches with [pcolor = red]":"n_dying"},inplace=True)
print(df)
df = df[["initial-density", "n_alive", "n_dying"]]

df_mean = df.groupby(
    by="initial-density")[["n_alive", "n_dying"]].mean().reset_index()
print(df_mean)

# ration between 
ratio = []

for ix in df_mean.index:
    alive = df_mean.loc[ix,"n_alive"]
    dying = df_mean.loc[ix, "n_dying"]
    dead = 10005 - alive - dying
    ratio.append(round(alive/dying,ndigits=3))
df_mean["ratio"] = ratio

fig, ax = plt.subplots(2, 2)

X_ratio = df_mean.index
Y_ratio = df_mean["ratio"]
graph_ratio = ax[0][0].plot(X_ratio, Y_ratio)

X_mean_alive = df_mean.index
Y_mean_alive = df_mean["n_alive"]
graph_ratio = ax[0][1].plot(X_mean_alive, Y_mean_alive)
plt.show()
