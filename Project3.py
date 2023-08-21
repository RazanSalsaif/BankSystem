import datetime
import random

class Bank:
    def __init__(self):
        self.__accounts = list()

    def add(self, account):
        self.__accounts.append(account)

    def checkAccount(self, id):
        if len(self.__accounts) == 0:
            return False

        for account in self.__accounts:
            if account.getID() == id:
                return True

        return False


    def getAccounts(self):
        return self.__accounts


    def getAccount(self, id):
        for account in self.__accounts:
            if account.getID() == id:
                return account


    def signIn(self , id='0'):
        if id == '0':
            print('please enter your account ID:')
            id = input()
            id = self.checkNum(id)

        if self.checkAccount(id):
            acc = self.getAccount(id)
            name = acc.getName().split(' ')
            print('Hello', name[0], 'How can i help you today?\n1-Withdraw\n2-Add funds'
                  '\n3-View transactions\n4-View account info\n5-Create Account\n6-Sign out\n7-Quit')
            choice = input()
            choice = self.checkNum(choice)

            while (not choice.isnumeric()) or int(choice) < 1 or int(choice) > 7:
                print('please enter a valid option!')
                choice = input()

            if choice == '1':
                print('How much would you like to withdraw from your account:')
                money = input()
                acc.withdraw(money)
                self.signIn(id)

            elif choice == '2':
                print('How much would you like to add in your account:')
                money = input()
                acc.addFund(money)
                self.signIn(id)

            elif choice == '3':
                acc.print()
                self.signIn(id)

            elif choice == '4':
                acc.getInfo()
                self.signIn(id)

            elif choice == '5':
                self.createAccount()

            elif choice == '6':
                self.start()

            elif choice == '7':
                print('\nHave a nice day!')

        else:
            print('No account was found under this ID\n')
            self.start()
    def createAccount(self):
        print('Please enter your name:')
        name = input()
        name = self.checkStr(name)

        account = Account(name)
        self.add(account)
        print('Account was created successfully!')
        print('Your account ID is:', account.getID(),'\n')
        self.signIn(account.getID())



    def start(self):
        tim = datetime.datetime.today().strftime('%p')

        if tim == 'AM':
            print('Good morning, Do you have an account or would you like to create one?\n1-Sign in\n2-Create Account')
        else:
            print('Good evening, Do you have an account or would you like to create one?\n1-Sign in\n2-Create Account')

        choice = input()
        choice = self.checkNum(choice)

        while (not choice.isnumeric()) or int(choice) < 1 or int(choice) > 2:
            print('Please make sure you have entered a correct option')
            choice = input()

        if choice == '1':
            self.signIn()

        elif choice == '2':
            self.createAccount()


    def checkNum(self, num):
        while not num.isnumeric():
            print('Please make sure the input is only numbers')
            num = input()
        return num

    def checkStr(self, text):
        while text == '' or text.isspace() or not all(chr.isalpha() or chr.isspace() for chr in text):
            print('Please make sure the input is only Alphabetic letters')
            text = input()
        return text




#################### END OF CLASS Bank



class Account:
    def __init__(self, name):
        self.__name = name
        self.__id = str(random.randint(1000,2000))
        self.__balance = 0.00
        self.__transaction = []

    def withdraw(self, money):

        while not money.isnumeric():
            print('Please Enter correct number!')
            money = input()

        if int(money) > self.__balance:
            print('Sorry you don\'t have', money, 'in your bank account\n')

        else:
            self.__balance -= int(money)
            print(money, 'SAR has been deducted from your bank balance successfully!\n')
            dt = datetime.datetime.today()
            st = (str(money) + ' SAR has been deducted from your bank account on ' +
                  dt.strftime('%A') + ', ' +dt.strftime('%d') + ' ' + dt.strftime('%B') + ' ' +
                  dt.strftime('%Y') + ', at ' + dt.strftime('%I') + ':' + dt.strftime('%M') +
                  dt.strftime('%p') + '\n')
            self.__transaction.append(st)


    def addFund(self, money):

        while not money.isnumeric():
            print('Please Enter correct number!')
            money = input()

        self.__balance += int(money)
        print(money, 'SAR has been added to your bank balance successfully!\n')
        dt = datetime.datetime.today()
        st = (str(money) + ' SAR has been added to your bank account on ' + dt.strftime('%A') +
              ', ' + dt.strftime('%d') + ' ' + dt.strftime('%B') + ' ' + dt.strftime('%Y') +
              ', at ' + dt.strftime('%I') + ':' + dt.strftime('%M') + dt.strftime('%p') + '\n')
        self.__transaction.append(st)

    def print(self):
        self.__transaction.sort(reverse = True)
        print('Transactions for', self.__name, 'bank account:\n')
        for n in self.__transaction:
            print(n)


    def getInfo(self):
        print('Your current balance is', self.__balance)
        print('Your account ID is', self.__id,'\n')

    def getID(self):
        return self.__id

    def getName(self):
        return self.__name

#################### END OF CLASS ACCOUNT

RiyadhBank = Bank()
RiyadhBank.start()




