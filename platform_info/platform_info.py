#informacje o platformie, na której uruchomiony jest ten skrypt

def main():
    import platform
    profile = [
        platform.architecture(),
        platform.dist(),
        platform.libc_ver(),
        platform.mac_ver(),
        platform.machine(),
        platform.node(),
        platform.platform(),
        platform.processor(),
        platform.python_build(),
        platform.python_compiler(),
        platform.python_version(),
        platform.system(),
        platform.uname(),
        platform.version(),
        ]
    for i in profile:
        print(i)
if __name__ == '__main__':
    main()