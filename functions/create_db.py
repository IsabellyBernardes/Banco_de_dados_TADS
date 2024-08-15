import sqlite3

def create_db(
    database_name:str
) -> sqlite3.Connection:
    """
    Creates a new SQLite database file with the specified 
    name and establishes a connection to it.

    Args:
        database_name (str): The name of the database file 
        to create (excluding the '.db' extension).

    Returns:
        sqlite3.Connection: A connection object to the newly 
        created SQLite database.

    Example:
        conn = create_db('my_database')
        # This creates a file named 'my_database.db' and 
        # returns a connection to it.
    """

    return sqlite3.connect(f'{database_name}.db')