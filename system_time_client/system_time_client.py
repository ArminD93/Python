import socket

def my_client():
    s = socket.socket() #Utworzenie gniazda sieciowego
    host = socket.gethostname() #pobranie adresu hosta lokalnego
    port = 12345 # Przypisanie portu do zmiennej

    s.connect((host, port)) #Nawiązanie połączenia
    print ("client")
    print (s.recv(1024)) #odbiór danych (max 1024 bajty)
    s.close()

my_client()

