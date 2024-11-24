import pandas as p
import matplotlib.pyplot as plt
df = p.read_csv("flights.csv")

a = df.groupby('CARGO').sum()
b = df.groupby('CARGO').max()
a.loc[:,'Unnamed: 0']=b.loc[:,'Unnamed: 0']

ax = a.loc[:,'Unnamed: 0'].plot(kind='bar')
plt.title("Количество полётов")
plt.savefig("NF.png")
ax2 = a.loc[:,'PRICE'].plot(kind='bar')
plt.title("Сумарный доход")
plt.savefig("M.png")
ax3 = a.loc[:,'WEIGHT'].plot(kind='bar')
plt.title("Количество перевезённого груза")
plt.savefig("NW.png")
