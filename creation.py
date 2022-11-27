import mysql.connector

cnx = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user='root',
    password= 'Mkhedr@1986')


# Get a cursor
cur = cnx.cursor()

fd = open('DBinit.sql', 'r')
sqlFile = fd.read()
fd.close()
sqlCommands = sqlFile.split(';')

for command in sqlCommands:
    try:
        if command.strip() != '':
            cur.execute(command)
    except (IOError, msg):
        print("Command skipped: ", msg)



# cur.execute("source D:\lenovo backup\D drive\Maan\\teaching\Fall 2022\ENSF 300\SQL with python tutorial\SQL-basics-tutorial\DBinit.sql")