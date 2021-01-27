import sqlite3
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys





class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(600,600,1600,900)
        self.setWindowTitle("todo")
        self.initUI()

    def initUI(self):    
        self.blin = QtWidgets.QPushButton(self)
        self.blin.setText("login")
        self.blin.clicked.connect(self.login)

        self.blout = QtWidgets.QPushButton(self)
        self.blout.setText("logout")
        self.blout.clicked.connect(self.logout)
        self.blout.move(0,30)

        self.bnewa = QtWidgets.QPushButton(self)
        self.bnewa.setText("new account")
        self.bnewa.clicked.connect(self.NewAcc)
        self.bnewa.move(0,60)


        self.tlog = QtWidgets.QTextEdit(self)
        self.tlog.setText("login")
        self.tlog.move(110,0)
    
        self.tpas = QtWidgets.QTextEdit(self)
        self.tpas.setText("password")
        self.tpas.move(110,40)

           
    def login(self):
        conn = sqlite3.connect('MyDB.db')

        cursor = conn.cursor()

        cursor.execute("select ID from Users where Name=? and Password=?", [self.tlog.toPlainText(), self.tpas.toPlainText()])

        results = int(cursor.fetchone()[0])
        
        cursor.execute("update Current set UserFK=? where ID=?", [results,1])  
        
        cursor.execute("select * from Current")
        print(cursor.fetchall())
        conn.commit()
        conn.close() 


    def logout(self):
        conn = sqlite3.connect('MyDB.db')

        cursor = conn.cursor()
        
        cursor.execute("update Current set UserFK=null where ID=1")  
        
        conn.commit()
        conn.close()

    def NewAcc(self):
        conn = sqlite3.connect('MyDB.db')

        cursor = conn.cursor()

        cursor.execute("select ID from Users where Name=?", [self.tlog.toPlainText()])



        if cursor.fetchone() is None:
            #cursor.execute("SELECT MAX(ID) FROM Users")
            #lastid = int(cursor.fetchone()[0])
            cursor.execute("INSERT INTO Users(Name,SecondName,Email,Password,State,Role) VALUES(?,?,?,?,?,?)", [self.tlog.toPlainText(),'asd','asd2',self.tpas.toPlainText(), 1, 0])
            #cursor.execute("INSERT INTO Users(ID) VALUES(?)", [lastid + 1])
           # results = int(cursor.fetchone()[0])
           # print(results)
            conn.commit()
        else:
            return()


        conn.close();
        


 

def window():
    app = QApplication(sys.argv)
    win = MyWindow()

    win.show()
    sys.exit(app.exec_())

window()



