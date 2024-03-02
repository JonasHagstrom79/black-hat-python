from datetime import datetime
import os
import socket
import ssl

target_host = "www.google.com"
target_port = 443  # HTTPS uses port 443

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Wrap the socket using SSL for HTTPS
client = ssl.wrap_socket(client, keyfile=None, certfile=None, server_side=False, cert_reqs=ssl.CERT_NONE, ssl_version=ssl.PROTOCOL_SSLv23)

# Connect the client
client.connect((target_host, target_port))

# Send some data (Note: We need to use \r\n\r\n at the end of the request header)
request = "GET / HTTP/1.1\r\nHost: {}\r\nConnection: close\r\n\r\n".format(target_host)
client.send(request.encode())

# Receive some data
response = b""
while True:
    part = client.recv(4096)
    if not part:
        break
    response += part

print(response.decode(errors='ignore'))

# Assuming 'response' is your variable that holds the HTTP response data
response_data = response.decode(errors='ignore')

# Get the current date and time
current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Define the directory and filename with the current date and time
directory = "response"
filename = f"response_{current_datetime}.html"
filepath = os.path.join(directory, filename)

# Check if the directory exists, and create it if it doesn't
if not os.path.exists(directory):
    os.makedirs(directory)

# Write the response data to the file in the specified directory
with open(filepath, 'w', encoding='utf-8') as file:
    file.write(response_data)

print(f"Response saved to {filepath}")

client.close()