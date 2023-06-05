import socket

def calcRedundantBits(inp_data):
 length = len(inp_data)
 for i in range(length):
  if(2**i >= length+i+1):
   return i

def posRedundantBits(inp_data,r):
 j      = 0
 k      = 1
 res    = ""
 length = len(inp_data)
 for i in range(1,length+r+1):
  if(i == 2**j):
   res = res +'0'
   j  += 1
  else:
   res = res + inp_data[-1 * k]
   k  += 1
 return res[::-1]

def calcParityBits(inp_data,r):
 length = len(inp_data)
 for i in range(r):
  val = 0
  for j in range(1,length+1):
   if(j & (2**i) == (2**i)):
    val = val ^ int(inp_data[-1 * j])
  res = inp_data[:length-(2**i)]+ str(val) + inp_data[length-(2**i) + 1:]
  inp_data = res
 return res

def read():
 inp_data = input("\nEnter Data to be Transmitted:")
 r        = calcRedundantBits(inp_data)
 pos      = posRedundantBits(inp_data,r)
 data     = calcParityBits(pos,r)
 print("Data Transmitted is:",data)
 sentData=input("Enter Data to be Recieved:")
 return sentData

s = socket.socket()
print ("Socket successfully created")

port = 9999
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

s.bind((ip, port))
print ("socket binded to %s" %(port))

s.listen(5)
print ("socket is listening")


c, addr = s.accept()
print ('Got connection from', addr )
while True:
 inp = c.recv(1024).decode()
 if(inp=="n" or inp=="N"):
  c.close()
  break
 elif(inp=="Y" or inp=="y"):
  sentData=read()
  c.send(sentData.encode())


