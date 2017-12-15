def log_to_ssh():
    import paramiko
    import re
    import getpass

    hostname = input('Podaj adress IP: ' )
    port = 22
    username = input('Podaj nazwę użytkownika: ' )
    password = getpass.getpass('Podaj hasło: ' )

    print()

    paramiko.util.log_to_file('paramiko.log')
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    s.load_system_host_keys()
    
    s.connect(hostname, port, username, password)
    stdin, stdout, stderr = s.exec_command('ls' )
    #print (stdout.readlines())

    a = stdout.readlines()
    
    linia = re.sub(r'\\n', '', str(a))
    #print (linia)
    print (linia)
    s.close()   


log_to_ssh()

