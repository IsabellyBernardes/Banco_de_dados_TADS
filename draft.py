import pandas as pd
import sqlite3

#create a data example
data=pd.DataFrame({
    'ID': [1,2,3,4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

#create a connection
conn = sqlite3.connect('mydatabase.db')

#se the to_sql method to save the DataFrame
data.to_sql(
    'client', conn,
    if_exists='replace',
    index=False
)

#closing the connection
conn.close()

conn = sqlite3.connect('mydatabase.db')
#curso do the searches
cursor = conn.cursor()
#respeitar a sequencia das funcoes
query = """
    SELECT name 
    FROM client
    WHERE name IN ('Alice','David')
"""
pd.read_sql_query(query, conn)