import pandas as pd
import sqlite3
from functions.create_db import create_db
from functions.drop_table import drop_table

drop_table(database= 'mydatabase',table_name='cliente')
create_db('mydatabase')


conn= sqlite3.connect('mydatabase.db')
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
        id_cliente INT ,
        nome TEXT
    )              
               """)

cursor.execute("""
    DROP TABLE cliente2
               """)


import pandas as pd
import sqlite3

# create a data example
data = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

# create a connection
conn = sqlite3.connect('mydatabase.db')

# Use the to_sql method to save the DataFrame to a table in the database
data.to_sql(
    'client', conn,
    if_exists='replace',
    index=False
)

# closing the connection
conn.close()


########## 
conn = sqlite3.connect('mydatabase.db')

query = """ 
    SELECT Name 
    FROM client
    WHERE name IN ('Alice', 'David')
"""


pd.read_sql_query(query, conn)