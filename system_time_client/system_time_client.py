import socket

def my_client():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345

    s.connect((host, port))
    print ("client")
    print (s.recv(1024))
    s.close

my_client()

