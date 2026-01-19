"""
 Implements a simple HTTP/1.0 Server
 Modificado para suportar arquivos binários (imagens) e MIME Types
"""

import socket


# Define socket host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000
BASE_DIR = 'htdocs' # Pasta onde ficam os arquivos do site

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
        continue # Ignora conexões vazias ou erros de decodificação

    if not request:
        continue

    # Parse HTTP headers
    headers = request.split('\n')
    # Pega o nome do arquivo (ex: /index.html)
    filename = headers[0].split()[1]
    
    # Remove parametros de URL se houver (ex: ?t=123)
    if '?' in filename:
        filename = filename.split('?')[0]

    # Roteamento para a raiz
    if filename == '/':
        filename = '/index.html'

    # Caminho completo do arquivo
    filepath = BASE_DIR + filename

    try:
        # Abrir como 'rb' (Leitura Binária)
        # Necessario para imagens nao corromperem
        fin = open(filepath, 'rb')
        content = fin.read()
        fin.close()

        # Definir o Content-Type correto
        # Isso ensina o navegador como exibir o arquivo
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

        response_header += '\n' # Linha em branco obrigatória

        # Enviar Bytes
        # Codifico o cabeçalho para bytes e somamos com o conteúdo (que já é bytes)
        client_connection.sendall(response_header.encode() + content)
        print(f"✅ Enviado: {filename}")

    except FileNotFoundError:
        # Tratamento de erro 404
        response = 'HTTP/1.0 404 NOT FOUND\n\n<h1>File Not Found</h1>'
        client_connection.sendall(response.encode())
        print(f"❌ Nao encontrado: {filename}")

    # Fecha conexão
    client_connection.close()

# Close socket
server_socket.close()