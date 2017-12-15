import os #import modułu
 
rootDir = input('Podaj ścieżkę do katalogu: ') #Podanie ścieżki
print() #zrobienie odstępu
for dirName, subdirList, fileList in os.walk(rootDir): #Wykonanie pętli for po ścieżce
    print('%s' % dirName) #Wyświtlenie ścieżki
    for fname in fileList: #Za pomocą tego for'a można wyświetlić pliki znajdujące się w danej ścieżce
        print('\t%s' % fname) #Wyświetlenie plików
