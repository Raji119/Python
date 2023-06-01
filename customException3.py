class Error(Exception):
 pass

class ZeroDivision(Error):
 pass

try:
 i=int(input("Enter a Number:"))
 if i==0:
  raise ZeroDivision
except ZeroDivision:
 print("Enter Greater Than Zero")
