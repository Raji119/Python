import time

def decorator(func):
 def wrapper():
  st=time.time()
  print("Start Time=",st)
  func()
  et=time.time()
  print("End Time=",et)
  d=et - st
  print("Total Time=",d)
 return wrapper

def fib():
 a,b=0,1
 while True:
  yield a
  a,b=b,a+b

@decorator
def display():
 f=fib()
 for i in range(n):
  print(next(f))

n=int(input("Enter n:"))
display()
