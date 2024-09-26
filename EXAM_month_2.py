import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS categories (
    code TEXT PRIMARY KEY,
    title TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS store (
    store_id INTEGER PRIMARY KEY,
    title TEXT NOT NULL
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    category_code TEXT,
    unit_price REAL NOT NULL,
    stock_quantity INTEGER NOT NULL,
    store_id INTEGER,
    FOREIGN KEY (category_code) REFERENCES categories(code),
    FOREIGN KEY (store_id) REFERENCES store(store_id)
)
''')

# Insert categories, ensuring no duplicates
categories_to_insert = [
    ('FD', 'Food products'),
    ('EL', 'Electronics'),
    ('CL', 'Clothing')
]

for code, title in categories_to_insert:
    try:
        cursor.execute("INSERT INTO categories (code, title) VALUES (?, ?)", (code, title))
    except sqlite3.IntegrityError:
        print(f"Category with code '{code}' already exists. Skipping insert.")

# Insert stores
stores_to_insert = [
    (1, 'Grocery Store'),
    (2, 'Electronics Hub'),
    (3, 'Fashion Outlet')
]

for store_id, title in stores_to_insert:
    try:
        cursor.execute("INSERT INTO store (store_id, title) VALUES (?, ?)", (store_id, title))
    except sqlite3.IntegrityError:
        print(f"Store with ID '{store_id}' already exists. Skipping insert.")

# Insert products
products_to_insert = [
    (1, 'Bread', 'FD', 1.5, 50, 1),
    (2, 'Smartphone', 'EL', 700.0, 15, 2),
    (3, 'T-Shirt', 'CL', 20.0, 100, 3)
]

for product in products_to_insert:
    try:
        cursor.execute("INSERT INTO products (id, title, category_code, unit_price, stock_quantity, store_id) VALUES (?, ?, ?, ?, ?, ?)", product)
    except sqlite3.IntegrityError:
        print(f"Product with ID '{product[0]}' already exists. Skipping insert.")

conn.commit()

def stores():
    cursor.execute("SELECT store_id, title FROM store")
    stores = cursor.fetchall()
    print("Список магазинов:")
    for store in stores:
        print(f"{store[0]}. {store[1]}")

def products(store_id):
    cursor.execute('''
        SELECT p.title, c.title, p.unit_price, p.stock_quantity
        FROM products p
        JOIN categories c ON p.category_code = c.code
        WHERE p.store_id = ?
    ''', (store_id,))
    products = cursor.fetchall()

    if products:
        print("\nСписок продуктов:")
        for product in products:
            print(f"Название продукта: {product[0]}")
            print(f"Категория: {product[1]}")
            print(f"Цена: {product[2]}")
            print(f"Количество на складе: {product[3]}\n")
    else:
        print("\nНет продуктов в выбранном магазине.\n")

while True:
    print("Вы можете отобразить список продуктов по выбранному id магазина из перечня магазинов ниже, для выхода из программы введите цифру 0:")
    stores()

    user_input = input("Введите id магазина: ")

    if user_input == '0':
        print("Выход из программы.")
        break

    try:
        store_id = int(user_input)
        if store_id <= 0:
            print("Пожалуйста, введите корректный id магазина.")
            continue

        products(store_id)
    except ValueError:
        print("Пожалуйста, введите корректное число.")

conn.close()
