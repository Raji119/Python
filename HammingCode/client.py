import socket

def calcRedundantBits(inp_data):
 length = len(inp_data)
 for i in range(length):
  if(2**i >= length+i+1):
   return i


def detectError(data,r):
 length = len(data)
 res    = 0
 for i in range(r):
  val = 0
  for j in range(1,length+1):
   if(j & (2**i) == (2**i)):
    val = val ^ int(data[-1 * j])
  res = res + val*(10**i)
 return int(str(res),2)

s = socket.socket()
port = 9999
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)
s.connect((ip, port))

while True:
 inp=input("Do you want to Receive Data?Y/N:")
 s.send(inp.encode())
 if inp=="N" or inp=="n":
  s.close()
  break
 elif inp=="Y" or inp=="y":
  data=s.recv(1024).decode()
  print("Received Data:",data)
  r=calcRedundantBits(data)
  isCorrect=detectError(data,r)
  if(isCorrect == 0):
   print("No Error\n")
  else:
   print("The Position of Error is:",isCorrect,"From Right\n")
 else:
  print("Invalid Input")

