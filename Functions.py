import mysql.connector as msc
from mymodule import BankAtm
def insert_query(query, **kwargs):
    mydb = msc.connect(host='localhost',user='root',password='Neeraj@123',database=kwargs['database'])
    mycur = mydb.cursor()
    mycur.execute(query)
    mydb.commit()

def Create_databse(database_name):
    db = msc.connect(host='localhost',user='root',password='Neeraj@123')
    mycur = db.cursor()
    mycur.execute(f"Create Database {database_name}")
    return 'Created database'

def select_column(columns, **kwargs):
    db = msc.connect(host='localhost',user='root',password='Neeraj@123',database=kwargs['database'])
    mycur = db.cursor()
    mycur.execute(f"Select {columns} from {kwargs['tname']}")
    x = mycur.fetchall()
    return x

# New customer open bank account
def to_open_account(cus_id):
    import datetime
    import random
    Branch = input('Enter Branch name: ')
    # name
    fname = input('Enter First name: ')
    lname = input('Enter last name: ')
    name = f"{fname} {lname}"
    occupation = input('Enter Occupation(e.g. Student/Goverment Job/Employee etc.): ')
    doc_type = input('Enter Document ID Type: ')
    doc_id = input('Enter Document Id No: ')
    account_no = random.randint(1000,1000000)
    ifsc = random.randint(100,1000)
    csid = str(cus_id)
    ifsc_code = f"{csid[2]}BOI{ifsc}"
    con = int(input('Enter mobile number: '))
    if len(str(con)) == 10:
        contact = str(con)
    else:
        con1 = int(input('Please Re-enter mobile number: '))
        if len(str(con1)) == 10:
            contact = str(con1)
    email = input('Enter email id: ')
    # address
    village = input('Enter Village: ')
    post = input('Enter post: ')
    city = input('Enter City: ')
    Distt = input('Enter District: ')
    state = input('Enter State: ')
    pincode = int(input('Enter pin code: '))
    address = f"{village} {post} {city} {Distt} {state} - {pincode}"
    # fetch current date
    date = datetime.datetime.now()
    year = date.strftime("%Y")
    month = date.strftime("%m")
    day = date.strftime("%d")
    ac_open_dt = f"{year}-{month}-{day}"
    # import data csv_file and database

    # to csv_file
    file = open("C:\\Users\\neera\\OneDrive\\Documents\\All Projects\\Python Projects\\Bank Account Clone\\Dataset\\Customer_Data.csv",'a')
    x = f"{Branch},{cus_id},{name},{occupation},{doc_type},{doc_id},{account_no},{ifsc_code},{contact},{email},{address},{state},{pincode},{ac_open_dt}\n"
    file.write(x)
    file.close()

    # to sql database
    mydb = msc.connect(host='localhost',user='root',password='Neeraj@123',database='Bank')
    mycur = mydb.cursor()
    sql = f"insert into Customer_detail values ('{Branch}',{cus_id},'{name}','{occupation}','{doc_type}','{doc_id}','{account_no}','{ifsc_code}','{contact}','{email}','{address}','{state}','{pincode}','{ac_open_dt}')"
    mycur.execute(sql)
    mydb.commit()
    return 'Account has been created.'

# Apply for new debit card
def debit_card(cus_id):
    import random
    import mysql.connector as msc
    import datetime
    atm_No = random.randint(1000000000000000,9999999999999999)
    cpin = int(input('Create pin: '))
    if len(str(cpin)) == 4:
        epin = cpin
    else:
        cpin = int(input('Please Re-enter pin: '))
        if len(str(cpin)) == 4:
            epin = cpin
        else:
            print('Something went wrong')
            exit()
    # convert decimal to hex string
    pin = hex(epin)
    date = datetime.datetime.now()
    year = date.strftime('%Y')
    month = date.strftime('%m')
    day = date.strftime('%d')
    vaild_from = f"{year}-{month}-{day}"
    y = str(int(year)+6)
    valid_thru = f"{y}-{month}-{day}"
    sql = f"insert into atm_data values ({cus_id},'{atm_No}','{pin}','{vaild_from}','{valid_thru}',0)"
    insert_query(sql, database='bank')
    output =  select_column('atm_No', tname='atm_data', database='bank')
    ss = f"| Your ATM number is {output[0][0]}. |"
    for i in range(len(ss)):
        print('-',end='')
    print()
    print(ss)
    for i in range(len(ss)):
        print('-',end='')
    print()
    
    
# Update Customer
def update_customer(c_id):
    mydb = msc.connect(host='localhost',user='root',password='Neeraj@123',database='bank')
    print('What do you want to change.\n1. Mobile number\n2. Email-ID\n3. Document ID\n4. ID number\n5. Name\n6. Change Atm pin')
    change = int(input('Choose any one of the above: '))
    if change == 1:
        mobile_number = int(input('Enter new mobile number: '))
        if len(str(mobile_number))==10:
            mycur = mydb.cursor()
            mycur.execute(f"update customer_detail set contact='{str(mobile_number)}' where customer_id={c_id}")
            mydb.commit()
            print('Sucessfully update mobile number.')
        else:
            print('! Invaild number.')
    elif change == 2:
        email = input('Enter new email-id: ')
        mycur = mydb.cursor()
        mycur.execute(f"update customer_detail set email_id='{email}' where customer_id={c_id}")
        mydb.commit()
        print('Sucessfully update Email-Id number.')
    elif change == 3:
        document = input('Enter new Document-id: ')
        mycur = mydb.cursor()
        mycur.execute(f"update customer_detail set id='{document}' where customer_id={c_id}")
        mydb.commit()
        print('Sucessfully update Document number.')
    elif change == 4:
        document_no = int(input('Enter new Document No: '))
        mycur = mydb.cursor()
        mycur.execute(f"update customer_detail set id_no='{document_no}' where customer_id={c_id}")
        mydb.commit()
        print('Sucessfully update Document No number.')
    elif change == 5:
        name = input('Enter new Name: ')
        mycur = mydb.cursor()
        mycur.execute(f"update customer_detail set name='{name}' where customer_id={c_id}")
        mydb.commit()
        print('Sucessfully update Name number.')
    elif change == 6:
        new_pass = int(input('Enter New ATM 4-digit pine: '))
        if len(str(new_pass)) == 4:
            account_number = int(input('Enter your A/C number: '))
            p3 = BankAtm(c_id)
            if str(account_number) == p3.Account_number:
                mycur = mydb.cursor()
                query = f"update atm_data set pine='{hex(new_pass)}' where customer_id={p3.Customer_id}"
                mycur.execute(query)
                mydb.commit()
                print('Sucessfully Updated your pin.')
        else:
            print('Wrong ATM number.')
    else:
        print('Incorrect choose')
