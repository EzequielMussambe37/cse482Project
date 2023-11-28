import mysql.connector
import json
import csv
import datetime
import os
import time


class Database:
    def __init__(self, db_name, db_endpoint, db_user, db_password, db_port=3306, purge=False):
        self.database = db_name
        self.host = db_endpoint
        self.user = db_user
        self.port = db_port
        self.password = db_password

    def query(self, query="SELECT CURDATE()", parameters=None):

        cnx = mysql.connector.connect(host=self.host,
                                      user=self.user,
                                      password=self.password,
                                      port=self.port,
                                      database=self.database,
                                      charset='utf8mb4')

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

    def dropTables(self, data_path='flask_app/database/'):
        for table in os.listdir(data_path + 'create_tables/'):
            table_name = os.path.splitext(table)[0]
            self.query(f"DROP TABLE IF EXISTS {table_name}")
            print(f"Dropped table: {table_name}")

    def createTables(self, purge=False, data_path='flask_app/database/'):

        # If purge is True, drop existing tables
        if purge:
            self.dropTables()

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
                        try:
                            self.insertRows(table_name, columns, [row])
                        except mysql.connector.errors.IntegrityError as err:
                            if err.errno == 1062:
                                pass  # Ignore duplicates
                        print("Calling Insert function...")
        print("All finished!")

    def insertRows(self, table='table', columns=['x','y'], parameters=[['v11','v12'],['v21','v22']]):
        for parameter in parameters:
            query = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in parameter])})"
            self.query(query, parameter)
        print(f"Inserted into table {table}.")