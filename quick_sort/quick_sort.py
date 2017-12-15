def quicksort(x):
    if len(x) == 0 or len(x) == 1: #Jeśli długość tabelki wynosi 0 lub jeden,
        return x  #to zwróć zawartość tej tabelki
    else:
        pivot = x[0] #Określenie pivotu jako pierwszego elementu tablicy - elementu podziałowego
        i = 0
        for j in range(len(x)-1): #wskaźnik j przegląda zbiór do przedostatniej pozycji
            if x[j+1] < pivot: #Jeśli wskaźnik jest mniejszy od pivotu, to wykonaj poniższą instr.
                x[j+1],x[i+1] = x[i+1], x[j+1]#określamy nowe miejsce pivota
                i += 1 #wskaźnik i, określający pozycję pivota przesuwamy o 1 pozycję
        x[0],x[i] = x[i],x[0] #przipisanie i-tego elementu do elementu zero

        first_part = quicksort(x[:i]) #Efekt sortowania lewej cześci tabelki wpisz do first_part 
        first_part.append(x[i]) #Dołącz element do końca tablicy
        second_part = quicksort(x[i+1:]) #Efekt sortowania prawej cześci tabelki wpisz do second_part

        return first_part + second_part #Zwróć wartość - połączenie zawartości z first_part i second_part

tabelka = [54,26,93,17,77,31,44,55,20]


print("Przed sortowaniem: ")
print(tabelka)
print()
print("Po posortowaniu: ")
print(quicksort(tabelka))