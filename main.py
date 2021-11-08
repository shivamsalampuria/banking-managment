import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='username',                                 #Enter Your username.
    passwd='xyz',                                    #Enter Your Password.
    database ='BANK_DB',                             #Enter Database name created at line 11 and Delete line 11.
    auth_plugin='mysql_native_password'
)
c = mydb.cursor(buffered=True)
#c.execute('CREATE DATABASE BANK_DB')                #Create Database First.

def Menu():                                          #Display Main Menu
    print("*"*200)
    print("MAIN MENU".center(200))
    print("1.Insert Records".center(200))
    print("2.Display Records".center(200))
    print("3.Search Records".center(200))
    print("4.Update Records".center(200))
    print("5.Delete Records".center(200))
    print("6.Transaction from Account".center(200))
    print("7.Exit".center(200))
    print("*" * 200)

def MenuSort():                                     #Sub-menu for command 2
    print("a.sorted as per Account number".center(200))
    print("b.sorted as per Customer name".center(200))
    print("c.sorted as per Balance".center(200))
    print("d.Back".center(200))


def MenuTransaction():                              #Sub-menu for command 6
    print("a.Debit/Withdraw from account".center(200))
    print("b.Credit into the account".center(200))
    print("c.Back".center(200))


def Create():                          #Function to create a table if not already exist.
    try:
        cmd = 'CREATE TABLE RECORDS(ACC_NO VARCHAR(20),NAME VARCHAR(30),MOBILE VARCHAR(10),EMAIL VARCHAR(50),ADDRESS VARCHAR(50),CITY VARCHAR(50),COUNTRY VARCHAR(10),BALANCE FLOAT(20))'
        c.execute(cmd)
        print('Table Created Successfully !')
        Insert()
    except:
        print('Table Already Exists.')
        Insert()

def Insert():                          #Function to insert data in Already Existing Table
    while True :                       #Looping for accepting Record
        ACC_NO = input("Enter Account Number : ")
        NAME = input("Enter Your Name : ")
        MOBILE = input("Enter Your Mobile Number : ")
        EMAIL = input("Enter your E-mail Address : ")
        ADDRESS = input("Enter Your Address : ")
        CITY = input("Enter Your City : ")
        COUNTRY = input("Enter Your Country : ")
        BALANCE = float(input("Enter Balance : "))
        rec = [ACC_NO,NAME,MOBILE,EMAIL,ADDRESS,CITY,COUNTRY,BALANCE]
        cmd = 'INSERT INTO RECORDS VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
        c.execute(cmd,rec)
        mydb.commit()
        ch = input ("Do you want to enter more records [y/n]? ")
        if ch=="N" or ch=="n":
            break
        elif ch=="Y" or ch=="y":
            continue

