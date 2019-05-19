from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import linksql
import warning
import Operating_manager
import Operating_patient
import Operating_doctor

class Interface(object):
    def __init__(self,master=None):                #重新构造TK（）图形
        self.root=master
        self.root.title("用户登录界面")
        self.root.geometry('450x300+400+250')
        self.root.resizable(False,False)
        self.create_frame()
    def create_frame(self):                           #初始登录界面
        self.win=Frame(self.root,height=300, width=450,bg='skyblue')
        self.win.place(x=0,y=0)
        self.lab1=Label(self.win,text='用户名：',bg='skyblue',fg='blue')
        self.lab1.place(x=100,y=65)      #用户名显示框
        self.lab2=Label(self.win,text='密   码：',bg='skyblue',fg='blue')
        self.lab2.place(x=100,y=110)    #密码显示框
        self.lab3=Label(self.win,text='类   别：',fg='blue',bg='skyblue')
        self.lab3.place(x=100,y=155)    #类别显示框
        self.try1=StringVar()
        self.try2=StringVar()
        self.entry1=Entry(self.win,width=23,textvariable=self.try1)
        self.entry1.place(x=170,y=65)                     #设置用户名文本框
        self.entry2=Entry(self.win,show="*",width=23,textvariable=self.try2)
        self.entry2.place(x=170,y=110)           #设置密码文本框
        self.comb=ttk.Combobox(self.win,width=20)                                     #类别下拉框选定设置
        self.comb['values'] = ('管理员','医生','病例')
        self.comb.place(x=170,y=155)                                     
        self.btn1=Button(self.win,text='登  录',width=8,command=self.hello)
        self.btn1.place(x=128,y=200)               #设置登录选框
        self.btn2=Button(self.win,text='取  消',width=8,command=self.win.destroy)
        self.btn2.place(x=255,y=200)
    def hello(self):
        capa=self.comb.get()
        name=self.try1.get()
        word=self.try2.get()
        if capa=="管理员":
            result=linksql.SQL().list_login_manager()
            a=result.__len__()
            b=0
            for i in range(a):
                if result[i][0]==name:
                    if result[i][1]==word:
                        self.win.destroy()
                        Operating_manager.Operation(self.root)
                    else:
                        warning.warn('密码错误！').invalid_user()
                else:
                    warning.warn("该用户不存在！").invalid_user()
        elif capa=='医生':
            result=linksql.SQL().list_login_doctor()
            a=result.__len__()
            b=0
            m=''
            for i in range(a):
                if result[i][0]==name:
                    m=i
                    break
            if m=='':
                    warning.warn("该用户不存在！").invalid_user()
            if result[m][1]==word:
                self.win.destroy()
                result1=linksql.SQL().search_one_doctor1(name)
                Operating_doctor.Operation(result1[0][3],result1[0][4],self.root)
            elif result[m][1]!=word:
                    warning.warn('密码错误！').invalid_user()
        elif capa=='病例':
            result=linksql.SQL().list_login_patient()
            a=result.__len__()
            b=0
            m=''
            for i in range(a):
                if result[i][0]==name:
                    m=i
                    break
            if m=='':
                    warning.warn("该用户不存在！").invalid_user()
            if result[m][1]==word:
                result1=linksql.SQL().search_one_patient1(name)
                self.win.destroy()
                Operating_patient.Operation(result1[0][2],self.root)
            elif result[m][1]!=word:
                    warning.warn('密码错误！').invalid_user()
        else:
            warning.warn("悟空，你又调皮了！！！").invalid_user()