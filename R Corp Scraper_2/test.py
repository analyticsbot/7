import pandas as pd

df = pd.read_csv('ex.csv')
df.loc[4,'Symbol'] = 'assaadas'

df.to_csv('ex.csv', index=False)