def DispSortAcc():                  #Function to display records as per acsending order of Account Number
    try:
        cmd = 'SELECT* FROM RECORDS ORDER BY ACC_NO '
        c.execute(cmd)
        S = c.fetchall()
        F = '%20s %21s %21s %21s %21s %21s %21s %20s'
        print(F % ("ACC_NO","NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*180)
        for i in S:
            for j in i :
                print("%22s" % j, end='')
            print()
        print("="*180)
    except:
        print("Table not found !")

def DispSortName():                  #Function to display records as per acsending order of Name
    try:
        cmd = 'SELECT* FROM RECORDS ORDER BY NAME'
        c.execute(cmd)
        S = c.fetchall()
        F = '%20s %21s %21s %21s %21s %21s %21s %20s'
        print(F % ("ACC_NO","NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*180)
        for i in S:
            for j in i :
                print("%22s" % j, end='')
            print()
        print("="*180)
    except:
        print("Table not found !")

def DispSortBalance():                 #Function to display records as per acsending order of Balance
    try:
        cmd = 'SELECT* FROM RECORDS ORDER BY BALANCE '
        c.execute(cmd)
        S = c.fetchall()
        F = '%20s %21s %21s %21s %21s %21s %21s %20s'
        print(F % ("ACC_NO","NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
        print("="*180)
        for i in S:
            for j in i :
                print("%22s" % j, end='')
            print()
        print("="*180)
    except:
        print("Table not found !")

def DispSearchAcc():                 #Function to display records by entering account number
    try:
        cmd = 'SELECT * FROM RECORDS'
        c.execute(cmd)
        S = c.fetchall()
        ch = input("Enter the account number to be searched : ")
        for i in S :
            if i[0]==ch:
                print("="*180)
                F = '%20s %21s %21s %21s %21s %21s %21s %20s'
                print(F % ("ACC_NO","NAME","MOBILE","EMAIL","ADDRESS","CITY","COUNTRY","BALANCE"))
                print("=" * 180)
                for j in i:
                    print("%22s" % j, end='')
                print()
                break
        else:
            print("Record not found !")
    except:
        print("Table doesn't exist.")

def Update():                       # Function to change details of customer
    try:
        cmd='SELECT * FROM RECORDS'
        c.execute(cmd)
        S = c.fetchall()
        A=input("Enter account number to change details : ")
        for i in S:
            i=list(i)
            if i[0]==A:
                ch = input("Change Name [y/n]? : ")
                if ch=="y" or ch=="Y":
                    i[1]=input("Enter new Name : ")
                    i[1]=i[1].capitalize()

                ch = input("Change Mobile Number [y/n]? : ")
                if ch=="y" or ch=="Y":
                    i[2] = input("Enter new Number : ")

                ch = input("Change Email ID [y/n]? : ")
                if ch=="y" or ch=="Y":
                    i[3] = input("Enter new Email : ")

                ch = input("Change Address [y/n]? : ")
                if ch=="y" or ch=="Y":
                    i[4] = input("Enter new Address : ")
                    i[4]=i[4].capitalize()

                ch = input("Change City [y/n]? : ")
                if ch=="y" or ch=="Y":
                    i[5] = input("Enter new City : ")
                    i[5]=i[5].capitalize()

                ch = input("Change Country [y/n]? : ")
                if ch=="y" or ch=="Y":
                    i[6] = input("Enter new Country : ")
                    i[6]=i[6].capitalize()

                ch = input("Change Balance [y/n]? : ")
                if ch=="y" or ch=="Y":
                    i[7] = float(input("Enter new Balance : "))

                cmd = 'UPDATE RECORDS SET NAME=%s,MOBILE=%s,EMAIL=%s,ADDRESS=%s,CITY=%s,COUNTRY=%s,BALANCE=%s WHERE ACC_NO=%s'
                val= (i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                c.execute(cmd,val)
                mydb.commit()
                print("Account Updated.")
                break
        else:
            print("record Not found !")
    except:
        print("Table doesn't exist.")

def Delete():                       #Function to delete details of a customer
    try:
        cmd='SELECT * FROM RECORDS'
        c.execute(cmd)
        S = c.fetchall()
        A=input("Enter account number to delete record : ")
        for i in S :
            i=list(i)
            if i[0]==A:
                cmd="DELETE FROM RECORDS WHERE ACC_NO=%s"
                val= (i[0],)
                c.execute(cmd,val)
                mydb.commit()
                print("Account record deleted.")
                break
        else:
            print("Record not found !")
    except:
        print("Table doesn't exist.")



def Debit():                           #Function to withdrawing amount from record
    try:
        cmd = 'SELECT * FROM RECORDS'
        c.execute(cmd)
        S = c.fetchall()
        print(" *Please note that money can only be debited if minimum balance of Rs.5000 exists* ")
        acc  =input("Enter account number : ")
        for i in S :
            i=list(i)
            if i[0] == acc :
                amt = float(input("Enter the amount to be withdrawn : "))
                if i[7]-amt >= 5000:
                        i[7]-=amt
                        cmd="UPDATE RECORDS SET BALANCE=%s WHERE ACC_NO=%s"
                        val = (i[7],i[0])
                        c.execute(cmd,val)
                        mydb.commit()
                        print("Amount Debited.")
                        break
                else :
                        print("Insufficient balance ! Money can only be debited if minimum balance of Rs.5000 exists  ")
                        break
        else :
            print("Record not found !")
    except :
        print("Table doesn't exist")


def Credit():                              #Function to add the amount into records
    try:
        cmd = 'SELECT * FROM RECORDS'
        c.execute(cmd)
        S=c.fetchall()
        acc=input("Enter account number : ")
        for i in S :
            i=list(i)
            if i[0]==acc:
                amt = float(input("Enter the amount to be credited : "))
                i[7]+=amt
                cmd="UPDATE RECORDS SET BALANCE=%s WHERE ACC_NO=%s"
                val = (i[7],i[0])
                c.execute(cmd,val)
                mydb.commit()
                print("Amount Credited.")
                break
        else :
            print("Record not found !")
    except :
        print("Table doesn't exist")

while True:
    Menu()
    ch=input("Enter your choice : ")
    if ch == '1':
        Create()
    elif ch == '2':
        MenuSort()
        ch1=input("Enter your choice : ")
        if ch1 in ["a","A"]:
            DispSortAcc()
        elif ch1 in ["b","B"]:
            DispSortName()
        elif ch1 in ["c","C"]:
            DispSortBalance()
        elif ch1 in ["d","D"]:
            print("Back to Main Menu")
        else:
            print("Invalid Choice")
    elif ch == '3':
        DispSearchAcc()
    elif ch == '4':
        Update()
    elif ch == '5':
        Delete()
    elif ch == '6':
        while True:
            MenuTransaction()
            ch1=input("Enter your choice : ")
            if ch1 in ["a", "A"]:
                Debit()
            elif ch1 in ["b", "B"]:
                Credit()
            elif ch1 in ["c", "C"]:
                print("Back to Main Menu")
                break
            else:
                print("Invalid Choice")
                break
    elif ch=="7":
        print("Exiting......")
        break
    else:
        print("Invalid choice")
