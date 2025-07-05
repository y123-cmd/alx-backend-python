#!/usr/bin/env python3
import sqlite3

def stream_users_in_batches(batch_size):
    connection = sqlite3.connect("ALX_prodev.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM user_data")

    while True:
        batch = cursor.fetchmany(batch_size)
        if not batch:
            break
        yield [dict(row) for row in batch]  # yield list of dicts

    cursor.close()
    connection.close()


def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):  # loop 1
        for user in batch:  # loop 2
            if user["age"] > 25:  # condition, not a loop
                print(user)
