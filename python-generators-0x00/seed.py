#!/usr/bin/env python3
import sqlite3
import csv
import uuid
import os

def connect_db():
    return sqlite3.connect("ALX_prodev.db")

def create_table(connection):
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_data (
            user_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            age REAL NOT NULL
        );
    """)
    connection.commit()
    print("Table user_data created successfully")
    cursor.close()

def insert_data(connection, csv_file):
    cursor = connection.cursor()
    try:
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                name, email, age = row
                user_id = str(uuid.uuid4())
                cursor.execute("SELECT * FROM user_data WHERE email = ?", (email,))
                if cursor.fetchone():
                    continue
                cursor.execute("""
                    INSERT INTO user_data (user_id, name, email, age)
                    VALUES (?, ?, ?, ?)
                """, (user_id, name, email, float(age)))
        connection.commit()
    except FileNotFoundError:
        print("CSV file not found.")
    finally:
        cursor.close()
