import socket
import time 

def my_server():
    s = socket.socket()
    host = socket.gethostname()
    port = 12345
    s.bind((host, port))
    s.listen(5)
    print ("server")
    while True:
        c, addr = s.accept()
        print ("Połączyłem się z '", addr)
        czas = time.ctime()

        c.send(czas.encode('utf-8'))
        c.close()


my_server()

