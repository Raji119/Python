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
  print("This is Child's Property")

class GrandChild(Child):
 def property(self):
  Child().property()
  print("This is GrandChild's Property")

obj1=GrandChild()
obj1.property()


