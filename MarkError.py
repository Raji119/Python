class MarkError(Exception):
 pass

class InvalidMarkError(MarkError):
 def __init__(self):
  super().__init__("Mark is Invalid")

class LessMarkError(MarkError):
 def __init__(self):
  super().__init__("Mark is Lesser Than Minimum Mark")

class CheckMark(MarkError):
 def __init__(self,per):
  if per<60:
   raise LessMarkError
  elif per>100:
   raise InvalidMarkError
  print("Congrats You Are Selected..")

try:
 per = int(input("Enter Mark:"))
 CheckMark(per)
except Exception as e:
 print(e)
