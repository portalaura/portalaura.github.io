import os
import platform
import mysql.connector

mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="sms",charset="utf8")
mycursor=mydb.cursor()

#MODULE FOR NEW ADMISSION
def newStudent():
    createTable	="""CREATE	TABLE	IF	NOT	EXISTS	STUDENT(SROLL_NO	VARCHAR(5),SNAME VARCHAR(30),FNAME VARCHAR(30),MNAME VARCHAR(30) ,PHONE	VARCHAR(12),	ADDRESS	VARCHAR(100),SCLASS VARCHAR(5),SSECTION VARCHAR(5), SADMISSION_NO    VARCHAR(10) PRIMARY KEY)"""
    mycursor.execute(createTable)
    sroll_no=input(" ENTER ROLL_NO : ")
    sname=input("\n ENTER STUDENT'S NAME : ")
    fname=input(" ENTER FATHER'S NAME : ")
    mname=input(" ENTER MOTHER'S NAME : ")
    phone=input(" ENTER CONTACT NO. : ")
    address=input(" ENTER ADDRESS : ")
    sclass =input(" ENTER CLASS : ")
    ssection=input(" ENTER SECTION : ")
    sadmission_no=input(" ENTER ADMISSION_NO   :   ")
    sql="insert into student (sroll_no,sname,fname,mname,phone,address,sclass,ssection,sadmission_no) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values=(sroll_no,sname,fname,mname,phone,address ,sclass,ssection,sadmission_no)
    mycursor.execute(sql,values)
    mycursor.execute("COMMIT")
    mycursor.close()
      

#MODULE TO DISPLAY STUDENT'S DATA
def displayStudent():
    mycursor.execute("SELECT * FROM student")
    data=mycursor.fetchall()
    print(data)
    mycursor.close()
    
#MODULE TO UPDATE STUDENT'S RECORD
def updateStudent():
    admission_no=input("ENTER ADMISSION NO :")
    sql="SELECT * FROM student WHERE sadmission_no= %s"
    mycursor.execute(sql,(admission_no,))
    data=mycursor.fetchall()
    if data:
        print("PRESS 1 FOR NAME")
        print("PRESS 2 FOR CLASS")
        print("PRESS 3 FOR ROLL NO")
        choice=int(input("Enter Your Choice"))
        if choice==1:
            name=input("ENTER NAME OF THE STUDENT  :")
            sql="UPDATE student SET sname= %s WHERE sadmission_no =%s"
            mycursor.execute(sql,(name,admission_no))
            mycursor.execute("COMMIT")
            print("NAME UPDATED")
        elif choice == 2:
            std=input("ENTER CLASS OF THE STUDENT   :")
            sql="UPDATE student SET sclass= %s WHERE sadmission_no=%s"
            mycursor.execute(sql,(std,admission_no))
            mycursor.execute("COMMIT")
            print("CLASS UPDATED")
        elif choice==3:
            roll_no=int(input("ENTER ROLL NO OF THE STUDENT  :"))
            sql="UPDATE	student	SET	sroll_no=	%s	WHERE sadmission_no = %s"
            mycursor.execute(sql,(roll_no,admission_no))
            mycursor.execute("COMMIT")
            print("ROLL NO UPDATED")
        else:
            print("Record Not Found Try Again !")
            mycursor.close()
    else:
        print("\nSomthing Went Wrong ,Please Try Again !")

#MODULE TO ENTER MARKS OF THE STUDENT
def marksStudent () :
    createTable ="""CREATE TABLE IF NOT EXISTS MARKS(SADMISSION_NO VARCHAR(10) PRIMARY KEY,HINDI INT,ENGLISH INT ,MATH INT ,SCIENCE INT,SOCIAL INT,COMPUTER INT,TOTAL INT ,AVERAGE DECIMAL)"""
    mycursor.execute(createTable)
    admission_no=input("ENTER ADMISSION NO OF THE STUDENT :")
    hindi=int(input("\n ENTER MARKS OF HINDI : "))
    english=int(input("\n ENTER MARKS OF ENGLISH : "))
    math=int(input("\n ENTER MARKS OF MATH : "))
    science=int(input("\n ENTER MARKS OF SCIENCE : "))
    social=int(input("\n ENTER MARKS OF SOCIAL : "))
    computer =int(input("\n ENTER MARKS OF COMPUTER : "))
    total = hindi + english + math + science + social + computer
    average = total/6
    sql="INSERT INTO MARKS(SADMISSION_NO,HINDI,ENGLISH,MATH,SCIENCE,SOCIAL,COMPUTER, TOTAL,AVERAGE) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    values=(admission_no,hindi,english,math,science,social,computer , total , average)
    mycursor.execute(sql,values)
    mycursor.execute("COMMIT")
    mycursor.close()
    print("\nMarks of the Student Entered Successfully !")
 
def reportCardAllStudent () :
    mycursor.execute("SELECT * FROM MARKS")
    data=mycursor.fetchall()
    print(data)
    mycursor.close()
    
#MODULE TO GENERATE REPORT CARD OF ONE STUDENTS
def reportCardOneStudent():
    admission_no=input("ENTER ADMISSION NO OF THE STUDENT :")
  
    sql="SELECT * FROM MARKS WHERE SADMISSION_NO= %s"
    mycursor.execute(sql,(admission_no,))
    data=mycursor.fetchall()
    if data:
        print(data)
    else:
        print("Record Not Found , Please Try Again !")
        mycursor.close()

    
def helpMe():
    print("Please, Visit The Offcial Website Of Vidyalaya To Download The Mannual !!!")

print("############################################################# #######")
while(1):
    print("|	Enter 1 -  Add Student		                                        |")
    print("|	Enter 2 -  Display Student's Data.					|")
    print("|	Enter 3 -  Update Students's Data .					|")
    print("|	Enter 4 -  Add Student's Marks Detail.					|")
    print("|	Enter 5 - Generate All Student's Report Card.                           |")
    print("|	Enter 6 - Generate Student Wise Report Card.                            |")
    print("|	Enter 7-  Exit.	                                                        |")
    print("|	Enter 0(ZERO) - Help.	                                                |")
    choice=int(input("PLEASE  ENTER  YOUR  CHOICE  :	"))
    if choice==1:
        newStudent()
    elif choice==2:
        displayStudent()
    elif choice==3:
        updateStudent()
    elif choice==4:
        marksStudent()
    elif choice==5:
        reportCardAllStudent()
    elif choice==6:
        reportCardOneStudent()
    elif choice==7:
        quit()
    elif choice==0:
        helpMe()
    else:
        print("Sorry ,May Be You Are Giving Me Wrong Input, Please Try Again !!! ")
