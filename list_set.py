#Python Script to Perform 10 Operations on Lists and Sets
while True:
 print("====Main Menu===")
 print(" 1.List \n 2.Set \n 3.Exit")
 print("================")
 ch = int(input("Enter Your Choice:")) 
 if ch==1:
  l =list(input("Enter List:"))
  while True:
   print("\nList Operations")
   print("=================")
   print(" 1.Length \n 2.Max \n 3.Min \n 4.Sort \n 5.Reverse \n 6.Insert \n 7.Count \n 8.Index \n 9.Concatenation \n 10.Remove \n 11.Append \n 12.Clear \n 13.Enumerate \n 14.Copy \n 15.Delete \n 16.Exit")
   print("=================")
   sch = int(input("Enter Your Choice:")) 
   print()
   if sch==1:
    print(len(l))
   elif sch==2:
    print(max(l))
   elif sch==3:
    print(min(l))
   elif sch==4:
    print(sorted(l))
   elif sch==5:
    print(l[::-1])
   elif sch==6:
    pos = int(input("Enter Position:"))
    ele = input("Enter an Element:")
    if(pos>0 and pos<=len(l)):
      l.insert(pos,ele)
      print(l)
    else:
      print("Invalid Position")
   elif sch==7:
    txt = input("Enter an Character to Count:")
    print(l.count(txt))
   elif sch==8:
    txt = input("Enter a Text:")
    if txt in l:
     fnd = l.index(txt)
     print("Pos = ",fnd)
    else:
     print("Not Found")
   elif sch==9:
    l2 =list(input("Enter a List:"))
    print(l+l2)
   elif sch==10:
    rm = input("Enter an Element:")
    if rm in l:
      l.remove(rm)
      print(l)
    else:
     print(rm,"Not Found in",l)
   elif sch==11:
    ele = input("Enter Element to be Appended:")
    l.append(ele)
    print(l)
   elif sch==12:
    l.clear()
   elif sch==13:
    y = enumerate(l)
    print(list(y))
   elif sch==14:
    x = l.copy()
    print(x)
   elif sch==15:
    del l
   elif sch==16:
     break
   else:
     print("Invalid Input...")
 if ch==2:
  s = set(input("Enter Set:"))
  while True:
   print("\nSet Operations")
   print("=================")
   print(" 1.Length \n 2.Add  \n 3.Pop \n 4.Equivalent \n 5.Subset \n 6.Superset \n 7.Union \n 8.Intersection \n 9.Set Difference \n 10.Symmetric Difference \n 11.SizeOf \n 12.Contains \n 13.clear \n 14.Delete \n 15.Update \n 16.Exit")
   print("=================")
   sch = int(input("Enter Your Choice:")) 
   print()
   if sch==1:
    print(len(s))
   elif sch==2:
    ele = input("Enter an Element:")
    s.add(ele)
    print(s)
   elif sch==3:
    print("Removed Element",s.pop())
    print("After Removing an Element",s)
   elif sch==4:
     s1 = set(input("Enter Set:"))
     if s==s1:
       print("Equivalent")
     else: 
       print("Not Equivalent")
   elif sch==5:
      s1 = set(input("Enter Set:"))
      if s<=s1:
       print(s,"is Subset of",s1)
      else:
       print(s,"is not Subset of",s1)
   elif sch==6:
    s1 = set(input("Enter Set:"))
    if s>=s1:
       print(s,"is Superset of",s1)
    else:
       print(s,"is not Superset of",s1)
   elif sch==7:
     s1 = set(input("Enter Set:"))
     print("Union=",s|s1)
   elif sch==8:
     s1 = set(input("Enter Set:"))
     print("Intersection=",s&s1)
   elif sch==9:
     s1 = set(input("Enter Set:"))
     print("Set Difference(s1-s2)=",s-s1)
     print("Set Difference(s2-s1)=",s1-s)
   elif sch==10:
     s1 = set(input("Enter Set:"))
     print("Symmetric Difference=",s^s1)
   elif sch==11:
     print(s.__sizeof__())
   elif sch==12:
    ele = input("Enter Element to Check:")
    if s.__contains__(ele):
      print("Element Found")
    else:
      print("Element Not Found")
   elif sch==13:
     s.clear()
   elif sch==14:
     del s
   elif sch==15:
     s.update([5,6,7])
     print(s)
   elif sch==16:
     break
   else:
     print("Invalid Input...")
 elif ch==3:
   exit()
 else:
   print("Invalid Input...")
