import sqlite3


class DbOperations:

    def __init__(self, file_name="database.db"):
        self.conn = sqlite3.connect(file_name)
        self.create_table()
    
    # def connect(self):
    #     conn = sqlite3.connect('database.db')
    #     return conn

    def close_db(self):
        self.conn.close()
    

    # Solo crea tabla de contraseñas, porque no sepuede abstraer bien
    def create_table(self, table_name="passwords"):
        # conn = self.connect()
        query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            website TEXT NOT NULL,
            username VARCHAR(200),
            password VARCHAR(50)
            );
            """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            print("Table created successfully")
        # conn.close()
    
    def insert_password(self, website, username, password, table_name="passwords"):
        # conn = self.connect()
        query_check_user = f"""
        SELECT * FROM {table_name} WHERE website = ? AND username = ?;
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query_check_user, (website, username))
            existing_user = cursor.fetchone()
            if existing_user:
                print("Username already exists for this website. Please choose a different username.")
                return -1
        query = f"""
        INSERT INTO {table_name} (website, username, password)
        VALUES (?, ?, ?);
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query, (website, username, password))
            print("Password inserted successfully")
        # conn.close()
    
    def view_password(self, website, username, table_name="passwords"):
        # conn = self.connect()
        query = f"""
        SELECT * FROM {table_name} WHERE website = '{website}' AND username = '{username}';
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchone()
            if row:
                # print("Website: ", row[3])
                # print("Username: ", row[4])
                # print("Password: ", row[5])
                # conn.close()
                return row
            else:
                print("No password found for this website")
                return -1
        # conn.close()
    
    def modify_password(self, website, username, password, table_name="passwords"):
        # conn = self.connect()
        query_check_website = f"""
        SELECT * FROM {table_name} WHERE website = ?;
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query_check_website, (website,))
            existing_website = cursor.fetchone()
            if not existing_website:
                print("Website does not exist. Cannot modify password.")
                return -1
        
        # Check if username exists for the given website
        query_check_user = f"""
        SELECT * FROM {table_name} WHERE website = ? AND username = ?;
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query_check_user, (website, username))
            existing_user = cursor.fetchone()
            if not existing_user:
                print("Username does not exist for this website. Cannot modify password.")
                return -1

        query = f"""
        UPDATE {table_name} SET username = '{username}', password = '{password}' WHERE website = '{website}';
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            print("Password updated successfully")
        # conn.close()
    
    
    def show_all_passwords(self, table_name="passwords"):
        # conn = self.connect()
        query = f"""
        SELECT * FROM {table_name};
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                # for row in rows:
                #     print("Website: ", row[3])
                #     print("Username: ", row[4])
                #     print("Password: ", row[5])
                #     print("----------------")
                return rows
            else:
                print("No passwords found")
                return -1
        # conn.close()
    
    def delete_password(self, website, username, table_name="passwords"):
        # conn = self.connect()
        query = f"""
        DELETE FROM {table_name} WHERE website = '{website}' and username = '{username}';
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            print("Password deleted successfully")
        # conn.close()
    
    def delete_all(self, table_name="passwords"):
        # conn = self.connect()
        query = f"""
        DELETE FROM {table_name};
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            print("All passwords deleted successfully")
        # conn.close()
    
db_class = DbOperations()
db_class.insert_password("facebook", "johndoe", "123456")
a = db_class.view_password("facebook", "johndoe")
if a != -1:
    print(a)
print("----------------")
db_class.modify_password("facebook", "johndoes", "123456789")
b = db_class.view_password("facebook", "johndoes")
if b != -1:
    print(b)
print("----------------")
# db_class.delete_all()
# db_class.show_all_passwords()
