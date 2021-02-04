from create_account import *
from auth import *
import os


def display():
    print("""
    1. Create Account
    2. Log in 
    3. Delete Account
    4. Help
    0. Exit
    """)


def login():
    userName = input("Enter Your User Name/ Handle: ")
    password = input("Enter Your Password: ")
    getAccess = Authentication(userName, password)
    getAccess.logIn()
    if getAccess.logFlag:
        print("log in successfully\nInformation's:")
        getAccess.getData()


def createAccount():
    createAccount = CreateAccount()
    createAccount.createAccount()


def deleteAccount():
    userName = input("Enter Your User Name/ Handle: ")
    password = input("Enter Your Password: ")
    getAccess = Authentication(userName, password)
    getAccess.logIn()
    if getAccess.existFlag and getAccess.passwordFlag:
        os.remove("user_files/" + userName + '.txt')
        print("Account Deleting......\nAccount Deleted Successfully")
    else:
        print("No account in this info")

def main():
    display()
    userChoice = input("Choose Your Option: ")
    if userChoice == "1":
        createAccount()
    elif userChoice == '2':
        login()
    elif userChoice == '3':
        deleteAccount()
    else:
        print("Please wait..... exiting")


if __name__ == "__main__":
    main()
