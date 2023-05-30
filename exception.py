while True:
	print("1.check value Error")
	print("2.check File not found Error")
	print("3.check Type Error")
	print("4.check IO Error")
	print("5.check Name Error")
	print("0.exit")
	n=int(input("enter your choice"))
	if n==1:
		try:
			f=open('f.txt','z')
			print("successful")
		except ValueError:
			print("Value Error")
	elif n==2:
		try:
			f=open('f9.txt','r')
			print("successful")
		except FileNotFoundError:
			print("file not Found Error")
	elif n==3:
		try:
			f=open('f.txt','r',"w")
			print("successful")
		except TypeError:
			print("Type Error")
	elif n==4:
		try:
			f=open('f.txt','r')
			f.write("sample")
		except IOError:
			print("IOError")
	elif n==5:
		try:
			f=opens('f.txt','r')
			print("successful")
		except NameError:
			print("Name Error")
	elif n==0:
		break
	else:
		print("invalid input")
