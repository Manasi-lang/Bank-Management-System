import mysql.connector

class LoginError(Exception):
    pass

class InsufficientBalanceError(Exception):
    pass

def main():
    user=[]
    customer=int(input("1.enter 1 for regestration\n 2.enter 2 for login"))
    if (customer==1):
        name=input("enter name")
        username=input("enter username")
        password=input("enter password")
        confirm_password=input("confirm_password")
        if password != confirm_password:
            print("password does not match try again")
            return
        else:
            age=int(input("enter age"))
            address=input("enter address")
            phone_no=int(input("enter phone_no"))
        

            mydb=mysql.connector.connect(
                host="localhost",
                username="root",
                password=2005,
                database="pythonconnectordb"
            )
            cur=mydb.cursor()
            s="INSERT INTO customer_details(name,username,password,age,address,phone_no)VALUES(%s,%s,%s,%s,%s,%s)"
            val=[('manasi','MANASI',123,21,'nashik',123456789)]
            cur.execute(s,val)
            mydb.commit()


            data=[name,username,password,age,address,phone_no]
            user.append(data)
            user.append([len(user)+1,username,password])
            print("regestration successful!")
            print(user)
            main()
            return
        
    customer=int(input("1.enter 1 for regestration\n 2.enter 2 for login"))
    if(customer==2):
        username=input("login username")
        password=input("login password")

    

        mydb=mysql.connector.connect(host="localhost",username="root",password=2005,database="pythonconnectordb")
        user_pswd = None
        username = None
        data=None
        cur=mydb.cursor()
        s="SELECT id, username, password,FROM customer_details WHERE username = %s"
        val=(id,username,password)
        cur.execute(s,val)
        mydb.commit()
        res=cur.fetchall()
        if res:
         db_username,db_password=res
         user_pswd =db_password
         username=db_username
         data=res
         print("login sucessfull")
        else:
         print("enter login id and username properly")
    try:
        for u in user: 
         if u[1] == username:
             user_pswd = u[2]

        if password!=user_pswd:
              raise LoginError
        
        print("Login Successfully")
        
    except LoginError:
        print("invalid username and password")
        exit(1)

def amt():
 customer=1
 balance = 0
 while (customer!=4):
        print("1.enter 1 for deposit \n 2. enter 2 for withdraw \n 3. enter 3 for show balance \n 4. enter 4 for exit")
        customer=int(input("enter choice"))
        
        if customer==1:
            amount=int(input("enter the amt"))
            balance=balance+amount
            print("depsoit amount",amount)
            
        elif customer==2:
            try:
                withdraw=int(input("enter the amt"))
                if withdraw>balance:
                    raise InsufficientBalanceError("Insufficient balance")
                else:
                    balance=balance-withdraw
                    print("withdraw amount",withdraw)
            except InsufficientBalanceError:
                print("insufficent balance")

        elif customer==3:
            print("balance amount",balance)

        elif customer==4:
            print("exit")
    
if __name__ == "__main__":
    main()
    amt()