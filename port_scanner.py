import socket

def scan(target, ports):
    print(f"Scanning {target} for open ports")

    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # (ipv4, tcp connection). Open socket
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()

target_ip = input("Enter ip address or domain: ")
ports = input("Enter ports to scan, comma-separated (e.g 3,66,77,43): ")

try:
    ports = [int(port.strip()) for port in ports.split(",")]
        if not all(1 <= p <= 65535 for p in ports):
        print("Error: Ports must be between 1 and 65535.")
        exit(1)
except ValueError:
    print("Error: Please enter valid integers for ports.")
    exit(1)

# Run scanner
scan(target_ip, ports)

    