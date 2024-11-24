import pandas as p
df = p.read_csv("transactions.csv")

g = df.sort_values(by='SUM', ascending=False).loc[df["STATUS"] == "OK",:]
g.loc[:,'Unnamed: 0']=[i for i in range(len(g.loc[:,'Unnamed: 0']))]
b=g[g['Unnamed: 0']==0]
c=g[g['Unnamed: 0']==1]
d=g[g['Unnamed: 0']==2]
print("3 самых крупных платежа из реально проведённых:\n"+str(b.iloc[0,3])+"\n"+str(c.iloc[0,3])+"\n"+str(d.iloc[0,3])+"\n")

a = df.loc[df["STATUS"] == "OK",:].groupby('CONTRACTOR').sum()
print("Полная сумма реально проведённых платежей в адрес Umbrella, Inc:"+"\n"+str(a.loc['Umbrella, Inc','SUM']))
