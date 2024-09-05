import sqlite3

def create_table(database:str,table_name:str, columns_desc:str) -> None:
    
    """
    Create a table in the specified SQLite database if it does not already exist.

    This function connects to the SQLite database with the given name, and creates a table with the
    specified name and column definitions. If the database file does not exist, it will be created.
    The table will only be created if it does not already exist.

    Args:
        database (str): The name of the SQLite database file (without the .db extension).
        table_name (str): The name of the table to be created.
        columns_desc (str): A string describing the columns and their data types for the table.
                            The format should follow SQL syntax for table creation.

    Returns:
        None: This function does not return any value.

    Example:
        create_table(
            database='mydatabase',
            table_name='cliente',
            columns_desc='id INTEGER PRIMARY KEY, name TEXT, email TEXT'
        )
    """
    
    database= f'{database}.db'
    
    conn= sqlite3.connect(database)
    cursor = conn.cursor()
    
    cursor.execute(f"""
        CREATE TABLE IF NOT EXISTS {table_name} ({columns_desc})
               """)
    
    conn.close()
    