import sqlite3

def drop_table(database:str,table_name:str) -> None:
    
    """
    Drops a table from an SQLite database.

    Connects to the specified SQLite database and drops the table with the given name. 
    The database name should be provided without the '.db' extension, which will be appended automatically.

    Parameters:
    - database (str): The name of the database file without the '.db' extension. The file will be looked for with the '.db' extension.
    - table_name (str): The name of the table to be dropped. The table will be removed from the specified database.

    Returns:
    - None: This function does not return any value.
    """
    
    database= f'{database}.db'
    
    conn= sqlite3.connect(database)
    cursor = conn.cursor()
    
    cursor.execute(f"""
    DROP TABLE {table_name}
               """)
    
    conn.close()
    