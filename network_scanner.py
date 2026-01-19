import socket

def scan(target):
    print(f"Scanning {target}...")
    for port in [80, 443, 21, 22]:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
        s.close()

scan("google.com")  
