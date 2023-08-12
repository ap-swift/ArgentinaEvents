from data import titleArray_es, descriptionArray_es, linkArray, titleArray_ru, descriptionArray_ru, titleArray_en, descriptionArray_en, titleArray_pt, descriptionArray_pt
from base import create_connection, fill_table_with_data

# Соединение с базой данных
conn = create_connection('mydatabase.db')

# Вызовите функцию для наполнения таблицы данными
fill_table_with_data(conn, titleArray_es, descriptionArray_es, linkArray, 'spanish')
fill_table_with_data(conn, titleArray_ru, descriptionArray_ru, linkArray, 'russian')
fill_table_with_data(conn, titleArray_en, descriptionArray_en, linkArray, 'english')
fill_table_with_data(conn, titleArray_pt, descriptionArray_pt, linkArray, 'portuguese')

# Закройте соединение с базой данных
conn.close()
