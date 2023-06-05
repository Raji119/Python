class A:
 def __init__(self):
  print("A")
  self.a=5
 def d(self):
  print(self.a)
class B:
 def __init__(self):
  print("B")
  self.a=6
 def d(self):
  print(self.a)
class C(A,B):
 def __init__(self):
  self.a=7
  
 def d(self):
  print("HII")
  A().d()
  B().d()
  print(self.a)

obj=C()
obj.d()
