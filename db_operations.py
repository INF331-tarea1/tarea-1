import sqlite3
import logging as lg

lg.basicConfig(level=lg.DEBUG,
                    format="%(asctime)s - %(levelname)s - %(message)s",
                    datefmt="%d-%b-%y %H:%M:%S",
                    filename="main_logs.log",
                    filemode="a")


class DbOperations:
    def __init__(self, file_name="database.db"):
        try:
            self.conn = sqlite3.connect(file_name)
            lg.info("Database connected successfully")
        except Exception as e:
            lg.critical(f"Error connecting to database: {e}")
            print("Error connecting to database")
            input("Press Enter to exit...")
            exit(1)
        self.create_table()

    def close_db(self):
        self.conn.close()

    def create_table(self, table_name="passwords"):
        # conn = self.connect()
        query = f"""
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            website TEXT NOT NULL,
            username VARCHAR(256),
            password VARCHAR(64)
            );
            """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            lg.info("Table created successfully")
        # conn.close()
    
    def insert_password(self, website, username, password, table_name="passwords"):
        query_check_user = f"""
        SELECT * FROM {table_name} WHERE website = ? AND username = ?;
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query_check_user, (website, username))
            existing_user = cursor.fetchone()
            if existing_user:
                print("Username already exists for this website. Please choose a different username.")
                lg.debug("Username already exists for this website. Please choose a different username.")
                return -1
        query = f"""
        INSERT INTO {table_name} (website, username, password)
        VALUES (?, ?, ?);
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query, (website, username, password))
            lg.info(f"Password inserted successfully for the website {website} and the username {username}")
            print("Password inserted successfully")
    
    def view_password(self, website, username, table_name="passwords"):
        query = f"""
        SELECT * FROM {table_name} WHERE website = ? AND username = ?;
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query, (website, username))
            row = cursor.fetchone()
            if row:
                return row
            else:
                print("No password found for this website")
                lg.debug(f"No password found for the website {website}")
                return -1
    
    def modify_password(self, website, username, password, table_name="passwords"):
        query_check_website = f"""
        SELECT * FROM {table_name} WHERE website = ?;
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query_check_website, (website,))
            existing_website = cursor.fetchone()
            if not existing_website:
                print("Website does not exist. Cannot modify password.")
                lg.debug(f"Website {website} does not exist. Cannot modify password.")
                return -1

        query_check_user = f"""
        SELECT * FROM {table_name} WHERE website = ? AND username = ?;
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query_check_user, (website, username))
            existing_user = cursor.fetchone()
            if not existing_user:
                print("Username does not exist for this website. Cannot modify password.")
                lg.debug(f"Username {username} does not exist for this website {website}. Cannot modify password.")
                return -1

        query = f"""
        UPDATE {table_name} SET password = ? WHERE website = ? AND username = ?;
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query, (password, website, username))
            print("Password updated successfully")
            lg.info(f"Password updated successfully for the website {website} and the username {username}")
    
    def show_all_passwords(self, table_name="passwords"):
        query = f"""
        SELECT * FROM {table_name};
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                return rows
            else:
                print("No passwords found")
                lg.debug("No passwords found")
                return -1
    
    def delete_password(self, website, username, table_name="passwords"):
        query = f"""
        DELETE FROM {table_name} WHERE website = ? and username = ?;
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query, (website, username))
            print("Password deleted successfully")
            lg.info(f"Password deleted successfully for the website {website} and the username {username}")
    
    def delete_all(self, table_name="passwords"):
        query = f"""
        DELETE FROM {table_name} WHERE website != 'dummy_pass' and username != 'dummy_pas';
        """
        with self.conn as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            print("All passwords deleted successfully")
            lg.info("All passwords deleted successfully")
