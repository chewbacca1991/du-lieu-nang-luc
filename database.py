import psycopg2

def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            database='your_database',
            user='your_user',
            password='your_password',
            host='localhost',
            port='5432'
        )
        return connection
    except Exception as e:
        print(f'Error connecting to database: {e}')
        return None
    # Moved closing connection to ensure it closes only when not returning the connection
    finally:
        if connection is not None:
            connection.close()