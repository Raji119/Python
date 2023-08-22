n=int(input("Enter a Number:"))

c=b=n
res=count=0

while(b>0):
 b//=10
 count+=1

while(c>0):
 mod=c%10
 res+=mod**count
 c//=10

if(res==n):
 print("Armstrong")
else:
 print("Not Armstrong")
