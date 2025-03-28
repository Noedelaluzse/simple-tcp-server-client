import socket 
import threading

HOST = '127.0.0.1' # Localhost
PORT = 5001 # Cambiar el puerto 5000

def start_server():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen()
    print(f"Server listening on {HOST}:{PORT}")
    while True:
      connection, address = server.accept()
      client_thread = threading.Thread(target=server, args=(connection, address))
      client_thread.start()

if __name__ == "__main__":
  start_server()
