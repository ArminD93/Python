import calendar


rok =[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]


def kalendarz():
    cal = calendar.month(2017, 12)
    print ("To jest kalendarz: ")
    print (cal)


for i in rok:
    if(calendar.isleap(i)):
        print(i, "rok przestepny")
    else:
        print(i, "rok zwykły")

print()
kalendarz()