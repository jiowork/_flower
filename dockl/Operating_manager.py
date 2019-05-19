from tkinter import *
from tkinter import ttk
from tkinter import messagebox as me
from tkinter.ttk import Treeview
import tkinter.font
import linksql
import warning

 
class Operation(object):
    def __init__(self,master=None):            #重新构造TK（）图形
        self.root=master
        self.root.title("                                                                                                                                          管理员操作界面")
        self.root.geometry('970x620+200+70')
        self.root.resizable(False,False)
        self.createPage()
    def createPage(self):                    #初始操作界面
        self.win=Frame(self.root,width=970,height=620)
        self.win.place(x=0,y=0)
        self.ft=tkinter.font.Font(family='Fixdsys',size=12,weight='bold')
        self.cv=Canvas(self.win,width=800,height=750)
        self.cv1=Canvas(self.win,bg="skyblue",width=120,height=605)
        self.cv1.place(x=2,y=3)
        self.cv2=Canvas(self.win,bg="gray",width=820,height=605)
        self.cv2.place(x=130,y=3)
        self.btn1=Button(self.win,text="查   看",font=self.ft,width=10,height=2,command=self.view_interface)
        self.btn1.place(x=11,y=80)
        self.btn5=Button(self.win,text='搜   索',font=self.ft,width=10,height=2,command=self.search_interface)
        self.btn5.place(x=11,y=180)
        self.btn2=Button(self.win,text="添   加",font=self.ft,width=10,height=2,command=self.add_interface)
        self.btn2.place(x=11,y=280)
        self.btn3=Button(self.win,text="修   改",font=self.ft,width=10,height=2,command=self.update_interface)
        self.btn3.place(x=11,y=380)
        self.btn4=Button(self.win,text="删   除",font=self.ft,width=10,height=2,command=self.delete_interface)
        self.btn4.place(x=11,y=480)
        self.view_start()
        self.win.mainloop()
    def view_start(self):
        cv=Canvas(self.win,bg="gray",width=820,height=605)
        im_start=PhotoImage(file='imgs/left.png')
        cv.create_image((820,609),Image=im_start)
        cv.place(x=130,y=3)
    def view_interface(self):                          #管理员查看界面
        cv=Canvas(self.win,bg="gray",width=820,height=605)
        cv.place(x=130,y=3)
        cv1=Canvas(self.win,bg="gray",width=810,height=50)
        cv1.place(x=135,y=8)
        lab1=Label(cv1,text='搜 索 类 型',bg='gray',width=10)
        lab1.place(x=10,y=15)
        self.comb1=ttk.Combobox(cv1,width=20)         
        self.comb1['values'] = ('医生','病例')
        self.comb1.place(x=100,y=15)
        btn1=Button(cv1,text='开始检索',command=self.view_list)
        btn1.place(x=300,y=12)
    def view_list(self):                            #view列表
        value=self.comb1.get()
        cv1=Canvas(self.win,bg="pink",width=810,height=540)
        cv1.place(x=135,y=61)
        frame = Frame(cv1)
        frame.place(x=5, y=8, width=804, height=530)
        scrollBar = Scrollbar(frame)
        scrollBar.pack(side=RIGHT, fill=Y)
        tree = Treeview(frame,columns=('c1', 'c2', 'c3','c4', 'c5', 'c6','c7','c8'),show="headings",yscrollcommand=scrollBar.set)
        tree.column('c1', width=150, anchor='center')
        tree.column('c2', width=105, anchor='center')
        tree.column('c3', width=70, anchor='center')
        tree.column('c4', width=70, anchor='center')
        tree.column('c5', width=90, anchor='center')
        tree.column('c6', width=105, anchor='center')
        tree.column('c7', width=105, anchor='center')
        tree.column('c8', width=90, anchor='center')

        if value=='医生':
            tree.heading('c1', text='ID')
            tree.heading('c2', text='姓名')
            tree.heading('c3', text='性别')
            tree.heading('c4', text='年龄')
            tree.heading('c5', text='类别')
            tree.heading('c6', text='电话')
            tree.heading('c7', text='科室')
            tree.heading('c8', text='职务')
            tree.pack(side=LEFT, fill=Y)
            scrollBar.config(command=tree.yview)
            result=linksql.SQL().search_all_doctor()
            num=result.__len__()
            for i in range(num):
                tree.insert('',i,values=(result[i][0],result[i][1],result[i][2],result[i][3],result[i][4],result[i][5],result[i][6],result[i][7]))
        elif value=='病例':
            tree.heading('c1', text='ID')
            tree.heading('c2', text='姓名')
            tree.heading('c3', text='性别')
            tree.heading('c4', text='年龄')
            tree.heading('c5', text='类别')
            tree.heading('c6', text='电话')
            tree.heading('c7', text='科室')
            tree.heading('c8', text='主治医生')
            # tree.heading('c9', text='其他')
            tree.pack(side=LEFT, fill=Y)
            scrollBar.config(command=tree.yview)
            result=linksql.SQL().search_all_doctor()
            result=linksql.SQL().serach_all_patient()
            num=result.__len__()
            for i in range(num):
                tree.insert('',i,values=(result[i][0],result[i][1],result[i][2],result[i][3],result[i][4],result[i][5],result[i][6],result[i][7]))
        else :
            warning.warn("请正确输入信息！").invalid_user()
    def search_interface(self):           #管理员搜索界面
        self.try1=StringVar()
        self.try2=StringVar()
        self.try3=StringVar()
        self.try4=StringVar()
        cv=Canvas(self.win,bg="gray",width=820,height=605)
        cv.place(x=130,y=3)
        cv1=Canvas(self.win,bg="gray",width=810,height=120)
        cv1.place(x=135,y=8)
        lab1=Label(cv1,text='I D 号',bg='gray',width=10)
        lab1.place(x=10,y=5)
        self.entry1=Entry(cv1,textvariable=self.try1)
        self.entry1.place(x=80,y=5)
        lab2=Label(cv1,text='姓   名',bg='gray',width=10)
        lab2.place(x=10,y=35)
        self.entry2=Entry(cv1,textvariable=self.try2)
        self.entry2.place(x=80,y=35)
        lab3=Label(cv1,text='科   室',bg='gray',width=10)
        lab3.place(x=10,y=65)
        self.entry3=Entry(cv1,textvariable=self.try3)
        self.entry3.place(x=80,y=65)
        lab4=Label(cv1,text='搜索类型',bg='gray',width=10)
        lab4.place(x=10,y=95)
        self.comb2=ttk.Combobox(cv1,width=17)         
        self.comb2['values'] = ('医生','病例')
        self.comb2.place(x=80,y=95)
        btn1=Button(cv1,text=' 开  始  检  索 ',command=self.search_list)
        btn1.place(x=320,y=50)
        lab=Label(cv1,text='搜索类型  不可为空！！！',bg='gray',fg='red')
        lab.place(x=670,y=100)
    def search_list(self):             #search列表
        idd=self.entry1.get()
        name=self.entry2.get()
        depart=self.entry3.get()
        value=self.comb2.get()
        cv1=Canvas(self.win,bg="pink",width=810,height=473)
        cv1.place(x=135,y=130)
        if value=='医生' :
            frame1 = Frame(cv1)
            frame1.place(x=5, y=5, width=804, height=530)
            scrollBar1 = Scrollbar(frame1)
            scrollBar1.pack(side=RIGHT, fill=Y)
            tree1 = Treeview(frame1,columns=('c1', 'c2', 'c3','c4', 'c5', 'c6','c7','c8'),show="headings",yscrollcommand=scrollBar1.set)
            tree1.column('c1', width=150, anchor='center')
            tree1.column('c2', width=105, anchor='center')
            tree1.column('c3', width=70, anchor='center')
            tree1.column('c4', width=70, anchor='center')
            tree1.column('c5', width=90, anchor='center')
            tree1.column('c6', width=105, anchor='center')
            tree1.column('c7', width=105, anchor='center')
            tree1.column('c8', width=90, anchor='center')
            tree1.heading('c1', text='ID')
            tree1.heading('c2', text='姓名')
            tree1.heading('c3', text='性别')
            tree1.heading('c4', text='年龄')
            tree1.heading('c5', text='类别')
            tree1.heading('c6', text='电话')
            tree1.heading('c7', text='科室')
            tree1.heading('c8', text='职务')
            tree1.pack(side=LEFT, fill=Y)
            scrollBar1.config(command=tree1.yview)
            if idd!='':             #只是当id不为空时
                result1=linksql.SQL().search_one_doctor2(idd)
                tree1.insert('',0,values=(result1[0][0],result1[0][1],result1[0][2],result1[0][3],result1[0][4],result1[0][5],result1[0][6],result1[0][7]))
            elif idd=='':           
                if depart=='':  #当id为空时，科室为空时
                    if name!='':   
                        result1=linksql.SQL().search_all_doctor1(name)
                        num1=result1.__len__()
                        for i in range(num1):
                            tree1.insert('',i,values=(result1[i][0],result1[i][1],result1[i][2],result1[i][3],result1[i][4],result1[i][5],result1[i][6],result1[i][7]))
                    elif name=='': #当ID为空，科室为空，姓名为空时
                        result1=linksql.SQL().search_all_doctor()
                        num1=result1.__len__()
                        for i in range(num1):
                            tree1.insert('',i,values=(result1[i][0],result1[i][1],result1[i][2],result1[i][3],result1[i][4],result1[i][5],result1[i][6],result1[i][7]))
                elif depart!='':
                    if name=='':    #当科室不为空，姓名为空时
                        result1=linksql.SQL().search_all_doctor2(depart)
                        num1=result1.__len__()
                        for i in range(num1):
                           tree1.insert('',i,values=(result1[i][0],result1[i][1],result1[i][2],result1[i][3],result1[i][4],result1[i][5],result1[i][6],result1[i][7],result1[0][8]))
                    elif name!='':   #当科室不为空，姓名不为空时
                        result1=linksql.SQL().search_all_doctor3(name,depart)
                        num1=result1.__len__()
                        for i in range(num1):
                               tree1.insert('',i,values=(result1[i][0],result1[i][1],result1[i][2],result1[i][3],result1[i][4],result1[i][5],result1[i][6],result1[i][7],result1[0][8]))
        elif value=='病例':
            frame2 = Frame(cv1)
            frame2.place(x=5, y=5, width=804, height=530)
            scrollBar2 = Scrollbar(frame2)
            scrollBar2.pack(side=RIGHT, fill=Y)
            tree2 = Treeview(frame2,columns=('c1', 'c2', 'c3','c4', 'c5', 'c6','c7','c8'),show="headings",yscrollcommand=scrollBar2.set)
            tree2.column('c1', width=150, anchor='center')
            tree2.column('c2', width=70, anchor='center')
            tree2.column('c3', width=70, anchor='center')
            tree2.column('c4', width=70, anchor='center')
            tree2.column('c5', width=75, anchor='center')
            tree2.column('c6', width=150, anchor='center')
            tree2.column('c7', width=105, anchor='center')
            tree2.column('c8', width=90, anchor='center')
            tree2.heading('c1', text='ID')
            tree2.heading('c2', text='姓名')
            tree2.heading('c3', text='性别')
            tree2.heading('c4', text='年龄')
            tree2.heading('c5', text='类别')
            tree2.heading('c6', text='电话')
            tree2.heading('c7', text='科室')
            tree2.heading('c8', text='主治医生')
            tree2.pack(side=LEFT, fill=Y)
            scrollBar2.config(command=tree2.yview)
            if idd!='':             #只是当id不为空时
                result1=linksql.SQL().search_one_patient2(idd)
                tree2.insert('',0,values=(result1[0][0],result1[0][1],result1[0][2],result1[0][3],result1[0][4],result1[0][5],result1[0][6],result1[0][7]))
            elif idd=='':           
                if depart=='':        #当id为空时，科室为空时
                    if name!='':
                        result1=linksql.SQL().search_all_patient1(name)
                        num1=result1.__len__()
                        for i in range(num1):
                            tree2.insert('',i,values=(result1[i][0],result1[i][1],result1[i][2],result1[i][3],result1[i][4],result1[i][5],result1[i][6],result1[i][7])) 
                    elif name=='': #当ID为空，科室为空，姓名为空时
                        result1=linksql.SQL().serach_all_patient()
                        num1=result1.__len__()
                        for i in range(num1):
                            tree2.insert('',i,values=(result1[i][0],result1[i][1],result1[i][2],result1[i][3],result1[i][4],result1[i][5],result1[i][6],result1[i][7]))
                elif depart!='':
                    if name=='':    #当科室不为空，姓名为空时
                        result1=linksql.SQL().search_all_patient2(depart)
                        num1=result1.__len__()
                        for i in range(num1):
                           tree2.insert('',i,values=(result1[i][0],result1[i][1],result1[i][2],result1[i][3],result1[i][4],result1[i][5],result1[i][6],result1[i][7]))
                    elif name!='':   #当科室不为空，姓名不为空时
                        result1=linksql.SQL().search_all_patient3(name,depart)
                        num1=result1.__len__()
                        for i in range(num1):
                               tree2.insert('',i,values=(result1[i][0],result1[i][1],result1[i][2],result1[i][3],result1[i][4],result1[i][5],result1[i][6],result1[i][7]))  
        else :
            frame2 = Frame(cv1)
            frame2.place(x=5, y=5, width=804, height=530)
            warning.warn('请正确选择搜索类型').invalid_user()
    def add_interface(self):                                             #管理员添加界面
        cv=Canvas(self.win,bg="gray",width=820,height=605)
        cv.place(x=130,y=3)
        cv1=Canvas(self.win,bg="gray",width=810,height=50)
        cv1.place(x=135,y=8)
        lab1=Label(cv1,text='添 加 类 型',bg='gray',width=10)
        lab1.place(x=10,y=15)
        self.comb1=ttk.Combobox(cv1,width=20)         
        self.comb1['values'] = ('医生','病例')
        self.comb1.place(x=100,y=15)
        btn1=Button(cv1,text='开始检索',command=self.add_interface_list)
        btn1.place(x=300,y=12)
    def add_interface_list(self):
        value=self.comb1.get()
        cv1=Canvas(self.win,bg="pink",width=810,height=540)
        cv1.place(x=135,y=61)
        # self.frame1=Frame(cv1,bg='white')
        # self.frame1.place(x=5, y=5, width=804, height=530)
        self.frame2 = Frame(cv1,bg='white')
        self.frame2.place(x=5, y=5, width=804, height=530)
        bm_right=PhotoImage(file='imgs/right.png')
        bm_left=PhotoImage(file='imgs/left.png')
        self.try5=StringVar()
        self.try6=StringVar()
        self.try7=StringVar()
        self.try8=StringVar()
        self.try9=StringVar()
        self.try10=StringVar()
        self.try11=StringVar()
        self.try12=StringVar()
        if value=='病例':
            frame = Frame(self.frame2,bg='gray')
            frame.place(x=240, y=5, width=310, height=500)
            lab_left=Label(self.frame2,image=bm_left,width=220)
            lab_left.bm=bm_left
            lab_left.place(x=0,y=0)
            lab_right=Label(self.frame2,image=bm_right,width=220)
            lab_right.bm=bm_right
            lab_right.place(x=560,y=0)
            title=self.comb1.get()
            title=title+'添加界面'
            lab1=Label(frame,text='{}'.format(title),bg='gray')
            lab1.place(x=115,y=20)
            lab2=Label(frame,text='姓  名',bg='gray',width=10)
            lab2.place(x=2,y=70)
            lab3=Label(frame,text='性  别',bg='gray',width=10)
            lab3.place(x=2,y=120)
            lab4=Label(frame,text='年  龄',bg='gray',width=10)
            lab4.place(x=2,y=170)
            lab5=Label(frame,text='类  别',bg='gray',width=10)
            lab5.place(x=2,y=220)
            lab6=Label(frame,text='电  话',bg='gray',width=10)
            lab6.place(x=2,y=270)
            lab7=Label(frame,text='科  室',bg='gray',width=10)
            lab7.place(x=2,y=320)
            lab8=Label(frame,text='主治医生',bg='gray',width=10)
            lab8.place(x=2,y=370)
            self.entry6=Entry(frame,textvariable=self.try6,width=27)
            self.entry6.place(x=90,y=70)
            self.entry7=Entry(frame,textvariable=self.try7,width=27)
            self.entry7.place(x=90,y=120)
            self.entry8=Entry(frame,textvariable=self.try8,width=27)
            self.entry8.place(x=90,y=170)
            self.entry9=Entry(frame,textvariable=self.try9,width=27)
            self.entry9.place(x=90,y=220)
            self.entry10=Entry(frame,textvariable=self.try10,width=27)
            self.entry10.place(x=90,y=270)
            self.entry11=Entry(frame,textvariable=self.try11,width=27)
            self.entry11.place(x=90,y=320)
            self.entry12=Entry(frame,textvariable=self.try12,width=27)
            self.entry12.place(x=90,y=370)
            btn1=Button(frame,text='确   定',width=10,command=self.add_success1)
            btn1.place(x=120,y=430)
        elif value=='医生':
            lab_left=Label(self.frame2,image=bm_left,width=220)
            lab_left.bm=bm_left
            lab_left.place(x=0,y=0)
            lab_right=Label(self.frame2,image=bm_right,width=220)
            lab_right.bm=bm_right
            lab_right.place(x=560,y=0)
            frame_fresh = Frame(self.frame2,bg='gray')
            frame_fresh.place(x=240, y=5, width=310, height=500)
            title=self.comb1.get()
            title=title+'添加界面'
            lab1=Label(frame_fresh,text='{}'.format(title),bg='gray')
            lab1.place(x=115,y=20)
            lab2=Label(frame_fresh,text='姓  名',bg='gray',width=10)
            lab2.place(x=2,y=70)
            lab3=Label(frame_fresh,text='性  别',bg='gray',width=10)
            lab3.place(x=2,y=120)
            lab4=Label(frame_fresh,text='年  龄',bg='gray',width=10)
            lab4.place(x=2,y=170)
            lab5=Label(frame_fresh,text='类  别',bg='gray',width=10)
            lab5.place(x=2,y=220)
            lab6=Label(frame_fresh,text='电  话',bg='gray',width=10)
            lab6.place(x=2,y=270)
            lab7=Label(frame_fresh,text='科  室',bg='gray',width=10)
            lab7.place(x=2,y=320)
            lab8=Label(frame_fresh,text='职  务',bg='gray',width=10)
            lab8.place(x=2,y=370)
            self.entry6=Entry(frame_fresh,textvariable=self.try6,width=27)
            self.entry6.place(x=90,y=70)
            self.entry7=Entry(frame_fresh,textvariable=self.try7,width=27)
            self.entry7.place(x=90,y=120)
            self.entry8=Entry(frame_fresh,textvariable=self.try8,width=27)
            self.entry8.place(x=90,y=170)
            self.entry9=Entry(frame_fresh,textvariable=self.try9,width=27)
            self.entry9.place(x=90,y=220)
            self.entry10=Entry(frame_fresh,textvariable=self.try10,width=27)
            self.entry10.place(x=90,y=270)
            self.entry11=Entry(frame_fresh,textvariable=self.try11,width=27)
            self.entry11.place(x=90,y=320)
            self.entry12=Entry(frame_fresh,textvariable=self.try12,width=27)
            self.entry12.place(x=90,y=370)
            btn1=Button(frame_fresh,text='确   定',width=10,command=self.add_success2)
            btn1.place(x=120,y=430)  
        else :
            warning.warn("请正确选择类型").invalid_user()
    def add_success1(self):              #病例添加信息
        a2=self.entry6.get()
        a3=self.entry7.get()
        a4=self.entry8.get()
        a5=self.entry9.get()
        a6=self.entry10.get()
        a7=self.entry11.get()
        a8=self.entry12.get()
        idd=self.add_patient_id()
        if ((a3!='男') & (a3!='女')):
            warning.warn('性别填写有误！！！').invalid_user()
        elif int(a4)>100:
            warning.warn('年龄填写有误！！！').invalid_user()
        elif int(a4)<=0:
            warning.warn('年龄填写有误！！！').invalid_user()
        elif len(a6)>11:
            warning.warn('电话填写不规范！！！').invalid_user()
        elif self.comb1.get()!=a5:
            warning.warn('类别与所选不符！！！').invalid_user()
        else :
            linksql.SQL().add_patient(idd,a2,a3,a4,a5,a6,a7,a8)
            linksql.SQL().add_patient_vice(a2,'123456',idd)
            s='用户名：'+idd+'\n'+'密码：123456'
            with open('F:/{}.txt'.format(a2),'a',encoding='utf-8') as file:
                file.write(s)
            me.showinfo('success','添加成功！！！')
            self.frame2.after(2,self.add_interface)
    def add_success2(self):             #医生添加信息
        a2=self.entry6.get()
        a3=self.entry7.get()
        a4=self.entry8.get()
        a5=self.entry9.get()
        a6=self.entry10.get()
        a7=self.entry11.get()
        a8=self.entry12.get()
        idd=self.add_doctor_id()
        if ((a3!='男') & (a3!='女')):
            warning.warn('性别填写有误！！！').invalid_user()
        elif int(a4)>100:
            warning.warn('年龄填写有误！！！').invalid_user()
        elif int(a4)<=0:
            warning.warn('年龄填写有误！！！').invalid_user()
        elif len(a6)>11:
            warning.warn('电话填写不规范！！！').invalid_user()
        elif self.comb1.get()!=a5:
            warning.warn('类别与所选不符！！！').invalid_user()
        else :
            linksql.SQL().add_doctor(idd,a2,a3,a4,a5,a6,a7,a8)
            linksql.SQL().add_doctor_vice(a2,'123456',a5,a7,idd)
            s='用户名：'+idd+'\n'+'密码：123456'
            with open('F:/{}.txt'.format(a2),'a',encoding='utf-8') as file:
                file.write(s)
            me.showinfo('success','添加成功！！！')
            self.frame2.after(2,self.add_interface)
    def add_doctor_id(self):          #医生自动获取ID号
        a1=self.entry11.get()
        result=linksql.SQL().search_all_doctor2(a1)
        num=len(result)
        while 1:
            if num==0:
                num=1
                break
        change1=int(result[num-1][0][4:8])+1
        change2=str(change1)
        while 1:
            if len(change2)<4:
                change2='0'+change2
            elif len(change2)==4:
                break
        new_id=result[num-1][0][0:4]+str(change2)
        return new_id
    def add_patient_id(self):        #病人自动获取ID号
        a1=self.entry11.get()
        result=linksql.SQL().search_all_patient2(a1)
        num=len(result)
        while 1:
            if num==0:
                num=1

                break
            else:
                break
        change1=int(result[num-1][0][4:10])+1
        change2=str(change1)
        while 1:
            if len(change2)<6:
                change2='0'+change2
            elif len(change2)==6:
                break
        new_id=result[num-1][0][0:4]+str(change2)
        return new_id
    def update_interface(self):                                             #管理员修改界面
        cv=Canvas(self.win,bg="gray",width=820,height=605)
        cv.place(x=130,y=3)
        cv1=Canvas(self.win,bg="gray",width=810,height=50)
        cv1.place(x=135,y=8)
        lab1=Label(cv1,text='请输入修改人的ID号',bg='gray',width=15)
        lab1.place(x=25,y=15)
        self.try20=StringVar()
        self.entry20=Entry(cv1,textvariable=self.try20)
        self.entry20.place(x=150,y=15)
        btn1=Button(cv1,text='开始检索',command=self.update_interface_list)
        btn1.place(x=350,y=12)
    def update_interface_list(self):
        value=self.entry20.get()
        num=len(value)
        cv1=Canvas(self.win,bg="pink",width=810,height=540)
        cv1.place(x=135,y=61)
        frame = Frame(cv1,bg='white')
        frame.place(x=5, y=5, width=804, height=530)
        if (num!=8) & (num!=10):
            warning.warn('该ID号不符合规范！！！').invalid_user()
        else :
            bm_right=PhotoImage(file='imgs/right.png')
            bm_left=PhotoImage(file='imgs/left.png')
            self.try21=StringVar()
            self.try22=StringVar()
            self.try23=StringVar()
            self.try24=StringVar()
            self.try25=StringVar()
            self.try26=StringVar()
            self.try27=StringVar()
            if num==8:
                result=linksql.SQL().search_one_doctor2(value)
                if len(result)==0:
                    warning.warn('该用户不存在！！！').invalid_user()
                elif len(result)!=0:
                    lab_left=Label(frame,image=bm_left,width=220)
                    lab_left.bm=bm_left
                    lab_left.place(x=0,y=0)
                    lab_right=Label(frame,image=bm_right,width=220)
                    lab_right.bm=bm_right
                    lab_right.place(x=560,y=0)
                    frame_fresh = Frame(frame,bg='gray')
                    frame_fresh.place(x=240, y=5, width=310, height=500)
                    lab1=Label(frame_fresh,text='医生修改界面',bg='gray')
                    lab1.place(x=115,y=20)
                    lab2=Label(frame_fresh,text='姓  名',bg='gray',width=10)
                    lab2.place(x=2,y=70)
                    lab3=Label(frame_fresh,text='性  别',bg='gray',width=10)
                    lab3.place(x=2,y=120)
                    lab4=Label(frame_fresh,text='年  龄',bg='gray',width=10)
                    lab4.place(x=2,y=170)
                    lab5=Label(frame_fresh,text='类  别',bg='gray',width=10)
                    lab5.place(x=2,y=220)
                    lab6=Label(frame_fresh,text='电  话',bg='gray',width=10)
                    lab6.place(x=2,y=270)
                    lab7=Label(frame_fresh,text='科  室',bg='gray',width=10)
                    lab7.place(x=2,y=320)
                    lab8=Label(frame_fresh,text='职  务',bg='gray',width=10)
                    lab8.place(x=2,y=370)
                    self.entry21=Entry(frame_fresh,textvariable=self.try21,width=27)
                    self.entry21.place(x=90,y=70)
                    self.entry22=Entry(frame_fresh,textvariable=self.try22,width=27)
                    self.entry22.place(x=90,y=120)
                    self.entry23=Entry(frame_fresh,textvariable=self.try23,width=27)
                    self.entry23.place(x=90,y=170)
                    self.entry24=Entry(frame_fresh,textvariable=self.try24,width=27)
                    self.entry24.place(x=90,y=220)
                    self.entry25=Entry(frame_fresh,textvariable=self.try25,width=27)
                    self.entry25.place(x=90,y=270)
                    self.entry26=Entry(frame_fresh,textvariable=self.try26,width=27)
                    self.entry26.place(x=90,y=320)
                    self.entry27=Entry(frame_fresh,textvariable=self.try27,width=27)
                    self.entry27.place(x=90,y=370)
                    btn1=Button(frame_fresh,text='确   定',width=10,command=self.update_success1)
                    btn1.place(x=120,y=430) 
            elif num==10:
                result=linksql.SQL().search_one_patient2(value)
                if len(result)==0:
                    warning.warn('该用户不存在！！！').invalid_user()
                elif len(result)!=0:
                    lab_left=Label(frame,image=bm_left,width=220)
                    lab_left.bm=bm_left
                    lab_left.place(x=0,y=0)
                    lab_right=Label(frame,image=bm_right,width=220)
                    lab_right.bm=bm_right
                    lab_right.place(x=560,y=0)
                    frame_fresh = Frame(frame,bg='gray')
                    frame_fresh.place(x=240, y=5, width=310, height=500)
                    lab1=Label(frame_fresh,text='医生修改界面',bg='gray')
                    lab1.place(x=115,y=20)
                    lab2=Label(frame_fresh,text='姓  名',bg='gray',width=10)
                    lab2.place(x=2,y=70)
                    lab3=Label(frame_fresh,text='性  别',bg='gray',width=10)
                    lab3.place(x=2,y=120)
                    lab4=Label(frame_fresh,text='年  龄',bg='gray',width=10)
                    lab4.place(x=2,y=170)
                    lab5=Label(frame_fresh,text='电  话',bg='gray',width=10)
                    lab5.place(x=2,y=220)
                    lab6=Label(frame_fresh,text='类  别',bg='gray',width=10)
                    lab6.place(x=2,y=270)
                    lab7=Label(frame_fresh,text='科  室',bg='gray',width=10)
                    lab7.place(x=2,y=320)
                    lab8=Label(frame_fresh,text='主治医师',bg='gray',width=10)
                    lab8.place(x=2,y=370)
                    self.entry21=Entry(frame_fresh,textvariable=self.try21,width=27)
                    self.entry21.place(x=90,y=70)
                    self.entry22=Entry(frame_fresh,textvariable=self.try22,width=27)
                    self.entry22.place(x=90,y=120)
                    self.entry23=Entry(frame_fresh,textvariable=self.try23,width=27)
                    self.entry23.place(x=90,y=170)
                    self.entry24=Entry(frame_fresh,textvariable=self.try24,width=27)
                    self.entry24.place(x=90,y=220)
                    self.entry25=Entry(frame_fresh,textvariable=self.try25,width=27)
                    self.entry25.place(x=90,y=270)
                    self.entry26=Entry(frame_fresh,textvariable=self.try26,width=27)
                    self.entry26.place(x=90,y=320)
                    self.entry27=Entry(frame_fresh,textvariable=self.try27,width=27)
                    self.entry27.place(x=90,y=370)
                    btn1=Button(frame_fresh,text='确   定',width=10,command=self.update_success2)
                    btn1.place(x=120,y=430) 
    def update_success1(self):           #医生修改界面
        a21=self.entry21.get()
        a22=self.entry22.get()
        a23=self.entry23.get()
        a24=self.entry24.get()
        # a25=self.entry25.get()
        a26=self.entry26.get()
        a27=self.entry27.get()
        idd=self.entry20.get()
        if ((a22!='男') & (a22!='女')&(len(a23)==0)):
            warning.warn('性别填写有误！！！').invalid_user()
        elif int(a23)>100:
            warning.warn('年龄填写有误！！！').invalid_user()
        elif int(a23)<=0:
            warning.warn('年龄填写有误！！！').invalid_user()
        elif len(a24)>11:
            warning.warn('电话填写不规范！！！').invalid_user()
        else :
            if len(a21)!=0:
                linksql.SQL().update_doctor_name(a21,idd)
            elif len(a22)!=0:
                linksql.SQL().update_doctor_sex(a22,idd)
            elif len(a23)!=0:
                linksql.SQL().update_doctor_age(a23,idd)
            elif len(a24)!=0:
                linksql.SQL().update_doctor_tel(a24,idd)
            elif len(a26)!=0:
                linksql.SQL().update_doctor_duty(a26,idd)
            elif len(a27)!=0:
                linksql.SQL().update_doctor_depart(a27,idd)
            me.showinfo('success','修改成功！')
    def update_success2(self):           #病人修改界面
        a21=self.entry21.get()
        a22=self.entry22.get()
        a23=self.entry23.get()
        a24=self.entry24.get()
        # a25=self.entry25.get()
        a26=self.entry26.get()
        a27=self.entry27.get()
        idd=self.entry20.get()
        if ((a22!='男') & (a22!='女')&(len(a23)==0)):
            warning.warn('性别填写有误！！！').invalid_user()
        elif int(a23)>100:
            warning.warn('年龄填写有误！！！').invalid_user()
        elif int(a23)<=0:
            warning.warn('年龄填写有误！！！').invalid_user()
        elif len(a24)>11:
            warning.warn('电话填写不规范！！！').invalid_user()
        else :
            if len(a21)!=0:
                linksql.SQL().update_patient_name(a21,idd)
            elif len(a22)!=0:
                linksql.SQL().update_patient_sex(a22,idd)
            elif len(a23)!=0:
                linksql.SQL().update_patient_age(a23,idd)
            elif len(a24)!=0:
                linksql.SQL().update_patient_tel(a24,idd)
            elif len(a26)!=0:
                linksql.SQL().update_patient_depart(a26,idd)
            elif len(a27)!=0:
                linksql.SQL().update_patient_doctor(a27,idd)
            me.showinfo('success','修改成功！')
    def delete_interface(self):
        cv=Canvas(self.win,bg="gray",width=820,height=605)
        cv.place(x=130,y=3)
        cv1=Canvas(self.win,bg="gray",width=810,height=50)
        cv1.place(x=135,y=8)
        lab1=Label(cv1,text='请输入要删除的ID号',bg='gray',width=15)
        lab1.place(x=25,y=15)
        self.try30=StringVar()
        self.entry30=Entry(cv1,textvariable=self.try30)
        self.entry30.place(x=150,y=15)
        btn1=Button(cv1,text='确定',command=self.delete_interface_list)
        btn1.place(x=350,y=12)
    def delete_interface_list(self):
        result=self.entry30.get()
        if len(result)==8:
            linksql.SQL().delete_doctor(result)
            linksql.SQL().delete_doctor1(result)
            me.showinfo('success','删除成功！')
        elif len(result)==10:
            linksql.SQL().delete_patient(result)
            linksql.SQL().delete_patient1(result)
            me.showinfo('success','删除成功！')



        
