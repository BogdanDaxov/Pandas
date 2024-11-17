import pandas as p
df = p.read_csv("transactions.csv")

g = df.sort_values(by='SUM', ascending=False).loc[df["STATUS"] == "OK",:]
print("3 самых крупных платежа из реально проведённых:\n"+str(g.loc[5085,'SUM'])+"\n"+str(g.loc[4451,'SUM'])+"\n"+str(g.loc[1348,'SUM'])+"\n")

a = df.groupby('CONTRACTOR').sum()
print("Полная сумма реально проведённых платежей в адрес Umbrella, Inc:"+"\n"+str(a.loc['Umbrella, Inc','SUM']))
