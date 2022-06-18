# by SPARSH MANNI  @sparsh_manni

import mysql.connector
import fontstyle
from tabulate import tabulate


#creating database if not exists
db = mysql.connector.connect(user='root', password='', host='localhost',database='')
cursor = db.cursor()
cursor.execute("create database if not exists school")
#creating required tables if not exists    
cursor.execute("use school")
cursor.execute('create table if not exists student(sname varchar(300),admno int(100) primary key,dob date,cls int(20),cty varchar(400)) ')
cursor.execute('create table if not exists emp(empno int(100)primary key,ename varchar(300),job varchar(100),hiredate date) ')
cursor.execute('create table if not exists fee(admno int(11) primary key,fee int(11),month varchar(15)) ')
cursor.execute('create table if not exists exam(sname varchar(30),admno int(11),per decimal(4,2),res varchar(15)) ')
db.commit()

#generating random no.
import random

randomm=(random.randint(100,500))
    

def insert1():
    sname=input("Enter Student Name : ")
    print('')
    admno=randomm
    dob=input("Enter Date of Birth(yyyy-mm-dd): ")
    print('')
    cls=input("Enter class for admission: ")
    print('')
    cty=input("Enter City : ")
    print('')
    db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
    cursor = db.cursor()
    sql="INSERT INTO student(sname,admno,dob,cls,cty) VALUES ( '%s' ,'%d','%s','%s','%s')"
    try:
        cursor.execute(sql %(sname,admno,dob,cls,cty))
        db.commit()
    except:
        db.rollback()
        db.close()
#insert1()

def display1():
    try:
        db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(tabulate(results ,headers=['Name', 'Adm.no.','Dob','Class',"City"],tablefmt="grid"))
    except:
        print ("Error: unable to fetch data")
        db.close()
#display1()

def update1():
    print("initial details are -")
    display1()
    try:
        db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            sname = c[0]
            admno= c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
    except:
        print ("Error: unable to fetch data")
    print()
    tempst=int(input("Enter Admission No : "))
    temp=input("Enter new class : ")
    temp1=input("Enter new name : ")
    temp2=input("Enter new dob : ")
    temp3=input("Enter new city : ")
    try:
        sql = "Update student set cls='%s' where admno='%d'" % (temp,tempst)
        sql1 = "Update student set sname='%s' where admno='%d'" % (temp1,tempst)
        sql2 = "Update student set dob='%s' where admno='%d'" % (temp2,tempst)
        sql3 = "Update student set cty='%s' where admno='%d'" % (temp3,tempst)
        
        cursor.execute(sql)
        cursor.execute(sql1)
        cursor.execute(sql2)
        cursor.execute(sql3)
        db.commit()
    except Exception as e:
        print (e)
        db.close()
#update()

def delete1():
    display1()
    try:
        db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            sname = c[0]
            admno= c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
    except:
        print ("Error: unable to fetch data")
    temp=int(input("\nEnter adm no to be deleted : "))
    try:
        sql = "delete from student where admno='%d'" % (temp)
        ans=input("Are you sure you want to delete the record(y/n) : ")
        if ans=='y' or ans=='Y':
            cursor.execute(sql)
            db.commit()
    except Exception as e:
        print (e)
        db.close()
#delete()


#random no,            
randomm22=(random.randint(1000,2000))
def insert2():
    empno=randomm22
    ename=input("Enter Employee Name : ")
    job=input("Enter Designation: ")
    hiredate=input("Enter date of joining: ")
    db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
    cursor = db.cursor()
    sql="INSERT INTO emp(empno,ename,job,hiredate) VALUES ( '%d' ,'%s','%s','%s')"
    try:
        cursor.execute(sql %(empno,ename,job,hiredate))
        db.commit()
    except:
        db.rollback()
        db.close()

def display2():
        db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
        cursor = db.cursor()
        sql = "select *from emp"
        cursor.execute(sql)
        results = cursor.fetchall()
      
        print(tabulate(results ,headers=['EMP NO.', 'EMP NAME','JOB','HIREDATE'],tablefmt="grid"))


