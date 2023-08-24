import sqlite3


class DbOperations:
    
    def connect(self):
        conn = sqlite3.connect('database.db')
        return conn

    # Solo crea tabla de contraseñas, porque no sepuede abstraer bien
    def create_table(self, table_name="passwords"):
        conn = self.connect()
        query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            CREATE_DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            UPDATE_DATE TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            website TEXT NOT NULL,
            username VARCHAR(200),
            password VARCHAR(50)
            );
            """
        with conn as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            print("Table created successfully")
        conn.close()
