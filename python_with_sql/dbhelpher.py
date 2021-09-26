import mysql.connector as connector


class DBHelpher:
    def __init__(self):
        self.con = connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='never settle',
            database='pythontest'
        )
        query = 'create table if not exists user (userId int primary key,userName varchar(200),phone varchar(12))'
        cur = self.con.cursor()
        cur.execute(query)
        print("Created")

    # Insert
    def insert_user(self, userId, userName, phone):
        query = "insert into user(userid,username,phone) values({},'{}','{}')".format(
            userId, userName, phone)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("user saved to db")

    # fetch all
    def fetch_all(self):
        query = "select * from user"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("user Id : ", row[0])
            print("user Name : ", row[1])
            print("user phone : ", row[2])
            print()
            print()

    # Delete
    def delete_user(self, userId):
        query = "delete from user where userId = {}".format(userId)
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("Deleted")

    # Update
    def update_user(self, userId, newName, newphone):
        query = "Update user set userName='{}',phone ='{}'where userId={}".format(newName,newphone,userId)
        print(query)       
        c = self.con.cursor()
        c.execute(query)
        self.con.commit()
        print("Updated")