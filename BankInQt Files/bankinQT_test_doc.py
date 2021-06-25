import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QWidget, QLineEdit, QVBoxLayout, QGridLayout, QMessageBox, QFileDialog
from PyQt5.QtCore import Qt, QRegExp 
from PyQt5.QtGui import QRegExpValidator

class depositMoneySavings(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Deposit Money')
        self.setFixedSize(260, 100)
        self.resize(260, 100)


        layout = QGridLayout()


        label_name = QLabel('Deposit money') 
        self.lineEdit_deposit = QLineEdit() 
        self.lineEdit_deposit.setPlaceholderText('Enter amount here....')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_deposit, 0, 1)
        

        button = QPushButton('Deposit')
        button.clicked.connect(self.hide)
        layout.addWidget(button, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        button.clicked.connect(self.saveInfo)

        self.setLayout(layout)

    def saveInfo(self):
        list_1=[]
        un='Eliot'
        pw='1234'
        login=False
        file = open('create_account.txt', 'r')
        for line in file:
            list_1.append((line[:(len(line)-1)]).split())
        file.close()
        for item in list_1:
            if un==item[0] and pw==item[1]:
                login=True
                index=list_1.index(item)

        print(list_1)



        am = self.lineEdit_deposit.text()

        bal=int(list_1[index][3])
        print(bal)

        bal += int(am)
        print(bal)

        print(list_1[index][3])
        list_1[index][3]=int(list_1[index][3])+int(am)
        print(list_1)


        file = open('create_account.txt', 'w')
        #for line in file:
            #list_1.append((line[:(len(line)-1)]).split())

        for item in list_1:
            file.write(str(item[0])+' '+str(item[1])+' '+str(item[2])+' '+str(item[3])+'\n')
        file.close()


class withDrawMoneySavings(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Deposit Money')
        self.setFixedSize(260, 100)
        self.resize(260, 100)


        layout = QGridLayout()


        label_name = QLabel('Deposit money') 
        self.lineEdit_deposit = QLineEdit() 
        self.lineEdit_deposit.setPlaceholderText('Enter amount here....')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_deposit, 0, 1)
        

        button = QPushButton('Deposit')
        button.clicked.connect(self.hide)
        layout.addWidget(button, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        button.clicked.connect(self.saveInfo)

        self.setLayout(layout)

    def saveInfo(self):
        list_1=[]
        un='Eliot'
        pw='1234'
        login=False
        file = open('create_account.txt', 'r')
        for line in file:
            list_1.append((line[:(len(line)-1)]).split())
        file.close()
        for item in list_1:
            if un==item[0] and pw==item[1]:
                login=True
                index=list_1.index(item)

        print(list_1)



        am = self.lineEdit_deposit.text()

        bal=int(list_1[index][3])
        print(bal)

        bal -= int(am)
        print(bal)

        print(list_1[index][3])
        list_1[index][3]=int(list_1[index][3])-int(am)
        print(list_1)


        file = open('create_account.txt', 'w')
        #for line in file:
            #list_1.append((line[:(len(line)-1)]).split())

        for item in list_1:
            file.write(str(item[0])+' '+str(item[1])+' '+str(item[2])+' '+str(item[3])+'\n')
        file.close()

class createAccount(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Create account')
        self.setFixedSize(640, 480)
        self.resize(640, 480)
        
        layout = QGridLayout()

        # Username box
        label_name_create = QLabel('New Username')  # Creates label
        self.lineEdit_username = QLineEdit()  # Essentially adds a text box
        # Placeholder text that sits in the text box
        self.lineEdit_username.setPlaceholderText('Enter a new username here....')
        layout.addWidget(label_name_create, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        # Password box
        label_password_create = QLabel('New Password')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Enter a new password here....')
        layout.addWidget(label_password_create, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        button = QPushButton('Create account')
        layout.addWidget(button, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        button.clicked.connect(self.saveInfo)
        button.clicked.connect(self.mainWindow)

        self.button = QPushButton('Go back', self)
        self.button.move(20, 430)
        self.button.clicked.connect(self.mainWindow)

        self.setLayout(layout)


    def saveInfo(self):
        fileName = open("create_account.txt", 'a')
        textUser = self.lineEdit_username.text()
        textPasswd = self.lineEdit_password.text()
        fileName.write((textUser) + " " + (textPasswd))
        fileName.write("\n")
        fileName.close()


    def mainWindow(self):
        self.w = MainWindow()
        self.w.show()
        self.hide()

class depositMoney(QWidget):
    def __init__(self):
        super().__init__() # Allows you to use method from your superclass in your subclass
        
        self.setWindowTitle('Deposit Money')
        self.setFixedSize(260, 100)
        self.resize(260, 100)


        layout = QGridLayout()


        label_name = QLabel('Deposit money') 
        self.lineEdit_deposit = QLineEdit() 
        self.lineEdit_deposit.setPlaceholderText('Enter amount here....')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_deposit, 0, 1)
        

        button = QPushButton('Deposit')
        button.clicked.connect(self.hide)
        layout.addWidget(button, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        button.clicked.connect(self.saveInfo)

        self.setLayout(layout)

    def saveInfo(self):
        list_1=[]
        un='Eliot'
        pw='1234'
        login=False
        file = open('create_account.txt', 'r')
        for line in file:
            list_1.append((line[:(len(line)-1)]).split())
        file.close()
        for item in list_1:
            if un==item[0] and pw==item[1]:
                login=True
                index=list_1.index(item)

        print(list_1)



        am = self.lineEdit_deposit.text()

        bal=int(list_1[index][2])
        print(bal)

        bal += int(am)
        print(bal)

        print(list_1[index][2])
        list_1[index][2]=int(list_1[index][2])+int(am)
        print(list_1)


        file = open('create_account.txt', 'w')
        #for line in file:
            #list_1.append((line[:(len(line)-1)]).split())

        for item in list_1:
            file.write(str(item[0])+' '+str(item[1])+' '+str(item[2])+' '+str(item[3])+'\n')
        file.close()
        

class withDrawMoney(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Withdraw Money')
        self.setFixedSize(260, 100)
        self.resize(260, 100)


        layout = QGridLayout()


        label_name = QLabel('Withdraw money') 
        self.lineEdit_withdraw = QLineEdit() 
        self.lineEdit_withdraw.setPlaceholderText('Enter amount here....')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_withdraw, 0, 1)
        

        button = QPushButton('Withdraw')
        button.clicked.connect(self.hide)
        layout.addWidget(button, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)
        button.clicked.connect(self.saveInfo)

        self.setLayout(layout)

    def saveInfo(self):
        list_1=[]
        un='Eliot'
        pw='1234'
        login=False
        file = open('create_account.txt', 'r')
        for line in file:
            list_1.append((line[:(len(line)-1)]).split())
        file.close()
        for item in list_1:
            if un==item[0] and pw==item[1]:
                login=True
                index=list_1.index(item)

        print(list_1)



        am = self.lineEdit_withdraw.text()

        bal=int(list_1[index][2])
        print(bal)

        bal -= int(am)
        print(bal)

        print(list_1[index][2])
        list_1[index][2]=int(list_1[index][2])-int(am)
        print(list_1)


        file = open('create_account.txt', 'w')
        #for line in file:
            #list_1.append((line[:(len(line)-1)]).split())

        for item in list_1:
            file.write(str(item[0])+' '+str(item[1])+' '+str(item[2])+' '+str(item[3])+'\n')
        file.close()



# Savings accounts page 
class SavingsAccount(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle('Savings Account')
        self.setFixedSize(640, 480)
        self.resize(640, 480)


        layout = QGridLayout()



        label = QLabel('<font size="8"> Savings Account </font>')
        self.setCentralWidget(label)
        label.setAlignment(Qt.AlignHCenter)

        # View balence button 
        self.button = QPushButton('View balence', self)
        self.setToolTip('This is a button')
        self.button.move(20, 180)
        self.button.resize(100, 100)
        self.button.clicked.connect(self.showBalence)

        self.button = QPushButton('Withdraw money', self) 
        self.button.setToolTip('This is a button')
        self.button.move(270, 180)
        self.button.resize(100, 100)
        self.button.clicked.connect(self.withDrawMoneySavings)

        self.button = QPushButton('Deposit funds', self) 
        self.button.setToolTip('This is a button')
        self.button.move(520, 180)
        self.button.resize(100, 100)
        self.button.clicked.connect(self.depositMoneySavings)

        self.button = QPushButton('Go back', self)
        self.button.move(20, 430)
        self.button.clicked.connect(self.Window3)

        self.setLayout(layout)

    def showBalence(self):
        message = QMessageBox()

        file = open("create_account.txt", "r")
        lines = file.readlines()
        result = []

        for x in open("create_account.txt", "r"):
            
            result.append((x[:(len(x)-1)]).split())



        #file.close()
        
        #print(result)


        bal = int(result[index][3])
        print(bal)

        message.setWindowTitle('Current Balence')
        message.setText("£" + str(bal))
        message.exec_()

    def withDrawMoneySavings(self):
        self.w = withDrawMoneySavings()
        self.w.show()

    def depositMoneySavings(self):
        self.w = depositMoneySavings()
        self.w.show()

    def Window3(self):
        self.w = Window3()
        self.w.show()
        self.hide()
    
        

# Current accounts page
class CurrentAccounts(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Current Account')
        self.setFixedSize(640, 480)
        self.resize(640, 480)

        layout = QGridLayout()

        label = QLabel('<font size="8"> Current Account </font>') # '<font size="NUMBER GOES HERE" ></font> changes font size 
        self.setCentralWidget(label)
        label.setAlignment(Qt.AlignHCenter) # Aligns text at top center

        # View balence button 
        self.button = QPushButton('View balence', self)
        self.setToolTip('This is a button')
        self.button.move(20, 180)
        self.button.resize(100, 100)
        self.button.clicked.connect(self.showBalence)

        self.button = QPushButton('Withdraw money', self) 
        self.button.setToolTip('This is a button')
        self.button.move(270, 180)
        self.button.resize(100, 100)
        self.button.clicked.connect(self.withDrawMoney)

        self.button = QPushButton('Deposit funds', self) 
        self.button.setToolTip('This is a button')
        self.button.move(520, 180)
        self.button.resize(100, 100)
        self.button.clicked.connect(self.depositMoney)

        self.button = QPushButton('Go back', self)
        self.button.move(20, 430)
        self.button.clicked.connect(self.Window3)

        self.setLayout(layout)

    # Shows dialog box on button click
    def showBalence(self):
        message = QMessageBox()

        file = open("create_account.txt", "r")
        lines = file.readlines()
        result = []

        for x in open("create_account.txt", "r"):
            
            result.append((x[:(len(x)-1)]).split())



        #file.close()
        
        #print(result)


        bal = int(result[index][2])
        print(bal)

        message.setWindowTitle('Current Balence')
        message.setText("£" + str(bal))
        message.exec_()

    def withDrawMoney(self):
        self.w = withDrawMoney()
        self.w.show()

    def depositMoney(self):
        self.w = depositMoney()
        self.w.show()

    def Window3(self):
        self.w = Window3()
        self.w.show()
        self.hide()

# Main menu 
class Window3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Menu')
        self.setFixedSize(640, 480)
        self.resize(640, 480)

        layout = QGridLayout()

        label = QLabel('<font size="8"> Main Menu </font>') # '<font size="NUMBER GOES HERE" ></font> changes font size 
        self.setCentralWidget(label)
        label.setAlignment(Qt.AlignHCenter) #Aligns text at top center 

        self.button = QPushButton('Current account', self) 
        self.button.setToolTip('This is a button')
        self.button.move(140, 220)
        self.button.resize(100, 100)
        self.button.clicked.connect(self.CurrentAccounts) #Loads new page on button click 

        self.button = QPushButton('Savings account', self) 
        self.button.setToolTip('This is a button')
        self.button.move(360, 220)
        self.button.resize(100, 100)
        self.button.clicked.connect(self.SavingsAccount) #Loads new page on button click 

        

        self.button = QPushButton('Go back', self)
        self.button.move(20, 430)
        self.button.clicked.connect(self.Window2)

        self.setLayout(layout)

    def CurrentAccounts(self):
        self.w = CurrentAccounts()
        self.w.show()
        self.hide()

    def SavingsAccount(self):
        self.w = SavingsAccount()
        self.w.show()
        self.hide()
    
    def Window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setFixedSize(640, 480)
        self.resize(640, 480)
        
        layout = QGridLayout()

        # Username box
        label_name = QLabel('Username')  # Creates label
        self.lineEdit_username = QLineEdit()  # Essentially adds a text box
        # Placeholder text that sits in the text box
        self.lineEdit_username.setPlaceholderText('Enter your username')
        layout.addWidget(label_name, 0, 0)
        layout.addWidget(self.lineEdit_username, 0, 1)

        # Password box
        label_password = QLabel('Password')
        self.lineEdit_password = QLineEdit()
        self.lineEdit_password.setPlaceholderText('Enter your password')
        layout.addWidget(label_password, 1, 0)
        layout.addWidget(self.lineEdit_password, 1, 1)

        # Login button
        button = QPushButton('Login')
        button.clicked.connect(self.check_password)
        layout.addWidget(button, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.button = QPushButton('Go back', self)
        self.button.move(20, 430)
        self.button.clicked.connect(self.mainWindow)

        self.setLayout(layout)

    def mainWindow(self):
        self.w = MainWindow()
        self.w.show()
        self.hide()

    # Checks to see if username and password are correct 
    def check_password(self):
        global index
        message = QMessageBox()


        file = open("create_account.txt", "r")

        accountLists = []

        for line in file:
            accountLists.append((line[:(len(line)-1)]).split())

        self.login=False

        for item in accountLists:
            if self.lineEdit_username.text() == item[0] and  self.lineEdit_password.text() == item[1]:
                self.login = True

                index = accountLists.index(item)

            
        if self.login == True:
            message.setText('Welcome!')
            message.setWindowTitle('Welcome')
            message.exec_()
            self.Window3()

        else:
            message.setText('Try again')
            message.setWindowTitle('Try again')
            message.exec_()
            


    def Window3(self):
        self.w = Window3()
        self.w.show()
        self.hide()
    
      
# Start screen 
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("Login")

        label = QLabel('<font size="8">Welcome!</font>')
        label.setAlignment(Qt.AlignHCenter)

        self.setCentralWidget(label)

        self.setFixedSize(640, 480)

        self.resize(640, 480)

        self.mainWindow()

    def mainWindow(self):

        # Adds button 
        self.button = QPushButton('Login', self) 
        self.button.setToolTip('This is a button')
        self.button.move(140, 220)
        self.button.resize(140, 80)
        self.button.clicked.connect(self.Window2)

        self.button = QPushButton('Create account', self) 
        self.button.setToolTip('This is a button')
        self.button.move(360, 220)
        self.button.resize(140, 80)
        self.button.clicked.connect(self.createAccount)

        self.show()

    def createAccount(self):
        self.w = createAccount()
        self.w.show()
        self.hide()
        
    def Window2(self):
        self.w = Window2()
        self.w.show()
        self.hide()


app = QApplication(sys.argv)

window = MainWindow()
window.show() 

# Start the event loop.
app.exec_()





# ************
# * Sources: *
# ************
# Elliot Antunes - Helping setting up reading usernames and passwords from text file and validating them and for adding and subtracting
# Learning what 'super().__init__()' does - https://realpython.com/python-super/
# For various things - https://pythonprogramminglanguage.com/
# Used to learn how to make the main window - https://www.learnpyqt.com/tutorials/creating-your-first-window/
# Used to learn how to make the login screen - https://learndataanalysis.org/create-a-simple-login-form-pyqt5-tutorial/
# https://www.google.com/


# © Eliot Poynton