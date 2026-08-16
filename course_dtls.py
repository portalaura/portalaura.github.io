import os
import platform
import mysql.connector 
import pandas as pd 

# 1. Database Connection
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="COURSE_MATCH"
)
mycursor = mydb.cursor()

# ==========================================
# NEW BLOCK: INITIAL TABLE CREATION
# ==========================================
def setup_database():
    """Creates the course_details table initially if it doesn't exist."""
    try:
        sql = """
        CREATE TABLE IF NOT EXISTS course_details (
            c_id INT PRIMARY KEY,
            stream VARCHAR(100),
            c_name VARCHAR(255)
        )
        """
        mycursor.execute(sql)
        mydb.commit()
    except mysql.connector.Error as err:
        print(f"Error creating table: {err}")
# ==========================================

def course_Insert():
    L = [] 
    c_id = int(input("Enter the course id : ")) 
    L.append(c_id)
    stream = input("Enter The Stream Name: ")
    L.append(stream)
    c_name = input("Enter available opportunities or courses in this stream : ") 
    L.append(c_name)
    
    course = L 
    sql = "insert into course_details (c_id, stream, c_name) values (%s,%s,%s)" 
    mycursor.execute(sql, course) 
    mydb.commit()
    print("Course added successfully!")
 
def cView(): 
    print("\nSelect the search criteria : ") 
    print("1. c_id") 
    print("2. Stream") 
    print("3. All") 
    ch = int(input("Enter the choice : ")) 
    
    if ch == 1:
        s = int(input("c_id : "))
        c = (s,)
        sql = "select * from course_details where c_id=%s"
        mycursor.execute(sql, c)
    elif ch == 2:
        s = input("Enter stream Name : ")
        n = (s,)
        sql = "select * from course_details where stream=%s"
        mycursor.execute(sql, n) 
    elif ch == 3:
        sql = "select * from course_details"
        mycursor.execute(sql)
    else:
        print("Invalid choice.")
        return

    res = mycursor.fetchall()
    print("\nThe course details are as follows : ")
    print(f"{'Course_ID':<12} | {'Stream_Name':<20} | {'Course_opportunities'}")
    print("-" * 65)
    for x in res:
        print(f"{x[0]:<12} | {x[1]:<20} | {x[2]}")
    
def removecourse():
    c_id = int(input("Enter the course_id of the course to be deleted : "))
    ci = (c_id,)
    sql = "Delete from course_details where c_id=%s"
    mycursor.execute(sql, ci) 
    mydb.commit()
    
    if mycursor.rowcount > 0:
        print("Course removed successfully!")
    else:
        print("No course found with that ID.")

def MenuSet(): 
    print("\n--- COURSE MATCH MENU ---")
    print("Enter 1 : To Add course")
    print("Enter 2 : To View course ")
    print("Enter 3 : To Remove course")
    try: 
        userInput = int(input("Please Select An Above Option: ")) 
    except ValueError:
        print("\nHey! That's Not A Number") 
        return False  
    else:
        print("\n") 
        if userInput == 1:
            course_Insert()
        elif userInput == 2:
            cView()
        elif userInput == 3:
            removecourse()
        else: 
            print("Enter correct choice. . . ")
    return True

def runAgain():
    # Run the initial table setup before starting the menu loop
    setup_database()
    
    MenuSet()
    
    runAgn = input("\nWant To Run Again Y/n: ")
    while runAgn.lower() == 'y':
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
            
        MenuSet()
        runAgn = input("\nWant To Run Again Y/n: ")

# Start the application
if __name__ == "__main__":
    runAgain()