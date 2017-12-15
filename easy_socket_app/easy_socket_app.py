def socket_app(): #definicja funkcji
    import socket #import modułu sieciowegoo
    s = socket.socket() # Tworzenie gniazda sieciowego - Metoda socket() zwraca obiekt socket, 
                        #na którym można wykonać takie metody jak connect czy send, bind
    s.connect(('172.217.9.131',80)) #nawiązanie połączenia
    s.send(b'GET / HTTP/1.0\n\n') #Wysłanie danych
    print (s.recv(200)) #odbior danych (max 200 bajtów)


socket_app() #Wywołanie funkcji
