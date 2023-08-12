import sqlite3

# Создание базы данных

def create_database():
    # Подключение к базе данных или создание файла базы данных, если он не существует
    conn = sqlite3.connect('mydatabase.db')

    # Создание курсора
    cursor = conn.cursor()

    # Создание общей таблицы со ссылками
    cursor.execute('''CREATE TABLE IF NOT EXISTS general (
                    id INTEGER PRIMARY KEY,
                    link_to_spanish INTEGER,
                    link_to_english INTEGER,
                    link_to_russian INTEGER,
                    link_to_portuguese INTEGER
                )''')

    # Создание таблицы на испанском языке
    cursor.execute('''CREATE TABLE IF NOT EXISTS spanish (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    description TEXT,
                    link TEXT
                )''')

    # Создание таблицы на английском языке
    cursor.execute('''CREATE TABLE IF NOT EXISTS english (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    description TEXT,
                    link TEXT
                )''')

    # Создание таблицы на русском языке
    cursor.execute('''CREATE TABLE IF NOT EXISTS russian (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    description TEXT,
                    link TEXT
                )''')

    # Создание таблицы на португальском языке
    cursor.execute('''CREATE TABLE IF NOT EXISTS portuguese (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    description TEXT,
                    link TEXT
                )''')

    # Сохранение изменений и закрытие соединения
    conn.commit()
    conn.close()

# Создание БД 
if __name__ == '__main__':
    create_database()


# Функция для создания соединения с базой данных
def create_connection(database_file):
    conn = sqlite3.connect(database_file)
    return conn

# Функция для выполнения SQL-запросов
def execute_query(conn, query, parameters=None):
    cursor = conn.cursor()
    if parameters:
        cursor.execute(query, parameters)
    else:
        cursor.execute(query)
    conn.commit()
    cursor.close()

# Функция для наполнения таблицы данными из массивов
def fill_table_with_data(conn, titleArray, descriptionArray, linkArray, table_name):
    for i in range(len(titleArray)):
        title = titleArray[i]
        description = descriptionArray[i]
        link = linkArray[i]

        query = f"INSERT INTO {table_name} (title, description, link) VALUES (?, ?, ?)"
        parameters = (title, description, link)
        execute_query(conn, query, parameters)
