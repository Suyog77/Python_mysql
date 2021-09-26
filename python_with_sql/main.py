from configparser import Interpolation
from dbhelpher import DBHelpher

def main():
    db=DBHelpher()
    while True:
        print("************WELCOME***********")
        print("PRESS 1 to insert new user")
        print("PRESS 2 to display all user")
        print("PRESS 3 to delete user")
        print("PRESS 4 to update user")
        print("PRESS 5 to Exit the program")
        print()

        try:
            choice=int(input())
            if(choice==1):
                uid=int(input("Enter ID of the user: "))
                username=input("Enter the name of user : ")
                userphone=input("Enter the phone of user")
                db.insert_user(uid,username,userphone)
                pass
            elif choice ==2:
                db.fetch_all()
                pass
            elif choice ==3:
                userid=int(input("Enter the id of user which you want to delete: "))
                db.delete_user(userid)
                pass
            elif choice ==4:
                uid=int(input("Enter ID of the user which you want to update: "))
                username=input("Enter the new name of user : ")
                userphone=input("Enter the new phone of user : ")
                db.update_user(uid,username,userphone)
                pass
            elif choice ==5:
                break
            else:
                print("invalid !!!")

        except Exception as e:
            print(e)
            print("invalid details!!")

if __name__=="__main__":
    main()