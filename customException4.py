class Error(Exception):
 pass

class TransitionError(Error):
 def __init__(self,prev,nex,msg):
  self.prev = prev
  self.next = next
  self.msg  = msg

try:
 raise TransitionError(2,3*2,"Not Allowed")
except TransitionError as error:
 print("Exception Occurred:",error.msg) 
