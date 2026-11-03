import socket

def scan(target, ports):
    print(f"Scanning {target} for open ports")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (ipv4, tcp connection)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

target_ip = input("Enter ip address or domain: ")
ports = input("Enter ports to scan, comma-separated (e.g 3,66,77,43): ")

try:
    