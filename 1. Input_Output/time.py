hours = int(input("Enter the hours:"))
minutes = int(input("Enter the minutes:"))
seconds = int(input("Enter the seconds:"))

if (hours <= 23 and hours >= 0 and 
    minutes <= 59 and minutes >= 0 and
    seconds <= 59 and seconds >= 0):
    print ("Your time is valid")

else:
    print ("Your time is invalid")

