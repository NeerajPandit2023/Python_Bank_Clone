import mymodule
import Functions
for interface in range(100):
    print('------------------ Welcome to my Bank --------------------')
    print("1. New bank account for open\n2. For apply debit card\n3. ATM machince\n4. Deposite Balance\n5. KYC/Update Account\n6. Show Customers detail\n7. check customer balance and atm-pin\n8. Quit")
    try:
        choose_user = int(input('Choose any one of the above: '))
    except:
        print('Please enter integer number.')
    else:
        # New bank account for open
        if choose_user == 1:
            try:
                cus_id = int(input('Enter Customer-ID: '))
            except:
                print('Something went wrong. Try again')
            else:
                x = Functions.to_open_account(cus_id)
                print(x)
                user = mymodule.Bank(cus_id)
                user.display()
        # For apply debit card
        elif choose_user == 2:
            try:
                cus = int(input('Enter Customer_ID: '))
            except:
                print('Something went wrong. Try again')
            else:
                users = mymodule.check_customer(cus)
                if users.b:
                    Functions.debit_card(cus)
                    print('Sucessfully Applied your debit card.')
                else:
                    print('Customer not found.')
        # Atm Machine
        elif choose_user == 3:
            try:
                cus = int(input('Enter Customer_ID: '))
            except:
                print('Incorret Customer-ID and Customer Name.')
            else:
                users = mymodule.check_customer(cus)
                if users.b:
                    atm_user = mymodule.BankAtm(cus)
                    atm_user.Atm_machine()
                else:
                    print('Customer not found.')
        # Deposite Balance
        elif choose_user == 4:
            try:
                customer_id = int(input('Enter Customer_ID: '))
            except:
                print('Incorrect input.')
            else:
                users = mymodule.check_customer(customer_id)
                if users.b:
                    Amount = int(input('Enter Amount: '))
                    p1 = mymodule.BankAtm(customer_id)
                    p1.deposite_balance(customer_id,Amount)
                else:
                    print('Customer not found.')
        # Update detail on customer
        elif choose_user == 5:
            try:
                customer_id = int(input('Enter Customer_ID: '))
            except:
                print('Incorrect input.')
            else:
                users = mymodule.check_customer(customer_id)
                if users.b:
                    Functions.update_customer(customer_id)
                else:
                    print('Customer not found.')
        # Show Customers detail
        elif choose_user == 6:
            try:
                customer_id = int(input('Enter Customer_ID: '))
            except:
                print('Incorrect input.')
            else:
                users = mymodule.check_customer(customer_id)
                if users.b:
                    p2 = mymodule.BankAtm(customer_id)
                    p2.display()
                else:
                    print('Customer not found.')
        # check customer balance and atm-pin
        elif choose_user == 7:
            try:
                customer_id = int(input('Enter Customer_ID: '))
            except:
                print('Incorrect input.')
            else:
                users = mymodule.check_customer(customer_id)
                if users.b:
                    p2 = mymodule.BankAtm(customer_id)
                    zx = f"| Name: {p2.Name} | A/c No: {p2.Account_number} | Balance: {p2.Balance} | ATM Pin: {p2.atm_pin} |"
                    for i in range(len(zx)):
                        print('-',end='')
                    print()
                    print(zx)
                    for i in range(len(zx)):
                        print('-',end='')
                    print()
                else:
                    print('Customer not found.')
        # Exit Program
        elif choose_user == 8:
            exit()
        else:
            print('Please Choose any one button')