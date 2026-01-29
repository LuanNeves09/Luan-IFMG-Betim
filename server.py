"""
 Implements a simple HTTP/1.0 Server
 Modified to support binary files (images) and MIME Types
"""

import socket


# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000
BASE_DIR = 'htdocs'

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)
print(f'🚀 Listening on port {SERVER_PORT} ...')

while True:    
    # Wait for client connections
    client_connection, client_address = server_socket.accept()

    # Get the client request
    try:
        request = client_connection.recv(1024).decode()
    except:
        continue # Ignore null conections

    if not request:
        continue

    # Parse HTTP headers
    headers = request.split('\n')
    # Get file name (e.g.: /index.html)
    filename = headers[0].split()[1]
    
    # Remove URL params, if have (e.g.: ?t=123)
    if '?' in filename:
        filename = filename.split('?')[0]

    # Routing to root
    if filename == '/':
        filename = '/index.html'

    # Full path to file
    filepath = BASE_DIR + filename

    try:
        # Open like 'rb' (Read Binary)
        # Need to images don't get corrupted
        fin = open(filepath, 'rb')
        content = fin.read()
        fin.close()

       # Set the correct Content-Type
       # This teaches the browser how to display the file
        response_header = 'HTTP/1.0 200 OK\n'
        
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            response_header += 'Content-Type: image/jpeg\n'
        elif filename.endswith('.html'):
            response_header += 'Content-Type: text/html\n'
        elif filename.endswith('.css'):
            response_header += 'Content-Type: text/css\n'
        elif filename.endswith('.js'):
            response_header += 'Content-Type: application/javascript\n'
        else:
            response_header += 'Content-Type: text/plain\n'

        response_header += '\n' # mandatory blank line between headers and content

        # Send Bytes
        # I encode the header into bytes and add it to the content (which is already in bytes)
        client_connection.sendall(response_header.encode() + content)
        print(f"✅ Enviado: {filename}")

    except FileNotFoundError:
        # Handling 404 Errors
        response = 'HTTP/1.0 404 NOT FOUND\n\n<h1>File Not Found</h1>'
        client_connection.sendall(response.encode())
        print(f"❌ Nao encontrado: {filename}")

    # FClose client connection
    client_connection.close()

# Close socket
server_socket.close()