''' Only creating Table is successful '''



import psycopg2

host = 'localhost'
user = 'postgres'
password = 'root'
port = '5432'
database = 'website15'


conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
if conn:
    print("connection successfull")


cur = conn.cursor()

option = input("Enter \n1.Create table\n2.Insert into:\n3.Query:\n4.Update:\n5.Delete:\n")
if(option=='1'):
    cur.execute("CREATE TABLE colony(serial INT PRIMARY KEY NOT NULL,NAME TEXT NOT NULL,SURNAME TEXT NOT NULL)")
    conn.commit()
    print("TABLE Created Successfully.")
elif(option=='2'):
    cur.execute("INSERT INTO colony(NAME, SURNAME) VALUES('New','Name')")
    conn.commit()
    print("inserted.")
elif(option=='3'):
    # cur.execute("SELECT * FROM public.colony")        # Both are same this or below
    cur.execute("SELECT * FROM colony")
    rows = cur.fetchall()
    for element in rows:
        print("serial = ", element[0])
        print("name = ", element[1])
        print("surname = ", element[2])
elif(option=='4'):
    cur.execute("UPDATE colony SET NAME='Wayne', SURNAME='Enterprises' WHERE SERIAL=2")
    conn.commit()
    print("Data Updated", cur.rowcount)
elif(option=='5'):
    number_delete = int(input("Enter which entry to delete: "))
    cur.execute(f"DELETE FROM colony WHERE SERIAL={number_delete}")
    conn.commit()
    print("delete Successfull")
else:
    print("wrong input.")




conn.close()