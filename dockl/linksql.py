import pymysql
 
class SQL:
    def __init__(self):               
        self.db = pymysql.connect("localhost","root","971104","ab_sql" )

    def list_login_manager(self):                  #管理员登录校验表
        cursor = self.db.cursor()
        sql = "SELECT * FROM login_manager"
        cursor.execute(sql)
        result =cursor.fetchall()
        return result
    def list_login_doctor(self):               #医生登录校验表
        cursor = self.db.cursor()
        sql = "SELECT * FROM login_doctor"
        cursor.execute(sql)
        result =cursor.fetchall()
        return result
    def list_login_patient(self):           #病人登录校验表
        cursor = self.db.cursor()
        sql = "SELECT * FROM login_patient"
        cursor.execute(sql)
        result =cursor.fetchall()
        return result
    def search_one_doctor1(self,name):           #从login_doctor中使用名字搜索一个医生信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM login_doctor WHERE name='{}' ".format(name)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_one_doctor2(self,idd):           #从site_doctor中使用id搜索一个医生信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_doctor WHERE id='{}' ".format(idd)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_one_doctor22(self,idd,ks):           #从site_doctor中使用id、ks搜索一个医生信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_doctor WHERE id='{}' AND ks='{}' ".format(idd,ks)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_all_doctor(self):                #从site_doctor中搜索所有医生详细信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_doctor "
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_all_doctorr(self,ks):                #从site_doctor中搜索科室所有医生详细信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_doctor WHERE ks='{}'".format(ks)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_all_doctor1(self,name):       #从site_doctor中使用姓名得出一个医生信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_doctor WHERE name='{}' ".format(name)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_all_doctor11(self,name,ks):       #从site_doctor中使用姓名,ks得出一个医生信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_doctor WHERE name='{}' AND ks='{}' ".format(name,ks)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_all_doctor2(self,ks):       #从site_doctor中使用科室得出一个医生信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_doctor WHERE ks='{}' ".format(ks)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_all_doctor_id(self,idd):       #从site_doctor中使用id得出一个医生信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_doctor WHERE id='{}' ".format(idd)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_all_doctor3(self,name,ks):       #从site_doctor中使用科室、姓名得出一个医生信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_doctor WHERE ks='{}' AND name='{}' ".format(ks,name)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_one_patient1(self,name):           #从login_patient中使用名字搜索一个病人信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM login_patient WHERE name='{}' ".format(name)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_one_patient2(self,id):           #从site_patient中使用id搜索一个病人信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_patient WHERE id='{}' ".format(id)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_one_patient22(self,id,ks):           #从site_patient中使用id,ks搜索一个病人信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_patient WHERE id='{}' AND ks='{}' ".format(id,ks)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def serach_all_patient(self):            #从site_patient中搜索所有病人详细信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_patient"
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def serach_all_patientt(self,ks):            #从site_patient中搜索科室所有病人详细信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_patient WHERE ks='{}'".format(ks)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_all_patient1(self,name):       #从site_doctor中使用姓名得出一个病人信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_patient WHERE name='{}' ".format(name)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_all_patient11(self,name,ks):       #从site_doctor中使用姓名,ks得出一个病人信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_patient WHERE name='{}' AND ks='{}' ".format(name,ks)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_all_patient2(self,ks):       #从site_doctor中使用科室得出一个医生信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_patient WHERE ks='{}' ".format(ks)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def search_all_patient3(self,name,ks):       #从site_doctor中使用科室、姓名得出一个医生信息
        cursor = self.db.cursor()
        sql = "SELECT * FROM site_patient WHERE ks='{}' AND name='{}' ".format(ks,name)
        cursor.execute(sql)
        results = cursor.fetchall()
        return results
    def add_patient(self,idd,name,sex,age,stye,cont,ks,doname):      #添加病例
        cursor = self.db.cursor()
        sql='insert into site_patient(id,name,sex,age,stye,cont,ks,doname)value("%s","%s","%s","%s","%s","%s","%s","%s")'%(idd,name,sex,age,stye,cont,ks,doname)
        cursor.execute(sql)
        self.db.commit()
    def add_patient_vice(self,name,password,idd):               #在login_patient中添加登录校验
        cursor = self.db.cursor()
        sql='insert into login_patient(name,password,id)value("%s","%s","%s")'%(name,password,idd)
        cursor.execute(sql)
        self.db.commit()
    # def add_patient_vices(self):
    #     cursor = self.db.cursor()
    #     sql=''
    def add_doctor(self,idd,name,sex,age,stye,cont,ks,duty):      #添加医生
        cursor = self.db.cursor()
        sql='insert into site_doctor(id,name,sex,age,stye,cont,ks,duty)value("%s","%s","%s","%s","%s","%s","%s","%s")'%(idd,name,sex,age,stye,cont,ks,duty)
        cursor.execute(sql)
        self.db.commit()
    def add_doctor_vice(self,name,password,stye,ks,idd):               #在login_doctor中添加登录校验
        cursor = self.db.cursor()
        sql='insert into login_doctor(name,password,stye,ks,id)value("%s","%s","%s","%s","%s")'%(name,password,stye,ks,idd)
        cursor.execute(sql)
        self.db.commit()
    def update_doctor_name(self,name,idd):               #在site_doctor中修改姓名
        cursor = self.db.cursor()
        sql = "UPDATE site_doctor SET name='{}' WHERE id='{}'" .format(name,idd)
        cursor.execute(sql)
        self.db.commit()
    def update_doctor_sex(self,sex,idd):               #在site_doctor中修改性别
        cursor = self.db.cursor()
        sql = "UPDATE site_doctor SET sex='{}' WHERE id='{}'" .format(sex,idd)
        cursor.execute(sql)
        self.db.commit()
    def update_doctor_age(self,age,idd):               #在site_doctor中修改年龄
        cursor = self.db.cursor()
        sql = "UPDATE site_doctor SET age='{}' WHERE id='{}'" .format(age,idd)
        cursor.execute(sql)
        self.db.commit()
    def update_doctor_tel(self,cont,idd):               #在site_doctor中修改电话
        cursor = self.db.cursor()
        sql = "UPDATE site_doctor SET cont='{}' WHERE id='{}'" .format(cont,idd)
        cursor.execute(sql)
        self.db.commit()
    def update_doctor_duty(self,onedo,idd):               #在site_doctor中修改职务
        cursor = self.db.cursor()
        sql = "UPDATE site_doctor SET onedo='{}' WHERE id='{}'" .format(onedo,idd)
        cursor.execute(sql)
        self.db.commit()
    def update_doctor_depart(self,ks,idd):               #在site_doctor中修改科室
        cursor = self.db.cursor()
        sql = "UPDATE site_doctor SET depart='{}' WHERE id='{}'" .format(ks,idd)
        cursor.execute(sql)
        self.db.commit()

    def update_patient_name(self,name,idd):               #在site_patient中修改姓名
        cursor = self.db.cursor()
        sql = "UPDATE site_patient SET name='{}' WHERE id='{}'" .format(name,idd)
        cursor.execute(sql)
        self.db.commit()
    def update_patient_sex(self,sex,idd):               #在site_patient中修改性别
        cursor = self.db.cursor()
        sql = "UPDATE site_patient SET sex='{}' WHERE id='{}'" .format(sex,idd)
        cursor.execute(sql)
        self.db.commit()
    def update_patient_age(self,age,idd):               #在site_patient中修改年龄
        cursor = self.db.cursor()
        sql = "UPDATE site_patient SET age='{}' WHERE id='{}'" .format(age,idd)
        cursor.execute(sql)
        self.db.commit()
    def update_patient_tel(self,cont,idd):               #在site_patient中修改电话
        cursor = self.db.cursor()
        sql = "UPDATE site_patient SET cont='{}' WHERE id='{}'" .format(cont,idd)
        cursor.execute(sql)
        self.db.commit()
    def update_patient_depart(self,ks,idd):               #在site_patient中修改科室
        cursor = self.db.cursor()
        sql = "UPDATE site_patient SET depart='{}' WHERE id='{}'" .format(ks,idd)
        cursor.execute(sql)
        self.db.commit()
    def update_patient_doctor(self,doname,idd):               #在site_patient中修改主治医师
        cursor = self.db.cursor()
        sql = "UPDATE site_patient SET doname='{}' WHERE id='{}'" .format(doname,idd)
        cursor.execute(sql)
        self.db.commit()
    def update_doctor_username(self,name,idd):
        cursor = self.db.cursor()
        sql = "UPDATE login_doctor SET name='{}' WHERE id='{}'" .format(name,idd)
        cursor.execute(sql)
        self.db.commit()
    def update_doctor_passwd(self,password,idd):
        cursor = self.db.cursor()
        sql = "UPDATE login_doctor SET password='{}' WHERE id='{}'" .format(password,idd)
        cursor.execute(sql)
        self.db.commit()
    def update_patient_username(self,name,idd):
        cursor = self.db.cursor()
        sql = "UPDATE login_patient SET name='{}' WHERE id='{}'" .format(name,idd)
        cursor.execute(sql)
        self.db.commit()
    def update_patient_passwd(self,password,idd):
        cursor = self.db.cursor()
        sql = "UPDATE login_patient SET password='{}' WHERE id='{}'" .format(password,idd)
        cursor.execute(sql)
        self.db.commit()
    def delete_doctor(self,idd):
        cursor = self.db.cursor()
        sql = "DELETE login_doctor  WHERE id='{}'" .format(idd)
        cursor.execute(sql)
        self.db.commit()
    def delete_doctor1(self,idd):
        cursor = self.db.cursor()
        sql = "UPDATE site_doctor WHERE id='{}'" .format(idd)
        cursor.execute(sql)
        self.db.commit()
    def delete_patient(self,idd):
        cursor = self.db.cursor()
        sql = "DELETE login_patient  WHERE id='{}'" .format(idd)
        cursor.execute(sql)
        self.db.commit()
    def delete_patient1(self,idd):
        cursor = self.db.cursor()
        sql = "UPDATE site_patient WHERE id='{}'" .format(idd)
        cursor.execute(sql)
        self.db.commit()


        
    

