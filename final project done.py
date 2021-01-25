import mysql.connector

# Establish connection with MySQL
db_connection = mysql.connector.connect(user='root', password='rootroot')
db_cursor = db_connection.cursor()

# Create Database and tables to be used
db_cursor.execute('create database IF NOT EXISTS Oliv_Proj')
db_cursor.execute('use Oliv_Proj')

# Creating tables
db_cursor.execute("CREATE TABLE IF NOT EXISTS employee (emp_name VARCHAR(200), street VARCHAR(200), city VARCHAR(200), salary INT, emp_id INT, company_ID INT, PRIMARY KEY (emp_name, emp_id))")
db_cursor.execute("CREATE TABLE IF NOT EXISTS company (company_id INT, company_name VARCHAR(200), city VARCHAR(200), phone_no VARCHAR(20), emp_id INT, PRIMARY KEY (company_id, emp_id))")
db_cursor.execute("CREATE TABLE IF NOT EXISTS customer (customer_id INT AUTO_INCREMENT PRIMARY KEY, customer_name VARCHAR(200), street VARCHAR(200), city VARCHAR(200), DOB INT)")
db_cursor.execute("CREATE TABLE IF NOT EXISTS account (account_number INT AUTO_INCREMENT PRIMARY KEY, balance INT, year_est INT )")
db_cursor.execute("CREATE TABLE IF NOT EXISTS loan (loan_number INT, account_number INT, loan_amount INT, PRIMARY KEY(loan_number, account_number))")

# Insert values into tables
val = [("Olivia", "Broadway", "Clifton", '457000', '123', '234'),
       ("Christopher","Orono", "Throng","400000","124","234"),
       ("Maggie","Houtan", "Havel","300000","125","236"),
       ("Sebastian","Colfax", "Clifton","450000","126","236"),
       ("Daniel","Main","Garfield","500000","128","236"),
       ("Matt","Clifton","Woodridge","300000","129","238"),
       ("Julie","PlesantView","Teaneck","327000","130","243"),
       ("Ashley","Alden","Monnachie","222000","131","243"),
       ("Julie","Hathway","Passaic","345000","132","238"),
       ("Monika","Morris","Lodi","450000","133","243")]

for value in val:
    sql = 'INSERT INTO employee(emp_name, street, city, salary, emp_id, company_id) VALUES ("{}", "{}", "{}", "{}", "{}", "{}")'.format(str(value[0]), str(value[1]), str(value[2]), int(value[3]), int(value[4]), int(value[5]))
    try:
        db_cursor.execute(sql)
        db_connection.commit()
    except:
        pass

val1=[("234","DMA","Clifton","9176549035","123"),
     ("235","MYA","Hawthorne", "1234000000","124"),
     ("236","AYA","Clifton", "1233020000","125"),
     ("237","DMA","Lodi", "9174500020","126"),
     ("238","AYA","Lodi","9735001000","127"),
     ("239","DMA","Wallington","9176549034","128"),
     ("240","MYA","Moonachie","1343270010","129"),
     ("241","MYA","Garfield","1212220003","130"),
     ("242","MYA","Clifton","1112220003","131"),
     ("243","DMA","Moonachie","1212220002","132")]

for value in val1:
    sql = "INSERT INTO company(company_ID, company_name, city, phone_no, emp_id) VALUES ({},'{}','{}','{}',{})".format(int(value[0]),str(value[1]),str(value[2]),str(value[3]),int(value[4]))
    try:
        db_cursor.execute(sql)
        db_connection.commit()
    except:
        pass


val2 = [("1234","Tom","Main ","Clifton", "07181999"),
       ("1233","Lily","Martine","Hawthorne", "10181969"),
       ("1232","Wyatt","Mamaroneck","Clifton", "12131998"),
       ("1231","Olivia","Old Scarsdale","Lodi", "07212000"),
       ("1230","Taii","Lake","Lodi","05131950"),
       ("1229","Erik","North Broadway","Wallington","11212000"),
       ("1228","Ariel","Valley","Moonachie","09012001"),
       ("1227","Theo","Garrettson","Garfield","12252000"),
       ("1226","Andrew","Washington","Clifton","01012001"),
       ("1225","May","North","Clifton","02031993")]

for value in val2:
    sql = "INSERT INTO customer(customer_id, customer_name, street, city, DOB) VALUES ({}, '{}','{}','{}','{}')".format(int(value[0]), str(value[1]), str(value[2]), str(value[3]), str(value[4]))
    try:
        db_cursor.execute(sql)
        db_connection.commit()
    except:
        pass


val3 = [("987","50000","2000"),
       ("986","9000","1975"),
       ("985","100000","1970"),
       ("984","15000","1998"),
       ("983","2000","2001"),
       ("982","35000","1981"),
       ("981","23000","1970"),
       ("980","23","1981"),
       ("979","12000","2000"),
       ("978","75000","2001")]

