import mysql.connector
import json
import csv
import datetime
import os
import time


class database:
    def __init__(self, purge=False):
        self.database = 'db'
        self.host = '127.0.0.1'
        self.user = 'master'
        self.port = 3306
        self.password = 'master'

    def query(self, query="SELECT CURDATE()", parameters=""):

        cnx = mysql.connector.connect(host=self.host,
                                      user=self.user,
                                      password=self.password,
                                      port=self.port,
                                      database=self.database,
                                      charset='latin1')

        if parameters is not None:
            cur = cnx.cursor(dictionary=True)
            cur.execute(query, parameters)
        else:
            cur = cnx.cursor(dictionary=True)
            cur.execute(query)

        row = cur.fetchall()
        cnx.commit()

        if "INSERT" in query:
            cur.execute("SELECT LAST_INSERT_ID()")
            row = cur.fetchall()
            cnx.commit()
        cur.close()
        cnx.close()
        return row

    def createTables(self, purge=False, data_path='flask_app/database/'):

        # If purge is True, drop existing tables
        if purge:
            for table in os.listdir(data_path + 'create_tables/'):
                table_name = os.path.splitext(table)[0]
                self.query(f"DROP TABLE IF EXISTS {table}")

        for table in os.listdir(data_path + 'create_tables/'):
            table_name = os.path.splitext(table)[0]
            with open(os.path.join(data_path + 'create_tables/', table), 'r') as file:
                current_table = file.read()
                self.query(current_table)
                print(f"Created new table: {table_name}")

        # Insert data for all CSV files without caring about order
        for table in os.listdir(data_path + 'initial_data/'):
            print(f"Grabbing info from: {table}")
            table_name = os.path.splitext(table)[0]
            print(f"Inserting into: {table_name}")
            with open(os.path.join(data_path + 'initial_data/', table), 'r') as file:
                reader = csv.reader(file)
                columns = next(reader)
                for row in reader:
                    row = [None if item == 'NULL' else item for item in row]  # Replace 'NULL' string with None
                    self.insertRows(table_name, columns, [row])
                    print("Calling Insert function...")
        print("All finished!")

    def insertRows(self, table='table', columns=['x','y'], parameters=[['v11','v12'],['v21','v22']]):
        for parameter in parameters:
            query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in parameter])})"
            self.query(query, parameter)
        print(f"Inserted into table {table}.")