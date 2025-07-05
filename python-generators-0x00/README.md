# Python Generators - 0x00

This project demonstrates how to use Python to interact with an SQL database and stream rows using generators.

## 📁 Files

- `seed.py`: Contains functions to:
  - Connect to a SQLite database
  - Create the `user_data` table
  - Insert data from a CSV file (`user_data.csv`)
- `0-main.py`: Script to test the functions in `seed.py` and display sample data.
- `user_data.csv`: Sample CSV file with user information (name, email, age).

## 🧪 Features

- Creates a SQLite database `ALX_prodev.db`
- Ensures the table `user_data` is created if not existing
- Skips duplicate entries based on email
- Reads and inserts data from `user_data.csv`
- Prints 5 sample records from the database

## 🧵 Generator (Optional)

A generator function can be added to stream database rows one at a time:

```python
def stream_rows(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data;")
    for row in cursor:
        yield row
    cursor.close()
