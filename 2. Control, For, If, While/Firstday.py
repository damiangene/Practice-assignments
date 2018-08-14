year1= int(input("What is the first year?"))
year2= int(input("What is the second year?"))

for year in range(year1,year2+1):
    
    #day = R(1 + 5R(Year − 1, 4) + 4R(Year − 1, 100) + 6R(Year − 1, 400), 7)
    day6 = 6*((year - 1)%400)
    #print (day6)

    day4 = 4*((year - 1)%100)
    #print (day4)

    day5 = 5*((year - 1)%4)
    #print (day5) 

    day = (day5 + day6 + day4 +1)%7
    if day == 0:
        print ("%s starts on a Sunday" % (year))
    
    if day == 1:
        print ("%s starts on a Monday" % (year))
   
    if day == 2:
        print ("%s starts on a Tuesday" % (year))
   
    if day == 3:
        print ("%s starts on a Wednesday" % (year))
   
    if day == 4:
        print ("%s starts on a Thursday" % (year))
   
    if day == 5:
        print ("%s starts on a Friday" % (year))
   
    if day == 6:
        print ("%s starts on a Saturday" % (year))
    
    