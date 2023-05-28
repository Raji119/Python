import mysql.connector

class Emp_DB:

 def __init__(self):
  self.con = mysql.connector.connect(user="root",passwd="root",host="localhost",database="emp",auth_plugin="mysql_native_password")
  self.cur = self.con.cursor()

 def read(self,name,age):
  ins = "INSERT INTO emp1(name,age) VALUES( %s,%s)"
  val = (name,age)
  self.cur.execute(ins,val)
  self.con.commit()

 def display(self):
  sel  = "SELECT * FROM emp1"
  self.cur.execute(sel)
  rows = self.cur.fetchall()
  for i in rows:
   print(i)

 def update(self,name1,name2):
  upd="UPDATE emp1 SET name=%s WHERE name=%s"
  val=(name2,name1)
  self.cur.execute(upd,val)
  self.con.commit()

 def delete(self,name):
  d="DELETE FROM emp1 WHERE name=%s"
  val=(name,)
  self.cur.execute(d,val)
  self.con.commit()

obj=Emp_DB()
while True:
  print("1.Insert \n2.Display \n3.Update \n4.Delete")
  ch=int(input("Enter Your Choice:"))
  if ch==1:
    name=input("Enter Name:")
    age =int(input("Enter Age:"))
    obj.read(name,age)
  elif ch==2:
    obj.display()
  elif ch==3:
    name1=input("Enter Name to be Updated:")
    name2=input("Enter Name:")
    obj.update(name1,name2)
  elif ch==4:
    name= input("Enter Name to be Deleted:")
    obj.delete(name)
  else:
   exit()


