class Parent:
 def property(self):
  print("This is Parent Property")
class Child(Parent):
 def property(self):
  super().property()
  print("This is Child Property")
obj=Child()
obj.property()
