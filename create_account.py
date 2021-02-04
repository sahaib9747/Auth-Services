from auth import *


class CreateAccount(Authentication):
    def __init__(self):
        self.name = input("Enter your full Name: ")
        self.dob = input("Enter Data of Birth(Date-month-year): ")
        self.email = input("Enter Email Address: ")
        self.userName = input("Enter UserName: ")
        self.password = input("Enter Enter Password: ")
        self.conPassword = input("Confirm Password: ")
        self.isMatched()
        self.accountFlag = False
        self.db = ""
        super().__init__(self.userName, self.password, self.email)

    def createAccount(self):
        while self.emailFlag or self.userNameFlag:
            if self.userNameFlag:
                self.userName = input("Username exits, Re-Enter Username: ")
            if self.emailFlag:
                self.email = input("Email exits, Re-Enter Email: ")
            self.isExist()
        if not self.accountFlag:
            self.createFile()
            self.db = "user_files/" + self.userName + '.txt'
            with open(self.db, 'a') as file:  # open and write information's
                file.write(self.name + '\n')
                file.write(self.dob + '\n')
                file.write(self.userName + '\n')
                file.write(self.password + '\n')
                file.write(self.email + '\n')
            with open("auth/user_emails.txt", 'a') as emailWriter:  # write email to email files
                emailWriter.write(self.email + '\n')
            print("Account Created Successfully")

    def createFile(self):
        self.db = open("user_files/" + self.userName + '.txt', 'x')
        self.db.close()
        self.accountFlag = True

    def isMatched(self):
        while self.password != self.conPassword:
            self.conPassword = input("Password doesn't matched, please re-enter: ")
