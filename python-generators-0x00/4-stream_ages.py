#!/usr/bin/env python3
import seed

def stream_user_ages():
    connection = seed.connect_to_prodev()
    cursor = connection.cursor()
    cursor.execute("SELECT age FROM user_data")  #  No AVG() used
    for row in cursor:
        yield row[0]  # Yield age one by one
    cursor.close()
    connection.close()

def calculate_average_age():
    total_age = 0
    count = 0

    for age in stream_user_ages():
        total_age += age
        count += 1

    average = total_age / count if count else 0
    print(f"Average age of users: {average:.2f}")

# Call the function
if __name__ == "__main__":
    calculate_average_age()
