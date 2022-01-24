## 导入UI设计所需要的库
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton,  QPlainTextEdit, QWidget, QLabel, QLineEdit
from PyQt5 import QtCore
import sys

## 导入QT设计师设计的界面
from administrator import Ui_MainWindow as administrator_Ui
from user import Ui_MainWindow as user_Ui
from register import Ui_MainWindow as register_Ui

## 导入使用者数据库
import sqlite3



## 登录窗口
class MyWindow(QWidget):
    signal = 0 ## 窗口切换状态值
    def __init__(self):
        super().__init__()
        self.setWindowTitle('登录')
        self.setFixedSize(400,300)
        self.setup_ui()

    ## 进入管理员系统
    def goDeveloper(self):
        self.developer = AdministratorWindow()

        ## 载入管理员界面的UI样式
        style_administrator_file = './style/administrator.qss'
        style_administrator_sheet = QSSLoader.read_qss_file(style_administrator_file)
        self.developer.setStyleSheet(style_administrator_sheet)

        self.developer.show()
    ## 进入用户系统
    def goUser(self):
        self.user = UserWindow()

        ## 载入用户界面的UI样式
        style_user_file = './style/user.qss'
        style_user_sheet = QSSLoader.read_qss_file(style_user_file)
        self.user.setStyleSheet(style_user_sheet)

        self.user.show()
    def setup_ui(self):
        self.title = QLabel(self,text='基于Tensorflow的垃圾分类系统')
        self.title.setStyleSheet('font:25px')
        self.title.move(20,20)
        self.title.setObjectName('title')

        self.lb1 = QLabel(self,text='用户名：')
        self.lb1.setStyleSheet('font:20px')
        self.lb1.move(80,100)
        self.lb1.setObjectName('lb1')
        self.le1 =QLineEdit(self)
        self.le1.move(180,100)


        self.lb2 = QLabel(self, text='密码：')
        self.lb2.setStyleSheet('font:20px')
        self.lb2.move(100, 150)
        self.lb2.setObjectName('lb2')
        self.le2 = QLineEdit(self)
        self.le2.move(180, 150)
        # le2.setEchoMode(QLineEdit.Normal)
        self.le2.setEchoMode(QLineEdit.Password)

        self.btn1 = QPushButton(self,text=' 登录 ')
        self.btn1.move(140,200)
        self.btn1.clicked.connect(self.handleToLogin)
        self.le2.returnPressed.connect(self.handleToLogin)

        self.btn2 = QPushButton(self,text=' 注册 ')
        self.btn2.move(260,200)
        self.btn2.clicked.connect(self.handleToRegister)

    ## 登录识别
    def handleToLogin(self):
        
        conn = sqlite3.connect('resident.db')
        c = conn.cursor()
        sql = "select * from user where name = " + self.le2.text()
        c.execute(sql)
        connect = c.fetchall()[0]
        print(connect)
        if ((self.le1.text() == connect[0]) & (self.le2.text() == connect[1]) & (connect[2] == 0)):
            print('管理员登录')
            self.goDeveloper()

        if((self.le1.text() == connect[0]) & (self.le2.text() == connect[1]) & (connect[2] == 1)):
            print('用户登录')
            self.goUser()
    ## 注册账号
    def handleToRegister(self):
        self.register = RegisterWindow()

        ## 载入注册界面的UI样式
        style_register_file = './style/register.qss'
        style_register_sheet = QSSLoader.read_qss_file(style_register_file)
        self.register.setStyleSheet(style_register_sheet)

        self.register.show()
        
## 管理者窗口
class AdministratorWindow(QMainWindow,administrator_Ui):
    def __init__(self):
        super(AdministratorWindow,self).__init__()

        self.timer_camera = QtCore.QTimer()  ## 初始化定时器，主要用于摄像头的打开与关闭
        self.setupUi(self)
        self.slot_init()

## 用户窗口
class UserWindow(QMainWindow,user_Ui):
    def __init__(self):
        super(UserWindow, self).__init__()
        self.timer_camera = QtCore.QTimer()  ## 初始化定时器
        self.setupUi(self)
        self.slot_init()

## 控制器窗口，控制页面的跳转
class Controller:
    def __init__(self):
        pass
    def show_MyWindow(self):
        self.Login = MyWindow()

        ## 导入登陆界面的UI样式
        style_login_file = './style/login.qss'
        style_login_sheet = QSSLoader.read_qss_file(style_login_file)
        self.Login.setStyleSheet(style_login_sheet)

        self.Login.show()

## 注册窗口
class RegisterWindow(QMainWindow,register_Ui):
    def __init__(self):
        super(RegisterWindow,self).__init__()

        self.setupUi(self)
        self.slot_init()

## 样式类
class QSSLoader:
  def __init__(self):
    pass

  @staticmethod
  def read_qss_file(qss_file_name):
    with open(qss_file_name,'r',encoding = 'UTF-8') as file:
      return file.read()

## 主函数
def main():
    app = QApplication(sys.argv)
    controller = Controller()
    controller.show_MyWindow()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()


