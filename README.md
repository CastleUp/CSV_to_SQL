## CSV to PostgreSQL

### Порядок действий:
1. Введите в данные поля информацию о своей базе данных, в которую вы хотите положить данные из csv
```python
connection_params = {
"dbname": "",
"user": "",
"password": "",
"host": "",
"port": "",
}
```

2. В переменную **create_table_query** положите SQL скрипт с названием новой таблиц *(enstru_name)* перечислением столбцов и их типов данных *(code VARCHAR(100) и тд.)*
```python
create_table_query = sql.SQL("""
            CREATE TABLE IF NOT EXISTS enstru_name (
                code VARCHAR(100) PRIMARY KEY,
                name_ru VARCHAR(500),
                detail_ru VARCHAR(500)
            )
        """)
```
1. В переменную **insert_query** положите SQL скрипт с названием столбцов вашей таблицы. Они должны пото совпадать с названиями из скрипта выше, а так же с вашем csv файлом
``` python
insert_query = sql.SQL("""
            INSERT INTO enstru_name (
                code, name_ru, detail_ru
            ) VALUES %s
        """)
```