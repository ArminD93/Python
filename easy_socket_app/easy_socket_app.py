def socket_app():
    import socket
    s = socket.socket()
    s.connect(('172.217.9.131',80))
    s.send(b'GET / HTTP/1.0\n\n')
    print (s.recv(200))


socket_app()
