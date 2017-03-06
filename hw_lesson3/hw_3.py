import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
df = pd.read_csv('source.tsv', sep='\t',parse_dates=['date'])
df['date'] = pd.to_datetime(df.date,format='%d',unit='D')
#df.resample('MS', axis=1).mean()
#group = df.groupby(pd.TimeGrouper(freq='D'))
#group = group.agg({'name':'count'})
#df.index=pd.date_range(df.date.day(), periods= 459).tolist()
#df.plot()
#plt.show()

print df
