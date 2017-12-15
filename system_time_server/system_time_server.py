import socket
import time 

def my_server():
    s = socket.socket() #Utworzenie gniazda sieciowego
    host = socket.gethostname() #pobranie adresu hosta lokalnego
    port = 12345 # Przypisanie portu do zmiennej
    s.bind((host, port)) #dowiązanie do hosta i portu
    s.listen(5) #Nasłuchiwanie, czeka na połączenie klienta
    print ("server") #tekst
    while True:
        c, addr = s.accept() #zakceptowanie połącznia od klienta
        print ("Połączyłem się z '", addr) #Podanie adresu klienta
        czas = time.ctime() #Przypisanie do zmiennej czasu systemowego

        c.send(czas.encode('utf-8')) #Wysłanie sendu do klienta
        c.close() #koniec połączenia


my_server() #Wywołanie funkcji

