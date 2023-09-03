while True:

 print("1.+ \n2.- \n3.* \n4./ \n5.Exit")
 ch=int(input("Enter your Choice:"))

 if(ch==5):
  exit()

 a=int(input("Enter a Number:"))
 b=int(input("Enter a Number:"))

 if ch==1:
  print(a+b)
 elif ch==2:
  print(a-b)
 elif ch==3:
  print(a*b)
 elif ch==4:
  print(a/b)
