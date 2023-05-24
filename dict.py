d = dict()

class Emp:

 def read(self):
  self.name    = input("Enter Employee Name:")
  self.address = input("Enter Address:")
  self.PAN     = input("Enter PAN:")
  self.basic   = int(input("Enter Basic Salary:"))
  self.TDS     = int(input("Enter TDS:"))
  self.deduct  = int(input("Enter Deduction:"))
  self.HRA     = 1.25 * self.basic
  self.DA      = 0.25 * self.basic
  self.grossSal= self.basic + self.HRA + self.DA
  self.netSal  = self.grossSal - self.deduct
  self.update()

 def update(self):
  d.update({self.name : {"name":self.name,"address":self.address,"PAN":self.PAN,"basic":self.basic,
  "TDS":self.TDS,"detuct":self.deduct,"HRA":self.HRA,"DA":self.DA,"grossSal":self.grossSal,"netSal":self.netSal}})

 def search(self,name):
  flag=0
  for key in d:
   if key==name:
    print("Employee Found\n")
    for i in d[key]:
     print(i,d[key][i])
    flag=1
  if flag==0:
   print("Employee Not Found\n")  

 def printEmp(self):
  if(len(d)==0):
   print("No Employees Found\n")
  else: 
   for key in d:
    print(key)
   print()

class Emps(Emp):
 emp = Emp()
 while True:
  ch=int(input(" 1.Add Employee \n 2.Print Employees \n 3.Find An Employee by Name \n 4.Exit \n Enter Your Choice:"))
  if ch==1:
   emp.read()
  elif ch==2:
   emp.printEmp()
  elif ch==3:
   name=input("Enter the Employee Name:")
   emp.search(name)
  elif ch==4:
   exit()
  else:
   print("Invalid Input")

