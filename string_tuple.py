#Python Script to Perform 10 Operations on Strings and Tuples
while True:
 print("====Main Menu===")
 print(" 1.String \n 2.Tuple \n 3.Exit")
 print("================")
 ch = int(input("Enter Your Choice:")) 
 if ch==1:
  str = input("Enter String:")
  while True:
   print("\nString Operations")
   print("=================")
   print(" 1.Length \n 2.UpperCase \n 3.LowerCase \n 4.Title \n 5.Reverse \n 6.SwapCase \n 7.Count \n 8.Find \n 9.Concatenation \n 10.Replace \n 11.StartsWith \n 12.EndsWith \n 13.Join \n 14.Strip \n 15.Isalpha \n 16.Exit")
   print("=================")
   sch = int(input("Enter Your Choice:")) 
   print()
   if sch==1:
    print(len(str))
   elif sch==2:
    print(str.upper())
   elif sch==3:
    print(str.lower())
   elif sch==4:
    print(str.title())
   elif sch==5:
    print(str[::-1])
   elif sch==6:
    print(str.swapcase())
   elif sch==7:
    txt = input("Enter an Character to Count:")
    print(str.count(txt))
   elif sch==8:
    txt = input("Enter a Text:")
    fnd = str.find(txt)
    if fnd!=-1:
     print("Pos = ",fnd)
    else:
     print("Not Found")
   elif sch==9:
    txt = input("Enter a Text:")
    print(str+txt)
   elif sch==10:
    txt1 = input("Enter Text to be Replaced:")
    txt2 = input("Enter New Text:")
    fnd  = str.find(txt1)
    if fnd!=-1:
      print(str.replace(txt1,txt2))
    else:
     print(txt1,"Not Found in",str)
   elif sch==11:
     inp = input("Enter a String:")
     if str.startswith(inp):
        print(str,"Starts With",inp)
     else:
        print(str,"Does Not Starts With",inp)
   elif sch==12:
     inp = input("Enter a String:")
     if str.endswith(inp):
        print(str,"Ends With",inp)
     else:
        print(str,"Does Not Ends With",inp)
   elif sch==13:
     inp = input("Enter a Character to Join With:")
     print(inp.join(str))
   elif sch==14:
     print(str.strip())
   elif sch==15:
     if str.isalpha():
       print("The String Contains only Alphabets")
     else:
       print("The String Contains Many More Symbols")
   elif sch==16:
     break
   else:
     print("Invalid Input...")
 if ch==2:
  tup = tuple(input("Enter Tuple:"))
  while True:
   print("\nTuple Operations")
   print("=================")
   print(" 1.Length \n 2.Max \n 3.Min \n 4.Repetition \n 5.Reverse \n 6.Sorted \n 7.Count \n 8.Index \n 9.Concatenation \n 10.Slicing \n 11.All \n 12.Any \n 13.Enumerate \n 14.Get Element By Index \n 15.Delete \n 16.Exit")
   print("=================")
   sch = int(input("Enter Your Choice:")) 
   print()
   if sch==1:
    print(len(tup))
   elif sch==2:
    print(max(tup))
   elif sch==3:
    print(min(tup))
   elif sch==4:
    n = int(input("Enter a Number:"))
    print(tup*n)
   elif sch==5:
    print(tup[::-1])
   elif sch==6:
    print(sorted(tup))
   elif sch==7:
    txt = input("Enter an Character to Count:")
    print(tup.count(txt))
   elif sch==8:
    txt = input("Enter a Character:")
    if txt in tup:
     fnd = tup.index(txt)
     print("Pos = ",fnd)
    else:
     print("Not Found")
   elif sch==9:
    tup2 = tuple(input("Enter a Text:"))
    print(tup+tup2)
   elif sch==10:
    start = int(input("Enter Starting Position:"))
    end   = int(input("Enter End Position:"))
    print(tup[start:end])
   elif sch==11:
      if all(tup):
        print("All Elements are True")
      else:
        print("Some Elements are Not True")
   elif sch==12:
      if any(tup):
        print("Atleast One Elements is True")
      else:
        print("ALl Elements are Not True")
   elif sch==13:
        y = enumerate(tup)
        print("Enumerated Tuple:",list(y))
   elif sch==14:
        try:
         ind = int(input("Enter Index:"))
         print(tup[ind])
        except:
         print("Invalid index")
   elif sch==15:
        del tup
   elif sch==16:
     break
   else:
     print("Invalid Input...")
 elif ch==3:
   exit()
 else:
   print("Invalid Input...")