def update2():
    print("initial details are -")
    display2()
    
    

    try:
        
        
        db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
        cursor = db.cursor()
        sql = "SELECT * FROM emp"
        cursor.execute(sql)
        results = cursor.fetchall()
        for c in results:
            empno=c[0]
            ename=c[1]
            job=c[2]
            hiredate=c[3]
    except:
        print ("Error: unable to fetch data")
        print()
        
    tempst=int(input("Enter Employee No : "))
    temp=input("Enter new designation : ")
    temp1=input("Enter new name : ")
    temp2=input("Enter new hiredate : ")
        
    try:
            sql = "Update emp set job='%s' where empno='%d'" %(temp,tempst)
            sql1 = "Update emp set ename='%s' where empno='%d'" %(temp1,tempst)
            sql2 = "Update emp set hiredate='%s' where empno='%d'" %(temp2,tempst)
            cursor.execute(sql)
            cursor.execute(sql1)
            cursor.execute(sql2)
            db.commit()
    except Exception as e:
            print (e)
            db.close()


def delete2():
    
        display2()
    
        try:
                db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
                cursor = db.cursor()
                sql = "SELECT * FROM emp"
                cursor.execute(sql)
                results = cursor.fetchall()
                for c in results:
                        empno = c[0]
                        ename= c[1]
                        job=c[2]
                        hiredate=c[3]
                        print(c)
        except:
                print ("Error: unable to fetch data")
        temp=int(input("\nEnter emp no to be deleted : "))
        try:
                sql = "delete from emp where empno='%d'" %(temp)
                ans=input("Are you sure you want to delete the record(y/n) : ")
                if ans=='y' or ans=='Y':
                        cursor.execute(sql)
                        db.commit()
        except Exception as e:
                                print (e)
                                db.close()

def insert3():
        db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        print(tabulate(results ,headers=['Name', 'Adm.no.','Dob','Class',"City"],tablefmt="grid"))
        for c in results:
            sname = c[0]
            admno= c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
            
            if cls<5:
                fees=1000
            elif cls>5 and cls<10:
                fees=2000
            elif cls>10:
                fees=3000
        admno=int(input("Enter adm no: "))
        fee=fees
        month=input("Enter the Month till fees is DEPOSITED : ")
        

        db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
        cursor = db.cursor()
        sql="INSERT INTO fee(admno,fee,month) VALUES ( '%d','%d','%s')"%(admno,fee,month)
        try:
                cursor.execute(sql)
                db.commit()
        except:
                db.rollback()
                db.close()

def update3():
        try:
                db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
                cursor = db.cursor()
                sql = "SELECT * FROM fee"
                cursor.execute(sql)
                results = cursor.fetchall()
                for c in results:
                        admno= c[0]
                        fee=c[1]
                        month=c[2]
                print(tabulate(results ,headers=['Adm.no.', 'Fee(Per Month)','Month'],tablefmt="grid"))
        except:
                print ("Error: unable to fetch data")
        print()
        tempst=int(input("Enter Admission No : "))
        temp=input("Enter new month : ")
        try:
                sql = "Update fee set month='%s'  where admno='%d'" % (temp,tempst)
                cursor.execute(sql)
                db.commit()
        except Exception as e:
                        print (e)
                        db.close()

def delete3():
        try:
                db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
                cursor = db.cursor()
                sql = "SELECT * FROM fee"
                cursor.execute(sql)
                results = cursor.fetchall()
                for c in results:
                        admno= c[0]
                        fee=c[1]
                        month=c[2]
                print(tabulate(results ,headers=['Adm.no.', 'Fee(Per Month)','Month'],tablefmt="grid"))

        except:
                print ("Error: unable to fetch data")
        temp=int(input("\nEnter adm no to be deleted : "))
        try:
                sql = "delete from fee where admno='%d'" % (temp)
                ans=input("Are you sure you want to delete the record(y/n) : ")
                if ans=='y' or ans=='Y':
                        cursor.execute(sql)
                        db.commit()
        except Exception as e:
                print (e)
                db.close()

def insert4():
        db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
        cursor = db.cursor()
        sql = "SELECT * FROM student"
        cursor.execute(sql)
        results = cursor.fetchall()
        print("|   NAME   | ADM. NO. |   DOB  |   CLASS   |  CITY  |")
        print("--------------------------------------------------")
        for c in results:
            sname = c[0]
            admno= c[1]
            dob=c[2]
            cls=c[3]
            cty=c[4]
            print("|%s ,  %d  ,  %s  ,  %s  ,  %s  )" % (sname,admno,dob,cls,cty))
        sname=input("Enter Student Name : ")
        admno=int(input("Enter Admission No : "))
        per=float(input("Enter percentage : "))
        res=input("Enter result: ")
        db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
        cursor = db.cursor()
        sql="INSERT INTO exam(sname,admno,per,res) VALUES ( '%s' ,'%d','%s','%s')"%(sname,admno,per,res)
        try:
                cursor.execute(sql)
                db.commit()
        except:
                db.rollback()
                db.close()
                
