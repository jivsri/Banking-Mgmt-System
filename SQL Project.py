print("********************************************************************************************************************************************************\n")
print("********************************************************************************************************************************************************\n")
print("*****************************************************WELCOME TO PEOPLE'S BANK***************************************************************************\n")
print("********************************************************************************************************************************************************\n")
print("********************************************************************************************************************************************************\n\n\n")


import mysql.connector as p
import random
mydb=p.connect(host='localhost',password='9900@JivSri',user='root',database='bank')
cur=mydb.cursor()
#cur.execute("CREATE TABLE acc(Account_no int Primary key,Name varchar(25),Age int(2),F_Name varchar(50),M_Name varchar(50),Address varchar(999),Amount int)")
#cur.execute("CREATE TABLE passwords(Account_no int Primary key,password int (4),Foreign Key(Account_no) references acc(Account_no) on delete cascade)")

#cur.execute("ALTER TABLE acc MODIFY COLUMN Amount int")
#cur.execute("ALTER TABLE trans ADD Balance int")
#cur.execute("DROP TABLE trans")

#qrystr = """CREATE TRIGGER trigger12 AFTER UPDATE ON acc FOR EACH ROW BEGIN IF !(new.Amount<=>old.Amount) THEN INSERT INTO trans values(old.Account_no,new.Amount-old.Amount,new.Amount); END IF;END;"""
#tran_id=random.randint(10000000,99999999)
#cur.execute(qrystr)
#mydb.commit()

#cur.execute("CREATE TABLE trans(Account_no int,Amount int,Balance int,Foreign Key(Account_no) references acc(Account_no) on delete cascade)")
#cur.execute("CREATE TABLE loan_info(Loan_id int primary key,Account_no int,Principal int,ROI int,Type varchar(30),Status varchar(30))")



#customer area

def customer_area():
    
    print('''\n\n\t     1.Opening of Bank Account
             2.Closing of Bank Account
             3.Deposit Money
             4.Withdraw Money
             5.Bank Statement
             6.Change Password
             7.Edit the Details of the Account
             8.Exit the Bank''')
    
    choice=int(input("\n\nEnter your choice: "))





    #choice 1
    
    if choice==1:
        print("Please fill the following form for the opening of the account")
        n=input("Enter your name:")
        age=int(input("Enter your age:"))
        add=input("Enter your address:")
        father=input("Enter your father's name:")
        mother=input("Enter your mother's name:")
        aadhar=int(input("Enter your aadhar number:"))
        import random
        acn=random.randint(10000000,99999999)
        print("Your New Account Number is:",acn)
        print("SET A NEW PASSWORD")
        passw=int(input("Enter your new password(4-digit):"))
        amt=0
        print("Your new account has successfully created with your new password")

        #mysql part starts
        query="INSERT INTO acc VALUES(%s,%s,%s,%s,%s,%s,%s)"
        record=(acn,n,age,father,mother,add,amt)
        cur.execute(query,record)
        mydb.commit()
        cur.execute("insert into passwords values(%s,%s)",(acn,passw))
        mydb.commit()
        
        print("\nTHANKS NOW YOU ARE THE MEMBER OF OUR BANK\n")
        





    #choice 2


    if choice==2:
        cur.execute("Select * from passwords")
        myrecord=cur.fetchall()
        count1=cur.rowcount
        
        if count1==0:
            print("There are no existing bank accounts\nFIRST OPEN ONE ACCOUNT")
            
            
        else:
            acc1=int(input("Enter your account number:"))
            check=True
            for b in myrecord:
                if acc1==b[0]:
                    check=False
                    passw2=int(input("Enter your password:"))
                    if passw2==b[1]:
                        cur.execute("DELETE FROM passwords where Account_no=%s",(acc1,))
                        mydb.commit()
                        cur.execute("DELETE FROM acc where Account_no=%s",(acc1,))
                        mydb.commit()
                        
                        print("YOUR ACCOUNT HAS SUCCESSFULLY CLOSED")
                        break
                    else:
                        print("You have entered wrong password\n")
                        print("TRY AGAIN!")
                        break

            if check==True:
                print("There is no such account in our bank")
                print("PLEASE TRY AGAIN!")
    







