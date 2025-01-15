import sqlite3
import threading

# Create and setup the databases for Users, Orders, and Products
def setup_databases():
    # Users Database
    conn_users = sqlite3.connect("users.db")
    with conn_users:
        conn_users.execute(
            "CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT UNIQUE)"
        )

    # Products Database
    conn_products = sqlite3.connect("products.db")
    with conn_products:
        conn_products.execute(
            "CREATE TABLE IF NOT EXISTS Products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL)"
        )

    # Orders Database
    conn_orders = sqlite3.connect("orders.db")
    with conn_orders:
        conn_orders.execute(
            "CREATE TABLE IF NOT EXISTS Orders (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, product_id INTEGER, quantity INTEGER, FOREIGN KEY(user_id) REFERENCES Users(id), FOREIGN KEY(product_id) REFERENCES Products(id))"
        )

# Insert data functions
def insert_user(name, email):
    conn = sqlite3.connect("users.db")
    try:
        with conn:
            conn.execute("INSERT INTO Users (name, email) VALUES (?, ?)", (name, email))
    except sqlite3.IntegrityError as e:
        print(f"Error inserting user ({name}, {email}): {e}")
    finally:
        conn.close()

def insert_product(name, price):
    conn = sqlite3.connect("products.db")
    try:
        with conn:
            conn.execute("INSERT INTO Products (name, price) VALUES (?, ?)", (name, price))
    except sqlite3.Error as e:
        print(f"Error inserting product ({name}, {price}): {e}")
    finally:
        conn.close()

def insert_order(user_id, product_id, quantity):
    conn = sqlite3.connect("orders.db")
    try:
        with conn:
            conn.execute("INSERT INTO Orders (user_id, product_id, quantity) VALUES (?, ?, ?)", (user_id, product_id, quantity))
    except sqlite3.Error as e:
        print(f"Error inserting order (User ID: {user_id}, Product ID: {product_id}, Quantity: {quantity}): {e}")
    finally:
        conn.close()

# Static data provided as per the instructions

# Users data
users_data = [
    (1, "Alice", "alice@example.com"),
    (2, "Bob", "bob@example.com"),
    (3, "Charlie", "charlie@example.com"),
    (4, "David", "david@example.com"),
    (5, "Eve", "eve@example.com"),
    (6, "Frank", "frank@example.com"),
    (7, "Grace", "grace@example.com"),
    (8, "Alice", "alice@example.com"),
    (9, "Henry", "henry@example.com"),
    (10, "Jane", "jane@example.com")
]

# Products data
products_data = [
    (1, "Laptop", 1000.00),
    (2, "Smartphone", 700.00),
    (3, "Headphones", 150.00),
    (4, "Monitor", 300.00),
    (5, "Keyboard", 50.00),
    (6, "Mouse", 30.00),
    (7, "Laptop", 1000.00),
    (8, "Smartwatch", 250.00),
    (9, "Gaming Chair", 500.00),
    (10, "Earbuds", -50.00)
]

# Orders data
orders_data = [
    (1, 1, 1, 2),
    (2, 2, 2, 1),
    (3, 3, 3, 5),
    (4, 4, 4, 1),
    (5, 5, 5, 3),
    (6, 6, 6, 4),
    (7, 7, 7, 2),
    (8, 8, 8, 0),
    (9, 9, 1, -1),
    (10, 10, 11, 2)
]

# Simulate insertions using threading
def simulate_insertions():
    threads = []

    # Insert users data
    for user in users_data:
        thread = threading.Thread(target=insert_user, args=(user[1], user[2]))
        threads.append(thread)

    # Insert products data
    for product in products_data:
        thread = threading.Thread(target=insert_product, args=(product[1], product[2]))
        threads.append(thread)

    # Insert orders data
    for order in orders_data:
        thread = threading.Thread(target=insert_order, args=(order[1], order[2], order[3]))
        threads.append(thread)

    # Start all threads
    for thread in threads:
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Fetch and print results from each database

    # Users data
    print("Users in users.db:")
    conn_users = sqlite3.connect("users.db")
    with conn_users:
        users_result = conn_users.execute("SELECT * FROM Users").fetchall()
        print(users_result)

    # Products data
    print("\nProducts in products.db:")
    conn_products = sqlite3.connect("products.db")
    with conn_products:
        products_result = conn_products.execute("SELECT * FROM Products").fetchall()
        print(products_result)

    # Orders data
    print("\nOrders in orders.db:")
    conn_orders = sqlite3.connect("orders.db")
    with conn_orders:
        orders_result = conn_orders.execute("SELECT * FROM Orders").fetchall()
        print(orders_result)

# Main function
if __name__ == "__main__":
    setup_databases()  # Set up the databases
    simulate_insertions()  # Run the simulation with multiple threads for insertions
