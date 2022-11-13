#!C:\Python310\python.exe

from database import DatabaseConnetor
import mysql.connector
import pandas as pd

class MYSQL(DatabaseConnetor):
    def __init__(self, host, port, username, password):
        super(MYSQL, self).__init__(host, port, username, password)

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host, port=self.port, user=self.username, password=self.password)
            self.cursor = self.connection.cursor()
            return True
        except Exception as e:
            print(e)
            return False


mysql = MYSQL(host='localhost', port='3306', username='test', password='test')
