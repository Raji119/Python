n=int(input("Enter a Number:"))

if n>0:
 print("The Fibonnaci Series:")
 f0,f1=0,1
 if(n>=1):
  print(f0)
 if(n>=2):
  print(f1)
 for i in range(2,n):
  f2=f0+f1
  f0=f1
  f1=f2
  print(f2)
else:
 print("Invalid Input...")  
