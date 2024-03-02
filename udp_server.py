import socket

server_host = '127.0.0.1'
server_port = 9997  # Ensure this matches the port your client is targeting

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((server_host, server_port))

print(f"UDP server listening on {server_host}:{server_port}")

while True:
    data, addr = server.recvfrom(4096)
    print(f"Received message: {data} from {addr}")
    # Optionally, send a response back to the client
    server.sendto(b"ACK", addr)