for value in val3:
    sql = "INSERT INTO account(account_number, balance,year_est) VALUES ({},{},{})".format(int(value[0]), int(value[1]), int(value[2]))
    try:
        db_cursor.execute(sql)
        db_connection.commit()
    except:
        pass

val4 = [("765", '987', 20000),
       ("345", '986', 3000),
       ("567", '985', 10000),
       ("278", '984', 1000),
       ("876", '983', 45000),
       ("978", '982', 35000),
       ("456", '981', 1000),
       ("189", '980', 4000),
       ("201", '979', 30000),
       ("908", '978', 30000)]


for value in val4:
    sql = "INSERT INTO loan(loan_number, account_number, loan_amount) VALUES ({},{},{})".format(int(value[0]), int(value[1]), value[2])
    try:
        db_cursor.execute(sql)
        db_connection.commit()
    except:
        pass


menu = """
1) Entering the Employee ID and I will provide you with the Company ID AND THE City where the employee works at.
2) Enter the account number to view the balance of the account and the current loan against that account.
3) Enter the account number to change the balance of the account.
4) Add a record about an account.
5) Delete a record about a account.
6) Exit.
"""

entered_value = int(input(menu))

while entered_value != 6:

    if entered_value == 1:
        entered_employee_id_number = int(input("Enter the employee ID number: "))
        sql = 'SELECT * FROM employee WHERE emp_id = {}'.format(entered_employee_id_number)
        try:
            db_cursor.execute(sql)
            data = db_cursor.fetchall()
            company_id = data[5]
            city = data[1]
            print("COMPANY ID: {}".format(company_id))
            print("CITY: {}".format(city))

        except:
            print("Does not exist")

    elif entered_value == 2:
        entered_account_number = int(input("Enter the account number: "))
        sql = 'SELECT * FROM account NATURAL JOIN loan WHERE account_number = {}'.format(entered_account_number)
        try:
            db_cursor.execute(sql)
            data = db_cursor.fetchall()

            account_balance = data[0][1]
            loan_amount = data[0][4]
            print("The current account balance is: ${}".format(account_balance))
            print("The current loan amount is: ${}".format(loan_amount))
        except:
            print("Does not exist")

    elif entered_value == 3:
        entered_account_number = int(input("Enter the account number: "))
        new_balance = int(input("Enter the new balance of the account: "))

        sql = "UPDATE account SET balance = {} WHERE account_number = {}".format(new_balance, entered_account_number)

        try:
            db_cursor.execute(sql)
            print("Balance UPDATED.")
        except:
            print("Does not exist")

    elif entered_value == 4:
        customer_name = input("Enter the account holders FULL NAME: ")
        customer_street = input("Enter their street name: ")
        customer_city = input("Enter the city: ")
        db_cursor.execute('SELECT MAX(customer_id) from customer')
        customer_id = db_cursor.fetchall()[0][0] + 1
        customer_DOB = int(input("Enter the year the customer was born: "))
        customer_balance = int(input("Enter the account starting balance: "))
        customer_loan_amount = int(input("Enter the customers loan amount: "))
        db_cursor.execute("SELECT MAX(account_number) from account")
        customer_account_number = db_cursor.fetchall()[0][0] + 1


        # SQL Queries to enter the user data into database
        # Query for customer table
        sql = "INSERT INTO customer(customer_id, customer_name, street, city, DOB) VALUES ({}, '{}','{}','{}','{}')".format(customer_id, customer_name, customer_street, customer_city, customer_DOB)

        try:
            db_cursor.execute(sql)
            db_connection.commit()
        except:
            print("Does not exist")
        # Query for account table
        sql = "INSERT INTO account(account_number, balance,year_est) VALUES ({},{},{})".format(customer_account_number, customer_balance, 2019)

        try:
            db_cursor.execute(sql)
            db_connection.commit()
        except:
            print("Does not exist")
        # Query for Loan table
        sql = "INSERT INTO loan(loan_number, account_number) VALUES ({},{})".format(customer_loan_amount, customer_account_number)

        try:
            db_cursor.execute(sql)
            db_connection.commit()

            print("VALUES ADDED SUCCESSFULLY!")
            print("New Customer Account Number: {}".format(customer_account_number))
        except:
            print("Does not exist")

    elif entered_value == 5:
        entered_account_number = int(input("Enter the account number to delete account record: "))
        entered_name = input("Enter the name of customer to delete record: ")

        sql = "DELETE FROM customer WHERE customer_name = '{}'".format(entered_name)
        try:
            db_cursor.execute(sql)
            db_connection.commit()
        except:
            print("Does not exist")

        sql = "DELETE FROM account WHERE account_number = {}".format(entered_account_number)
        try:
            db_cursor.execute(sql)
            db_connection.commit()
        except:
            print("Does not exist")

        sql = "DELETE FROM loan WHERE account_number = {}".format(entered_account_number)
        try:
            db_cursor.execute(sql)
            db_connection.commit()

            print("Successfully removed record.")
        except:
            print("Does not exist ")

    entered_value = int(input(menu))
