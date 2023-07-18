n=int(input("Enter a Number:"))

for i in range(1,n+1):
 k=i
 for j in range(i,n):
  print(end=" ")
 while(k>0):
  print("*",end="")
  k=k-1
 print()
