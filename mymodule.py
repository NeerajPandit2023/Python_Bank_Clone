class BankAtm:
    def __init__(self, cus_id):
        import mysql.connector as msc
        from ast import literal_eval
        self.mydb = msc.connect(host='localhost',user='root',password='Neeraj@123',database='bank')
        mycur = self.mydb.cursor()
        sql = f"select * from customer_detail as cd inner join atm_data as a on cd.customer_id = a.customer_id where cd.customer_id={cus_id}"
        mycur.execute(sql)
        x = mycur.fetchone()
        self.x_1 = x
        self.Customer_id = x[1]
        self.Name = x[2]
        self.Account_number = x[6]
        self.ifsc_code = x[7]
        self.atm_no = x[15]
        self.email_id = x[9]
        self.mobile_no = x[8]
        self.atm_pin = literal_eval(x[16])
        self.Balance = x[19]
    
    def pin(self):
        return self.atm_pin
    
    def display(self):
        data = self.x_1
        print("---------------------Welcome to my Bank---------------------------")
        print(f"| Branch: {data[0]}\t\t Customer-ID: {data[1]}                |")
        print("------------------------------------------------------------------")
        print(f"| Name: {data[2]}\t\t Occupation: {data[3]}")
        print(f"| Document: {data[4]}\t\t Document-No: {data[5]}")
        print(f"| A/C No: {data[6]}\t\t IFSC Code: {data[7]}")
        print(f"| Mobile No: {data[8]}\t\t E-mail: {data[9]}")
        print(f"| Address: {data[10][:-25]}\t State: {data[11]}")
        print(f"| ATM No: {data[15]}\t A/C open date: {data[13]}")
        print("------------------------------------------------------------------")
        
    def check_pin(self):
        return f"Your pin is {self.atm_pin}"
        
    def Atm_machine(self):
        for i in range(100):
            message = f"|          Welcome to MYBANK ATM          |"
            for line in range(len(message)):
                print('-',end='')
            print()
            print(message)
            for line in range(len(message)):
                print('-',end='')
            print()
            pin=int(input("Enter your pin (to exit press'0'): "))
            if pin == self.atm_pin:
                lin = f"| Customer Name: {self.Name} | Account number: xxx{self.Account_number[-4:]} |"
                for line in range(len(lin)):
                    print('-',end='')
                print()
                print(lin)
                for line in range(len(lin)):
                    print('-',end='')
                print()
                for k in range(5):
                    c=int(input('choose your tarnsaction\n1. Withdraw\n2. Balance enqueiry\n3. fast cash\n: '))
                    if c == 1:
                        x=int(input('Enter your widthdraw amount: '))
                        n=self.Balance
                        if (n==x or n>x) and x%100==0:
                            ubal=n-x
                            cur = self.mydb
                            adb = cur.cursor()
                            sql = f"update atm_data set balance={ubal} where customer_id={self.Customer_id}"
                            adb.execute(sql)
                            self.mydb.commit()
                            print('Thank you for transaction')
                            print('Please collect cash And Debit Card')
                        elif x%100!=0:
                            print("Incorrect Ammount.")
                        else:
                            print('>>>Sorry! your available balance is',self.Balance,'only. So Failed transaction')
                        if k!=4:
                            x2=input('If you want to check more operation (yes/no): ')
                            if x2=='no':
                                break
                    elif c == 2:
                        adb=self.mydb.cursor()
                        adb.execute(f'select balance from atm_data where customer_id={self.Customer_id}')
                        x_1 = adb.fetchone()
                        print('Available balance is',x_1[0])
                        if k!=4:
                            x2=input('If you want to check more operation (yes/no): ')
                            if x2=='no':
                                break
                    elif c == 3:
                        f=int(input('choose amount 1-1000, 2-500, 3-2000, 4,5000 : '))
                        adb=self.mydb.cursor()
                        adb.execute(f"select balance from atm_data where customer_id={self.Customer_id}")
                        k_1=adb.fetchone()
                        k = k_1[0]
                        if f==1 and k>f:
                            adb=self.mydb.cursor()
                            uba=k-1000
                            adb.execute(f'update atm_data set balance={uba} where customer_id={self.Customer_id}')
                            self.mydb.commit()
                            print('Take cash 1000')
                        elif f==2 and k>f:
                            adb=self.mydb.cursor()
                            uba=k-500
                            adb.execute(f'update atm_data set balance={uba} where customer_id={self.Customer_id}')
                            self.mydb.commit()
                            print('Take cash 500')
                        elif f==3 and k>f:
                            adb=self.mydb.cursor()
                            uba=k-2000
                            adb.execute(f'update atm_data set balance={uba} where customer_id={self.Customer_id}')
                            self.mydb.commit()
                            print('Take cash 2000')
                        elif f==4 and k>f:
                            adb=self.mydb.cursor()
                            uba=k-5000
                            adb.execute(f'update atm_data set balance={uba} where customer_id={self.Customer_id}')
                            self.mydb.commit()
                            print('Take cash 5000')
                        else:
                            print('please choose amount.')
                        if k!=4:
                            x2=input('If you want to check more operation (yes/no): ')
                            if x2=='no':
                                break
                    else:
                        print('please Choose any one.')
                else:
                    print('You have completed more transcation so try later.')
            elif pin==0:
                break
            else:
                print('Wrong pin')
                ask = input("If you want to change ATM pin. If 'yes' to click '1': ")
                if ask == '1':
                    new_pass = int(input('Enter New ATM 4-digit pine: '))
                    if len(str(new_pass)) == 4:
                        account_number = int(input('Enter your A/C number: '))
                        if str(account_number) == self.Account_number:
                            cur_1 = self.mydb.cursor()
                            query = f"update atm_data set pine='{hex(new_pass)}' where customer_id={self.Customer_id}"
                            cur_1.execute(query)
                            self.mydb.commit()
                            self.atm_pin = new_pass
                            print('Sucessfully Updated your pin.')
                        else:
                            print('Wrong ATM number.')
                    else:
                        print('Please enter 4-digit number.')
                    
                
    def deposite_balance(self,cus_id, Amount):
        if self.Customer_id == cus_id:
            bal = self.Balance + Amount
            x = self.mydb.cursor()
            x.execute(f'update atm_data set balance = {bal} where Customer_id = {self.Customer_id}')
            self.mydb.commit()
            print(f'Now, Your Bank Balance {bal}')
            
