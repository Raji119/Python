n=int(input("Enter a Number:"))
for i in range(n+1):
 for k in range(n-i+1):
  print(end=" ")
 for j in range(i):
  print("*",end=" ")
 print()
for i in range(n+1):
 for k in range(i+2):
  print(end=" ")
 for j in range(n-i-1):
  print("*",end=" ")
 print()
