# Simulating Concurrent Insertions in a Distributed Database System using SQLite and Threading

## Objective
The objective of this assignment is to create a program that simulates a distributed system where different types of data (Users, Orders, Products) are stored in separate SQLite databases. The program should insert at least 10 records for each model (Users, Orders, and Products) concurrently using threading to simulate simultaneous insertions.

## Requirements
1. **Models**:
   - **Users Table**: Contains three fields: `id`, `name`, `email`.
   - **Products Table**: Contains three fields: `id`, `name`, `price`.
   - **Orders Table**: Contains four fields: `id`, `user_id`, `product_id`, `quantity`.

2. **Databases**:
   - Each model is stored in a separate SQLite database:
     - `Users`: Stored in `users.db`
     - `Products`: Stored in `products.db`
     - `Orders`: Stored in `orders.db`

3. **Insertions**:
   - Users Table: Insert 10 records with predefined data.
   - Products Table: Insert 10 records with predefined data.
   - Orders Table: Insert 10 records with predefined data.

4. **Concurrency**:
   - The program should use Python's `threading` library to simulate simultaneous insertions into the respective databases.

5. **No Database-Level Validation**:
   - All validations and integrity checks should be handled in the application logic, not the database.

## Solution Overview
The solution involves the following steps:

1. **Database Setup**:
   - Create three separate SQLite databases for Users, Products, and Orders.
   - Create the respective tables in each database if they do not already exist.

2. **Insert Data Functions**:
   - Functions to insert records into each table: `insert_user`, `insert_product`, and `insert_order`.
   - Each insert operation connects to the respective database and inserts data.

3. **Concurrency with Threading**:
   - The insert operations for users, products, and orders are executed in parallel using Python threads.
   - Each thread performs an insertion for one record.

4. **Simulate Insertions**:
   - A function simulates concurrent insertions by launching threads for each data entry (10 users, 10 products, 10 orders).
   - After all threads finish, the results are fetched and printed from each database.
