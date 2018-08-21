import pymysql

def connect():
 return pymysql.connect(host="localhost" , user="root" ,passwd="" ,db="minorproject")
