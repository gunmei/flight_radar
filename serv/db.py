import psycopg2

# Настройки подключения к PostgreSQL
DB_CONFIG = {
    'dbname': 'postgres',
    'user': 'postgres',
    'password': '123456',
    'host': 'localhost',  # адрес сервера
    'port': 5432          # Стандартный порт PostgreSQL
}

# Сохраняет список рейсов в базу данных.
def save_to_db(flights):
    print("Сохранение в БД")
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        # Создание таблицы (если ее еще нет)
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS flights (
            id SERIAL PRIMARY KEY,
            aircraft VARCHAR(50),
            registration VARCHAR(50),
            altitude INTEGER,
            ground_speed INTEGER,
            heading INTEGER,
            timestamp TIMESTAMP DEFAULT NOW()
        )
        """)

        # Очистка старых данных
        cursor.execute("DELETE FROM flights")

        # Вставка новых данных
        for flight in flights:
            cursor.execute("""
            INSERT INTO flights (aircraft, registration, altitude, ground_speed, heading)
            VALUES (%s, %s, %s, %s, %s)
            """, (
                flight.get('aircraft'),
                flight.get('registration'),
                flight.get('altitude'),
                flight.get('ground_speed'),
                flight.get('heading')
            ))

        conn.commit()
    except Exception as e:
        print(f"Ошибка сохранения в базу данных: {e}")
    finally:
        if conn:
            cursor.close()
            conn.close()