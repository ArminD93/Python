import calendar  #import modułu kalendarza


rok =[2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020]  #Utworzenie tablicy


def kalendarz(): 
    cal = calendar.month(2017, 12)  #Pobiera rok 2017 i miesiąc 12 (Grudzień)
    print ("To jest kalendarz: ") #Wyświetlenie tekstu
    print (cal) #Wyświetlenie zawrtości zmiennej cal, czyli wyświetnie miesiąca Grdzień 2017


for i in rok: #Dla każdego elementu w tablicy rok wykonaj poniższe instrukcje
    if(calendar.isleap(i)): #sprawdza, czy rok jest przestępny
        print(i, "rok przestepny")
    else:
        print(i, "rok zwykły")

print() 
kalendarz()