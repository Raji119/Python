n=int(input("Enter a Number:"))

if(n>=0):
 fact=1
 for i in range(2,n+1):
  fact*=i
 print(fact)
else:
 print("Invalid Input")
