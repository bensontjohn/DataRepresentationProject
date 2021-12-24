# Code adapated from https://github.com/andrewbeattycourseware/datarepresentation2021
import mysql.connector
from mysql.connector import cursor
import dbconfig as config

class OrderDAO:
    # initialise database connection variable
    db = ""
    def __init__(self):
        self.db = mysql.connector.connect(
            # 'host': 'localhost',
            # 'user': 'root',
            # 'password': 'root',
            # 'database': 'datarepresentationproject'
            host = config.mysql['host'],
            user = config.mysql['user'],
            password = config.mysql['password'],
            database = config.mysql['database']
        )
        print ("Database connection made")


#function to create/insert rows into the table
    def create(self, order):
        cursor = self.db.cursor()
        sql = "INSERT INTO customer_order (name, item, price) VALUES (%s,%s,%s)"
        values = [
           #order['id'],
            order['name'],
            order['item'],
            order['price']
        ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

#function to return all items
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'SELECT * FROM customer_order'
        cursor.execute(sql)
        results = cursor.fetchall()
        # to convert tuples to array object
        returnArray = []        
        for result in results:
            resultAsDict = self.convertToDict(result)#convert tuple into a Dict object
            returnArray.append(resultAsDict)
        return returnArray

#function to find the order by id
    def findById(self,id):        
        cursor = self.db.cursor()
        sql = 'SELECT * FROM customer_order WHERE id = %s'
        values = [id,]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        return self.convertToDict(result) 
        print(result)

#function to update       
    def update(self, order):
        cursor = self.db.cursor()
        sql = "UPDATE customer_order SET name = %s, item = %s, price = %s WHERE id = %s"
        values = [
           order['name'],
           order['item'],
           order['price'],
           order['id']
       ]
        cursor.execute(sql, values)
        self.db.commit()
        return order
    
#function to delete
    def delete(self, id):
       cursor = self.db.cursor()
       sql = 'DELETE FROM customer_order WHERE id = %s'
       values = [id]
       cursor.execute(sql, values)
    #  self.db.commit() // to delete the row
       return {}

#convert to Dict function
    def convertToDict(self, result):
        colnames = ['id','name', 'item', 'price']
        order = {}

        if result:
            for i , colName in enumerate(colnames):
                value = result[i]
                order[colName] = value
        return order   

orderDao = OrderDAO()