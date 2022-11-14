import mysql.connector
from repository.database import DatabaseConnetor

class MYSQL(DatabaseConnetor):

    def __init__(self, host, port, username, password):
        super(MYSQL, self).__init__(host, port, username, password)
        self.cursor = None
        self.connect()
        print('MYSQL connector initialized')

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host, port=self.port, user=self.username, password=self.password)
            self.cursor = self.connection.cursor()
            return self.connection
        except Exception as e:
            print(e)
            return False

    def disconnect(self):
        try:
            self.cursor.close()
            self.connection.close()
            return True
        except Exception as e:
            print(e)
            return False

    def create_database(self, database_name):
        try:
            query = f"CREATE DATABASE IF NOT EXISTS {database_name}"
            self.cursor.execute(query)
            return True
        except Exception as e:
            print(e)
            return False

    def create_table(self, table_name, columns):
        try:
            query = f"CREATE TABLE IF NOT EXISTS {table_name} (id INT PRIMARY KEY, {columns}, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"
            self.cursor.execute(query)
            return True
        except Exception as e:
            print(e)
            return False

    def set_database(self, database_name):
        try:
            query = f"USE {database_name}"
            self.cursor.execute(query)
            return True
        except Exception as e:
            print(e)
            return False

    def insert_data(self, columns, values):
        try:
            self.cursor.execute(columns, values)
            self.connection.commit()
            return True
        except Exception as e:
            print(e)
            return False

    def get_last_row(self, table_name):
        try:
            query = f"SELECT id FROM {table_name} ORDER BY id DESC LIMIT 1"
            self.cursor.execute(query)
            return self.cursor.fetchone()
        except Exception as e:
            print(e)
            return False
