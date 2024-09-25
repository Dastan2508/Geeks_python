import sqlite3


def create_database():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS countries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
    );
    ''')

    # Проверка на существование стран перед вставкой
    cursor.execute("SELECT COUNT(*) FROM countries")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO countries (title) VALUES ('Киргизия');")
        cursor.execute("INSERT INTO countries (title) VALUES ('Германия');")
        cursor.execute("INSERT INTO countries (title) VALUES ('Китай');")

    # Создание таблицы городов
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        area REAL DEFAULT 0,
        country_id INTEGER,
        FOREIGN KEY (country_id) REFERENCES countries(id)
    );
    ''')

    cursor.execute("SELECT COUNT(*) FROM cities")
    if cursor.fetchone()[0] == 0:
        cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Бишкек', 127.4, 1);")
        cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Ош', 182.3, 1);")
        cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Берлин', 891.8, 2);")
        cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Мюнхен', 310.7, 2);")
        cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Пекин', 16410.5, 3);")
        cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Шанхай', 6340.5, 3);")
        cursor.execute("INSERT INTO cities (title, area, country_id) VALUES ('Гуанчжоу', 7434.4, 3);")

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        city_id INTEGER,
        FOREIGN KEY (city_id) REFERENCES cities(id)
    );
    ''')

    cursor.execute("SELECT COUNT(*) FROM students")
    if cursor.fetchone()[0] == 0:
        students = [
            ('Иван', 'Петров', 1),
            ('Алина', 'Семенова', 1),
            ('Денис', 'Кузьмин', 2),
            ('Юлия', 'Федорова', 3),
            ('Филипп', 'Шульц', 3),
            ('Анна', 'Мюллер', 4),
            ('Жоу', 'Ван', 5),
            ('Ли', 'Чен', 6),
            ('Мэй', 'Хуанг', 7),
            ('Борис', 'Егоров', 2),
            ('Сергей', 'Новиков', 1),
            ('Ирина', 'Смирнова', 2),
            ('Чжан', 'Ли', 6),
            ('Лена', 'Майер', 4),
            ('Чен', 'Чжу', 5)
        ]
        cursor.executemany("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?);", students)

    conn.commit()
    conn.close()

    print("База данных и таблицы успешно созданы и заполнены.")


# Функция для получения списка городов
def get_cities():
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()
    conn.close()
    return cities


def get_students_by_city(city_id):
    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    query = """
    SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
    FROM students
    JOIN cities ON students.city_id = cities.id
    JOIN countries ON cities.country_id = countries.id
    WHERE cities.id = ?
    """
    cursor.execute(query, (city_id,))
    students = cursor.fetchall()
    conn.close()
    return students


def main():
    create_database()

    cities = get_cities()

    print(
        "Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

    # Печать списка городов
    for city in cities:
        print(f"{city[0]}. {city[1]}")

    while True:
        city_id = input("Введите id города: ")
        if city_id == '0':
            print("Выход из программы.")
            break

        if city_id.isdigit():
            city_id = int(city_id)
            students = get_students_by_city(city_id)
            if students:
                for student in students:
                    print(
                        f"Имя: {student[0]}, Фамилия: {student[1]}, Страна: {student[2]}, Город: {student[3]}, Площадь города: {student[4]} км²")
            else:
                print("Нет учеников в данном городе.")
        else:
            print("Некорректный ввод, попробуйте снова.")


if __name__ == "__main__":
    main()
0