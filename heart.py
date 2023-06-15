n=int(input("Enter a Number:"))
for i in range(n+1):
 for k in range(n-i+1):
  print(end=" ")
 for j in range(i):
  print("*",end=" ")
 for k in range(n-i):
  print(" ",end=" ")
 for j in range(i):
  print("*",end=" ")
 print()

for i in range(2*n+1):
 for k in range(i+2):
  print(end=" ")
 for j in range(2*n-i-1):
  print("*",end=" ")
 print()
