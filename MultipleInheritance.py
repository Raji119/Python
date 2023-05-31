class Father:
 def property(self):
  print("This is Father's Property")

class Mother:
 def property(self):
  print("This is Mother's Property")

class Child(Father,Mother):
 def property(self):
  Father().property()
  Mother().property()
  print("This is Child1 Property")

obj=Child()
obj.property()
