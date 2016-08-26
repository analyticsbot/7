import psycopg2
import os
import glob
import pandas as pd

df = pd.read_csv('twitterkeys.csv')

conn = psycopg2.connect('postgresql://postgres:postgres@localhost:5432/twitter')
cur = conn.cursor()

for i, row in df.iterrows():
    Username, Password, ConsumerKey, ConsumerSecret, AccessToken, \
              TokenSecret, id, inUse= row[0], row[1], row[2], row[3], row[4],\
              row[5], row[6], row[7]

    sql = "insert into twitterkeys values " + '(\'' + Username +"','"+ Password+"','"+ ConsumerKey+"','"+\
              ConsumerSecret+"','"+ AccessToken+"','"+ \
              TokenSecret+"',"+ str(id)+","+ str(inUse) + ')'
    print sql

    cur.execute(sql)




conn.commit()
cur.close()
