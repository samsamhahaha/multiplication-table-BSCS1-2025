import calendar

while True:
 year = int(input("enter ur desired year: "))
 print(calendar.calendar(year))

 again = input("Again? yes/no: ")
 if again.lower() == "n":
  break