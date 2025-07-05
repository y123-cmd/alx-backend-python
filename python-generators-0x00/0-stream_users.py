def stream_users():
    # Connect to the database
    import sqlite3

    connection = sqlite3.connect("ALX_prodev.db")
    connection.row_factory = sqlite3.Row  # makes each row a dictionary-like object
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM user_data")

    for row in cursor:
        yield dict(row)  # Convert row object to dictionary

    cursor.close()
    connection.close()
