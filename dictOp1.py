d={}
while True:
 print("Dictionary Operations")
 print(" 1.Add \n 2.Update Name \n 3.Get Item \n 4. View Keys \n 5.View Values")
 ch=int(input("Enter your Choice:")) 
 if ch==1:
  id   = int(input("Enter Id:"))
  name = input("Enter Name:")
  age  = int(input("Enter Age:"))
  d.update({id:{"name":name,"age":age}})
  print(d[id])
 elif ch==2:
  try:
   id   = int(input("Enter Id:"))
   name = input("Enter Updated Name:")
   d[id]["name"]=name
   print(d[id])
  except:
   print("Invalid Input")
 elif ch==3:
  id  = int(input("Enter Id:"))
  print(d[id])
 elif ch==4:
  print(d.keys())
 elif ch==5:
  print(d.values())
 else:
  exit()
