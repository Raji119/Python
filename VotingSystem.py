class VotingSystem(Exception):
 def __init__(self,name,id,age):
  self.name = name
  self.id   = id
  self.age  = age

try:
 name = input("Enter Name:")
 id   = int(input("Enter Id:"))
 age  = int(input("Enter Age:"))
 if age < 18:
  raise VotingSystem
 voter = VotingSystem(name,id,age)
 print("You Are Eligible to Vote")
except Exception as e:
 print("Sorry You Are Not Eligible to Vote")
