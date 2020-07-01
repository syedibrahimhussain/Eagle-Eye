import mysql.connector


def mysql_connect():
 mydb = mysql.connector.connect(host="localhost", user="root", passwd="root786")
 if (mydb):
  return 1
 else:
  return -1

def mysql_cdb():
 mydb = mysql.connector.connect(host="localhost", user="root", passwd="root786")
 my_cursor=mydb.cursor()
 my_cursor.execute("CREATE DATABASE NPDATABASE")

def mysql_ctb():
 mydb = mysql.connector.connect(host="localhost", user="root", passwd="root786", database="NPDATABASE")
 my_cursor=mydb.cursor()
 my_cursor.execute("CREATE TABLE USERDATA(NP VARCHAR(250), NAME VARCHAR(250))")

def mysql_enterdata(np, name):
 mydb = mysql.connector.connect(host="localhost", user="root", passwd="root786", database="NPDATABASE")
 my_cursor=mydb.cursor()
 v1 = (np, name)
 query="INSERT INTO  USERDATA VALUES(%s,%s)"
 my_cursor.execute(query, v1)
 mydb.commit()


def mysql_searchdata(np):
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root786", database="NPDATABASE")
    mycursor = mydb.cursor()
    sqlq = "select * from USERDATA where np like %s"
    mycursor.execute(sqlq,(np,))
    result = mycursor.fetchone()
    if (result!=None):
        return(1)
    else:
        return(-1)

def mysql_display():
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="root786", database="NPDATABASE")
    mycursor = mydb.cursor()
    sql= "select * from USERDATA"
    mycursor.execute(sql)
    result = mycursor.fetchall()
    for r in result:
        print("no plate :" + str(r[0]))
        print("name :" + str(r[1]))
        #print("address:" + str(r[2]))
        print("-----------------")


