def log_to_ssh():
    import paramiko #moduł odpowiadający za łączność ssh
    import re  #moduł odpowiadający za wyrażenia regularne
    import getpass #moduł odpowiadający za szyfrowanie

    hostname = input('Podaj adress IP: ' ) #Prosi użytkownia o podanie IP
    port = 22
    username = input('Podaj nazwę użytkownika: ' ) #podanie nazwy użytkownika
    password = getpass.getpass('Podaj hasło: ' ) #Podanie hasła, hasło będzie niewidoczne na ekranie
                                                 #takie zabezpieczenie by nikt niewidział

    print() #Zrobienie odstępu

    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient() #Wykonanie metody SSHClient
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #załadowanie uprawnień,polityki
    s.load_system_host_keys() 
    
    s.connect(hostname, port, username, password) #Nawiązanie połączenia
    stdin, stdout, stderr = s.exec_command('ls' ) #przkazanie polecenia do debiana
    

    a = stdout.readlines() #Czytaj linie
    
    linia = re.sub(r'\\n', '', str(a)) #Wyrażenie regularne utworzone w celu pozbycia się \n
   
    print (linia)
    s.close()   


log_to_ssh()

