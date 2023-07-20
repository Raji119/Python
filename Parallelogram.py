n=int(input("Enter a Number:"))

for i in range(0,n+1):
 for j in range(i,n):
  print(end=" ")
  k=j
 while(k>=0):
  print("*",end="")
  k=k-1
 print()
