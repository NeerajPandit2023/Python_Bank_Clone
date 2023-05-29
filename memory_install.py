# these code only one time run code 
import Functions
import mysql.connector as msc

# To Create table in database (MySQL)
Functions.Create_databse('Bank')
# customer details table 
mydb = msc.connect(host='localhost',user='root',password='Neeraj@123',database='Bank')
cur = mydb.cursor()
cur.execute('CREATE TABLE Customer_detail ( \
    Branch varchar(50), \
    Customer_id int NOT NULL, \
    Name varchar(255) NOT NULL, \
    Occupation varchar(50), \
    Id varchar(255) NOT NULL, \
    Id_No varchar(255) NOT NULL, \
    Account_No varchar(20) unique, \
    IFSC_Code varchar(20), \
    Contact char(10), \
    Email_id varchar(100), \
    Address varchar(255), \
    State varchar(50), \
    PinCode char(6), \
    Account_Open_Dt Date, \
    PRIMARY KEY (Customer_id) \
)')
# atm data table
mycur = mydb.cursor()
mycur.execute('create table atm_data ( \
                Customer_id int, \
                Atm_No char(16) unique, \
                Pine varchar(20), \
                Vaild_From date, \
                Vaild_Thru date, \
                Balance int, \
                foreign key(Customer_id) \
                references customer_detail(Customer_id) \
                on update cascade \
                on delete cascade \
)')

# To Create csv File header
# please change file location below for save csv file format
file = open(r"C:\Users\neera\OneDrive\Documents\All Projects\Python Projects\Bank Account Clone\Dataset\Customer_Data.csv",'w')
file.write('Branch,Customer_id,Name,Occupation,Document Id,Id No,Account No,IFSC Code,Mobile No,Email id,Address,State,Pin Code,A/C open Dt\n')
file.close()
print('Sucessfully installed')