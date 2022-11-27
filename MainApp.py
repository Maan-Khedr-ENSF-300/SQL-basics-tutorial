import mysql.connector

# Connect to server
print("Welcome to the Archery Olympics Database:")
print("In order to proceed please select your role from the list below:")
print("1-DB Admin")
print("2-Data Entry")
print("3-Browse as guest")

selection = input("please type 1, 2, or 3 to select your role:")

if selection in ['1','2']:
    username= input("user name:")
    passcode= input ("password:")
else:
    username="guest"
    passcode=None

cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user=username,
    password= passcode)


# Get a cursor
cur = cnx.cursor()


# Execute a query
cur.execute("use olympicarchery")



# Fetch results
col_names=cur.column_names
print("Attribute List:\n")
att_size=len(col_names)
for i in range(att_size):
    print(col_names[i],'\t',end='')
print()
print(120*'-')


rows = cur.fetchone()
print("number of entries in table\n",len(rows))
print("Current employee table content:\n ",rows)
rows = cur.fetchall()
print("number of entries in table\n",len(rows))
print("Current employee table content:\n ",rows)

# a slightly better way
cur.execute("select * from employee")
rows = cur.fetchall()
print("Current employee table content:\n ")
size=len(rows)
for i in range(size):
    for x in range(len(rows[i])):
        print(rows[i][x],end='\t')
    print()

insert_employee=("insert into employee "
                  "values (%(fname)s,%(minit)s,%(lname)s,%s,%s,%s,%s,%d,%s,%s)")
employee_data= ('m','e','k','010101010',None,None,None,55500,None,4)

emp_data={
    'fname':'Maan',
    'lname':'k',
    'ssn':'',

}
cur.execute(insert_employee,emp_data)
#cur.execute(insert_employee,employee_data)
cur.execute("insert into employee values ('m','e','k','101010101',null,null,null,55500,null,4)")
cnx.commit()

# Close connection
cnx.close()