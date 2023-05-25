from magicMethods import *

obj1 = Calc()
obj2 = Calc()

obj1.data()
obj2.data()

while True:
        print("1. Bitwise AND \n2. Bitwise OR \n3. Greater Than \n4. Less Than \n5. XOR")
        ch = int(input("Enter your choice: "))
        if ch == 1:
                obj1 & obj2
        elif ch == 2:
                obj1 | obj2
        elif ch == 3:
                obj1 > obj2
        elif ch == 4:
                obj1 < obj2
        elif ch == 5:
                obj1 ^ obj2
        else:
                print ("Invalid Input")
                exit()

