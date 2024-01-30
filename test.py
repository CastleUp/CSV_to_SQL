import csv
import psycopg2
from psycopg2 import sql, extras

# Замените параметры подключения на свои
connection_params = {
    "dbname": "",
    "user": "",
    "password": "",
    "host": "",
    "port": "",
}

# Замените на путь к вашему CSV-файлу
csv_file_path = "путь к файлу"

# Открываем CSV-файл и читаем данные
with open(csv_file_path, newline="", encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=";")
    header = next(csv_reader)  # Пропускаем заголовок
    data = [tuple(row) for row in csv_reader]

# Подключаемся к PostgreSQL
with psycopg2.connect(**connection_params) as connection:
    with connection.cursor() as cursor:
        # Создаем таблицу, если её нет
        create_table_query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS enstru_name (
                code VARCHAR(100) PRIMARY KEY,
                name_ru VARCHAR(500),
                detail_ru VARCHAR(500)
            )
        """)
        cursor.execute(create_table_query)

        # Загружаем данные в таблицу
        insert_query = sql.SQL("""
            INSERT INTO enstru_name (
                code, name_ru, detail_ru
            ) VALUES %s
        """)
        psycopg2.extras.execute_values(cursor, insert_query, data, page_size=1000)  # Оптимизированный вставка