def display4():
        try:
                db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
                cursor = db.cursor()
                sql = "SELECT * FROM exam"
                cursor.execute(sql)
                results = cursor.fetchall()
                for c in results:
                        sname = c[0]
                        admno= c[1]
                        per=c[2]
                        res=c[3]
                        print ("(%s,%d,%d,%d)"%(sname,admno,per,res) )
                        print(tabulate(results, headers=['sname', 'admno','per','res'], tablefmt=''))
        except:
                print ("Error: unable to fetch data")
                db.close()

def update4():
        try:
                db = mysql.connector.connect(user='root', password='', host='',database='school')
                cursor = db.cursor()
                sql = "SELECT * FROM exam"
                cursor.execute(sql)
                results = cursor.fetchall()
                for c in results:
                        sname = c[0]
                        admno= c[1]
                        per=c[2]
                        res=c[3]
        except:
                print ("Error: unable to fetch data")
                print()
        tempst=int(input("Enter Admission No : "))
        temp=input("Enter new result : ")
        try:
                sql = "Update exam set res='%s' where admno='%d'" %(temp,tempst)
                cursor.execute(sql)
                db.commit()
        except Exception as e:
                print (e)
                db.close()





def selection():
    db = mysql.connector.connect(user='root', password='', host='localhost',database='school')
    cursor = db.cursor()
    text = fontstyle.apply("WELCOME TO SCHOOL MANAGEMENT SYSTEM", "RED")
    print('::::::::::::::::::::::::::::::::::::::')
    print("______________________________________")
    print('\n WELCOME TO SCHOOL MANAGEMENT SYSTEM \n______________________________________')
    print("::::::::::::::::::::::::::::::::::::::")
    print("")
    print("1. STUDENT MANAGEMENT")
    print("2. EMPLOYEE MANAGEMENT")
    print("3. FEE MANAGEMENT")
    print("4. EXAM MANAGEMENT")
  
    ch=int(input("\nENTER YOUR CHOICE (1-4) : "))
    if ch==1:
        print('\nWELCOME TO STUDENT MANAGEMENT SYSTEM')
        print("______________________________________")
        print('a.NEW ADMISSION ')
        print('b.UPDATE STUDENT DETAILS')
        print('c.ISSUE TC')
        print('d.SEE ALL STUDENTS\n')       
        c=input("Enter ur choice (a-c) : ")
        if c=='a':
            insert1()
        elif c=='b':
            update1()
        elif c=='c':
            delete1()
        elif c=='d':
                display1()
    elif ch==2:
        print('WELCOME TO EMPLOYEE MANAGEMENT SYSTEM')
        print("______________________________________")
        print('a.NEW EMPLOYEE')
        print('b.UPDATE STAFF DETAILS')
        print('c.DELETE EMPLOYEE')
        print("d.DISPLAY ALL EMPLOYEES \n")
        c=input("Enter ur choice : ")           
        if c=='a':
                insert2()

                
                
        elif c=='b':
                update2()
                
        elif c=='c':
                delete2()
        elif c=='d':
            display2()
    elif ch==3:
            print('WELCOME TO FEE MANAGEMENT SYSTEM')
            print("______________________________________")
            print('a.NEW FEE')
            print('b.UPDATE FEE')
            print('c.EXEMPT FEE')
            c=input("Enter ur choice : ")
            if c=='a':
                    insert3()
            elif c=='b':
                    update3()
            elif c=='c':
                    delete3()
            else:
                    print('Enter correct choice...!!')
    
    elif ch==4:
            print('WELCOME TO EXAM MANAGEMENT SYSTEM')
            print("______________________________________")
            print('a.EXAM DETAILS')
            print('b.UPDATE DETAILS ')
            print('c.DELETE DETAILS')
            c=input("Enter ur choice : ")
            if c=='a':
                    insert4()
            elif c=='b':
                    update4()
            elif c=='c':
                    display4()
            elif c=='d':
                delete4()
                
        
    else:
            print('Enter correct choice..!!')

selection()
t=input("DO YOU WANT TO RUN PROGRAM AGAIN ??(y/n)")
while t=="y" or t=="Y":
        selection()

        

        