#choice 3


        
    if choice==3:
        cur.execute("Select * from passwords")
        myrecord=cur.fetchall()
        count=cur.rowcount
        
        if count==0:
            print("There are no existing bank accounts\nFIRST OPEN ONE ACCOUNT")
        
        else:
            acc=int(input("Enter your account number:"))
            check=True
            for c in myrecord:
                if acc==c[0]:
                    check=False
                    passw=int(input("Enter your password:"))
                    if passw==c[1]:
                        money=int(input("ENTER THE AMOUNT OF MONEY YOU WANT TO DEPOSIT:"))
                        cur.execute("SELECT Amount from acc where Account_no=%s",(acc,))
                        arr=cur.fetchall()
                        amt=arr[0][0]
                        newam=amt+money
                        print("New amount :",newam)
                        cur.execute("UPDATE acc set Amount=%s where Account_no=%s",(newam,acc))
                        mydb.commit()
                        
                        print("You have successfully deposited your money")
                        
                    else:
                        print("You have entered wrong password\n")
                        print("TRY AGAIN!")
        

            if check==True:
                print("This account number does not exist")
                print("FIRST CREATE NEW BANK ACCOUNT")
                








    #choice 4


    if choice==4:
        cur.execute("Select * from passwords")
        myrecord=cur.fetchall()
        count=cur.rowcount
        
        if count==0:
            print("There are no existing bank accounts\nFIRST OPEN ONE ACCOUNT")
            
        else:
            acc=int(input("Enter your account number:"))
            check=True
            for c in myrecord:
                if acc==c[0]:
                    check=False
                    passw=int(input("Enter your password:"))
                    if passw==c[1]:
                        cur.execute("SELECT Amount from acc where Account_no=%s",(acc,))
                        arr=cur.fetchall()
                        amt=arr[0][0]
                        if amt==0:
                            print("There is zero balance in your account\nFIRST DEPOSIT SOME MONEY")
                            break
                        else:
                            money=int(input("ENTER THE AMOUNT OF MONEY YOU WANT TO WITHDRAW:"))
                            if money>amt:
                                print("Insufficient Balance\nPLEASE TRY AGAIN!")
                                    
                            else:
                                newam=amt-money
                                cur.execute("UPDATE acc set Amount=%s where Account_no=%s",(newam,acc))
                                mydb.commit()
                                print("You have successfully withdrawn your money")
                                    
                    else:
                        print("You have entered wrong password\n")
                        print("TRY AGAIN!")
                            


            if check==True:
                print("This account number does not exist")
                print("FIRST CREATE NEW BANK ACCOUNT")

                






    #choice 5

    if choice==5:
        cur.execute("Select * from passwords")
        myrecord=cur.fetchall()
        count=cur.rowcount
        
        if count==0:
            print("There are no existing bank accounts\nFIRST OPEN ONE ACCOUNT")
        
        else:
            acc=int(input("Enter your account number:"))
            check=True
            for d in myrecord:
                if acc==d[0]:
                    check=False
                    passw=int(input("Enter your password:"))
                    if passw==d[1]:
                        cur.execute("SELECT * from acc where Account_no=%s",(acc,))
                        arr=cur.fetchall()
                        print("Account Number: ",arr[0][0])
                        print("Name: ",arr[0][1])
                        print("Age: ",arr[0][2])
                        print("Father's Name: ",arr[0][3])
                        print("Mother's Name: ",arr[0][4])
                        print("Address: ",arr[0][5])
                        #print("Balance: ",arr[0][6])

                        cur.execute("SELECT * from trans where Account_no=%s",(acc,))
                        rec=cur.fetchall()
                        print("\n\nACCOUNT TRANSANCTIONS\n")
                        print("(Account_no,Amount,Balance)")
                        for i in rec:
                            print(i)
                    
                    else:
                        print("You have entered wrong password\n")
                        print("TRY AGAIN!")
                    
            if check==True:
                print("This account number does not exist")
                print("FIRST CREATE NEW BANK ACCOUNT")






    #choice 6


    if choice==6:
        cur.execute("Select * from passwords")
        myrecord=cur.fetchall()
        count=cur.rowcount
        
        if count1==0:
            print("There are no existing bank accounts\nFIRST OPEN ONE ACCOUNT")
        
        else:
            acc=int(input("Enter your account number:"))
            check=True
            for c in myrecord:
                if acc==c[0]:
                    check=False
                    passw=int(input("Enter your old password:"))
                    if passw==c[1]:
                        new1=int(input("ENTER YOUR NEW PASSWORD(4-digit):"))
                        cur.execute("UPDATE passwords set password=%s where Account_no=%s",(new1,acc))
                        mydb.commit()
                        print("Your password has successfully changed")
                
                    else:
                        print("You have entered wrong password\n")
                        print("TRY AGAIN!")
                            

            if check==True:
                print("This account number does not exist")
                print("FIRST CREATE NEW BANK ACCOUNT")






    #choice 7


    if choice==7:
        cur.execute("Select * from passwords")
        myrecord=cur.fetchall()
        count=cur.rowcount
        
        if count==0:
            print("There are no existing bank accounts\nFIRST OPEN ONE ACCOUNT")
        
        else:
            acc=int(input("Enter your account number:"))
            check=True
            for c in myrecord:
                if acc==c[0]:
                    check=False
                    car=int(input("Enter your password:"))
                    if car==c[1]:
                        print("What You want to edit? ")
                        print("1.Address")
                        print("2.Age")
                        print("3.Name")
                        print("4.Father's Name")
                        print("4.Mother's Name")
                        
                        
                        make=int(input("Choose:"))
                        if make==1:
                            add1=input("Enter your new address:")
                            cur.execute("UPDATE acc set Address=%s where Account_no=%s",(add1,acc))
                            mydb.commit()
                            print("Your address has successfully changed")
                            
                        if make==2:
                            age1=input("Enter your new Age:")
                            cur.execute("UPDATE acc set Age=%s where Account_no=%s",(age1,acc))
                            mydb.commit()
                            print("Your age has successfully changed")
                                
                        if make==3:
                            name1=input("Enter your new name:")
                            cur.execute("UPDATE acc set Name=%s where Account_no=%s",(name1,acc))
                            mydb.commit()
                            print("Your name has successfully changed")
                            
                        if make==4:
                            name1=input("Enter your new father's name:")
                            cur.execute("UPDATE acc set F_Name=%s where Account_no=%s",(name1,acc))
                            mydb.commit()
                            print("Your Father's name has successfully changed")
                            
                        if make==5:
                            name1=input("Enter your new mother's name:")
                            cur.execute("UPDATE acc set M_Name=%s where Account_no=%s",(name1,acc))
                            mydb.commit()
                            print("Your Mother's name has successfully changed")
                            
                                
                                
                    else:
                        print("You have entered wrong password\n")
                        print("TRY AGAIN!")
                            
            if check==True:
                print("This account number does not exist")
                print("FIRST CREATE NEW BANK ACCOUNT")





    #choice 8
    if choice==8:
        print("THANKS FOR VISITING OUR BANK")
        

        

    else:
        print("THANKS FOR VISITING OUR BANK")
    







    


#main function

while True:
    customer_area()
    choice=input("Do you want to continue to avail services: ")
    if choice in ("NO","no","No"):
        break