class check_customer:
    def __init__(self,cus_id):
        import mysql.connector as msc
        mydb = msc.connect(host='localhost',user='root',password='Neeraj@123',database='bank')
        mycur = mydb.cursor()
        mycur.execute("select customer_id from customer_detail")
        x = mycur.fetchall()
        for i in x:
            if cus_id == i[0]:
                b = True
                break
        else:
            b = False
        self.b = b
        
class Bank:
    def __init__(self, cus_id):
        import mysql.connector as msc
        from ast import literal_eval
        self.mydb = msc.connect(host='localhost',user='root',password='Neeraj@123',database='bank')
        mycur = self.mydb.cursor()
        self.cur = mycur
        sql = f"select * from customer_detail where customer_id = {cus_id}"
        mycur.execute(sql)
        x = mycur.fetchone()
        self.x_1 = x
        self.Customer_id = x[1]
        self.Name = x[2]
        self.Account_number = x[6]
        self.ifsc_code = x[7]
        self.email_id = x[9]
        self.mobile_no = x[8] 
        
    def display(self):
        data = self.x_1
        print("---------------------Welcome to my Bank---------------------------")
        print(f"| Branch: {data[0]}\t\t Customer-ID: {data[1]}                |")
        print("------------------------------------------------------------------")
        print(f"| Name: {data[2]}\t Occupation: {data[3]}             ")
        print(f"| Document: {data[4]}\t\t Document-No: {data[5]}    ")
        print(f"| A/C No: {data[6]}\t\t IFSC Code: {data[7]}              ")
        print(f"| Mobile No: {data[8]}\t\t E-mail: {data[9]}  ")
        print(f"| A/C open date: {data[13]}\t State: {data[11]}       ")
        print(f"| Address: {data[10][:-10]}                    ")
        print("------------------------------------------------------------------")
               