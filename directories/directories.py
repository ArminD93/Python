def katalogi():
    import os, os.path #Import potrzebnych modułów
    dirtocheck = input('Podaj ścieżkę do katalogu: ') #Prosi podanie ścieżki przez użytkownika
    print() #odstęp

    for root, _, files in os.walk(dirtocheck): #Wykoanie pętli for po podanej wcześniej ścieżce
        for f in files: #wykonanie for'a po każdym pliku
            fullpath = os.path.join(root, f) #Przypisanie do zmiennej fullpath, konstrukcja ścieżki 
            if os.path.getsize(fullpath) < 2* 1024 * 1024: #mniej niż 2MB
                print (fullpath) #Wyświetlenie zawartości zmiennej fullpath


katalogi() #Wywołanie funckji