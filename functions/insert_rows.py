import sqlite3

def insert_one_row(
    database_name:str,
    table_name:str,
    columns_name:str,
    values:str
) -> None:
    
    """
    Inserts a single row of data into a table in an SQLite database.

    This function connects to the specified SQLite database, constructs an SQL query
    to insert a row with the provided data into the specified table, executes the query,
    and commits the changes. The connection to the database is closed after the operation.

    Args:
        database_name (str): The name of the SQLite database file. The file extension '.db'
                             is automatically appended if not included.
        table_name (str): The name of the table into which the data will be inserted.
        columns_name (str): A string containing the column names in the table where the data
                            will be inserted, separated by commas.
        values (str): A string representing the values to be inserted, formatted as needed for
                      the SQL query. The values should be formatted as a comma-separated list
                      matching the order of the columns specified. For example, `"'value1', 123"`.

    Returns:
        None: This function does not return any value.

    Raises:
        sqlite3.Error: If an error occurs during the SQL query execution or while accessing
                       the database.

    Example:
        # Example usage of the function
        insert_one_row(
            database_name='mydatabase',
            table_name='produto',
            columns_name='nome, qtd',
            values="'nitendo switch', 90"
        )
        
        # This will insert a row into the 'produto' table with 'nome' set to 'nitendo switch'
        # and 'qtd' set to 90. The database file 'mydatabase.db' will be used.
    """
    
    database_name= f'{database_name.db}'
    conn= sqlite3.connect(database_name)
    cursor = conn.cursor()

    query = f"""
        INSERT INTO {table_name} ({columns_name})
        VALUES ({values})
    """
    
    cursor.execute(query)
    conn.commit() # Serve para subir para o banco de dados
    conn.close()
    
    return None