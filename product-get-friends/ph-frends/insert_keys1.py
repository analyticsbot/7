from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:postgres@localhost:5432/twitter')
import pandas as pd
df = pd.read_csv('twitterkeys.csv')
df.to_sql('twitterkeys', engine, if_exists = 'append')
