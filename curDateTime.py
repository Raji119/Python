from datetime import date,datetime

today = date.today()

print("Today is:",today)
print("dd/mm/yyyy:",today.strftime("%d/%m/%Y"))
print("Textual Month,date and year:",today.strftime("%B %d ,%Y"))
print("Month-dd-yyy:",today.strftime("%b-%d-%Y"))

now = datetime.now()
print("Now:",now)
print("Date and Time is:",now.strftime("%d/%m/%Y %H:%M:%S"))
