'''
Created on 20. jan. 2011

@author: Ketil
'''


from time import clock

def weekDay(day,month,year,day1=1,month1=1,year1=1900,weekday=1,leapYear=False):
    daysInMonth =     [31,28,31,30,31,30,31,31,30,31,30,31]
    daysInMonthLeap = [31,29,31,30,31,30,31,31,30,31,30,31]
    counter=0
    while year1<year+1:
        if year1%4==0 and year1!=1900:
            leapYear=True
        else:
            leapYear=False
        month1=1
        while month1<13:
            day1=1
            if leapYear!=True:
                while day1<daysInMonth[month1-1]+1:
                    if day1==1 and weekday==7:
                        print [weekday,day1,month1,year1]
                        counter+=1
                    if day1==day and month1==month and year1==year:
                        print counter
                        return weekday
                    day1+=1
                    weekday+=1
                    if weekday==8:
                        weekday=1
            else:
                while day1<daysInMonthLeap[month1-1]+1:
                    if day1==1 and weekday==7:
                        print [weekday,day1,month1,year1]
                        counter+=1
                    if day1==day and month1==month and year1==year:
                        print counter
                        return weekday
                    day1+=1
                    weekday+=1
                    if weekday==8:
                        weekday=1
            month1+=1
#            print [year1,month1,day1,weekday]
        year1+=1
    return weekday
    


def numberOfSundays():
    print weekDay(31,12,2000)
    return 0


def main():
    clock()
    foo= numberOfSundays()
    print foo
    print clock()
if __name__ == '__main__':
    main()