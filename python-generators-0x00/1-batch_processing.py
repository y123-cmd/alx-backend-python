# Assuming we have a function `fetch_all_users()` that retrieves all users from the database
def fetch_all_users():
    # This is a placeholder for the actual database fetching logic
    # In practice, this function should interact with your database to return user records
    query = "SELECT * FROM user_data"
    return [
        {'user_id': '00234e50-34eb-4ce2-94ec-26e3fa749796', 'name': 'Dan Altenwerth Jr.', 'email': 'Molly59@gmail.com', 'age': 67},
        {'user_id': '006bfede-724d-4cdd-a2a6-59700f40d0da', 'name': 'Glenda Wisozk', 'email': 'Miriam21@gmail.com', 'age': 119},
        {'user_id': '006e1f7f-90c2-45ad-8c1d-1275d594cc88', 'name': 'Daniel Fahey IV', 'email': 'Delia.Lesch11@hotmail.com', 'age': 49},
        {'user_id': '00cc08cc-62f4-4da1-b8e4-f5d9ef5dbbd4', 'name': 'Alma Bechtelar', 'email': 'Shelly_Balistreri22@hotmail.com', 'age': 102},
        {'user_id': '01187f09-72be-4924-8a2d-150645dcadad', 'name': 'Jonathon Jones', 'email': 'Jody.Quigley-Ziemann33@yahoo.com', 'age': 116},
        # More user records...
    ]

def stream_users_in_batches(batch_size):
    all_users = fetch_all_users()
    for i in range(0, len(all_users), batch_size):
        yield all_users[i:i + batch_size]

def batch_processing(batch_size):
    for batch in stream_users_in_batches(batch_size):
        filtered_users = [user for user in batch if user['age'] > 25]
        for user in filtered_users:
            print(user)

# Example usage
if __name__ == "__main__":
    batch_processing(50)

