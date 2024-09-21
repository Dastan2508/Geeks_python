import sqlite3

def create_db():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL,
            price REAL NOT NULL DEFAULT 0.0,
            quantity INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    products = [
        ('Мыло детское', 50.50, 10),
        ('Шампунь для волос', 75.00, 5),
        ('Зубная паста', 25.50, 20),
        ('Крем для рук', 120.00, 7),
        ('Гель для душа', 60.75, 15),
        ('Бритвенные станки', 150.99, 2),
        ('Полотенце банное', 250.00, 50),
        ('Кофе растворимый', 300.50, 25),
        ('Чай черный', 200.00, 30),
        ('Конфеты шоколадные', 180.25, 40),
        ('Молоко 1л', 35.99, 100),
        ('Хлеб ржаной', 40.00, 120),
        ('Кефир 1л', 45.50, 90),
        ('Яблоки', 85.75, 70),
        ('Томатный сок', 55.00, 60)
    ]

    cursor.executemany('''
        INSERT INTO products (product_title, price, quantity)
        VALUES (?, ?, ?)
    ''', products)

    conn.commit()
    conn.close()

def update_quantity(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products SET quantity = ? WHERE id = ?
    ''', (new_quantity, product_id))
    conn.commit()
    conn.close()

def update_price(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE products SET price = ? WHERE id = ?
    ''', (new_price, product_id))
    conn.commit()
    conn.close()

def delete_product(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM products WHERE id = ?
    ''', (product_id,))
    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    for product in products:
        print(product)
    conn.close()

def get_products_by_price_and_quantity(price_limit, quantity_limit):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM products
        WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    products = cursor.fetchall()
    for product in products:
        print(product)
    conn.close()

def search_products_by_title(keyword):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM products
        WHERE product_title LIKE ?
    ''', ('%' + keyword + '%',))
    products = cursor.fetchall()
    for product in products:
        print(product)
    conn.close()

def test_functions():
    create_db()
    add_products()
    print("Все товары после добавления:")
    get_all_products()

    print("\nИзменение количества товара с ID 1 на 50:")
    update_quantity(1, 50)
    get_all_products()

    print("\nИзменение цены товара с ID 1 на 99.99:")
    update_price(1, 99.99)
    get_all_products()

    print("\nУдаление товара с ID 2:")
    delete_product(2)
    get_all_products()

    print("\nТовары дешевле 100 сом и с количеством больше 5:")
    get_products_by_price_and_quantity(100, 5)

    print("\nПоиск товаров по ключевому слову 'мыло':")
    search_products_by_title('мыло')

test_functions()
