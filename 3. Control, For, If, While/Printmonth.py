def input_check():
    month = input("Select a month: ")
    month = month.lower()

    day = input("Select a starting day: ")
    day = day.lower()

    week_day = {"monday":0, "tuesday":1, "wednesday":2, "thursday":3, "friday":4, "saturday":5, "sunday":6}
    
    months = {"january":31, "february":28, "march":31, "april":30,
              "may":31, "june":30, "july":31, "august":31,
              "september":30, "october":31, "november":30, "december":31}

    if month in months:
        n = months.get(month)

    else:
        input_check() 

    #for days in week_day:
    #    print ("{:>3}".format(days[:2].title()), end = " ")
    print(" Mo  Tu  We  Th  Fr  Sa  Su ")

    print (week_day[day]*4*" ", end="")
    
    for number in range(1,n+1):
        print ("{:>3}".format(number), end =" ")

        if (week_day[day] + number) % 7 == 0:
            print()
        

input_check()
