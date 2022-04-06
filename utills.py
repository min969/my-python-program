
import mysql.connector as mysql
import datetime

conn = mysql.connect(host="localhost", user="root", password="Marina98", db="mcdb")


def save(amount,price,description, cust_name):
    cur = conn.cursor(dictionary=True)
    qry = "INSERT INTO `customer order` (amount, price,description,cust_name) VALUES(%s,%s,%s,%s,%s)"
    cur.execute(qry, (amount, price, description, cust_name))
    conn.commit()
    return True