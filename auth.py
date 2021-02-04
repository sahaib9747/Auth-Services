class Authentication:
    def __init__(self, uName: str, password: str, email: str = None):
        self.userName = uName
        self.password = password
        self.email = email
        self.userNameFlag = False
        self.emailFlag = False
        self.logFlag = False
        self.existFlag = False
        self.isExist()
        self.passwordFlag = False

    def isExist(self):
        try:
            with open("user_files/" + self.userName + '.txt', 'r') as file:
                self.existFlag = True
                self.userNameFlag = True  # if file exists its means username already exists
        except FileNotFoundError:
            self.existFlag = False
            self.userNameFlag = False
        if self.email:  # if email has given
            with open("auth/user_emails.txt", "r") as mailFile:
                mailFile = mailFile.readlines()  # read all of mails form mail file
                for mail in mailFile:
                    if mail.strip() == self.email:  # if mail matched its means mail already exists
                        self.emailFlag = True
                        break
                else:
                    self.emailFlag = False

    def logIn(self):
        if self.existFlag:
            with open("user_files/" + self.userName + '.txt') as dataSet:  # open file is exists
                dataSet = dataSet.readlines()  # all of data as list splitting by new line.
                for logData in dataSet:  # iterating dataSet list for matching username and password.
                    # if userName matched re iterate for password.
                    if self.userName == logData.strip():
                        attempt = 10
                        while attempt:
                            for password in dataSet:
                                if password.strip() == self.password:
                                    # if matched log in success and break inner and outer
                                    self.logFlag = True
                                    self.passwordFlag = True
                                    break
                            if self.logFlag:
                                break
                            else:
                                self.password = input("Wrong password! You can try %i more times: " % (attempt - 1))
                            attempt -= 1
                    if self.logFlag:
                        break

    def getData(self):
        if self.logFlag:
            with open("user_files/" + self.userName + '.txt', 'r') as file:
                for data in file:
                    print(data.strip())
        else:
            print("No account in this info")
