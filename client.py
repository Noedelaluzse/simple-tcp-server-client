import socket

HOST = '127.0.0.1'  # Localhost
PORT = 5001  # Cambiar el puerto 5000

def start_client():
  with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    print(f"Connected to server at {HOST}:{PORT}. Write your message (DESCONEXION to leave): " )
    while True:
      message = input("> ").upper()
      "No se puede enviar un mensaje vacio"
      client.sendall(message.encode('utf-8'))
      
      # No empty message are allowed
      if message == "":
        print("No se puede enviar un mensaje vacio")
        continue
      elif message == "DESCONEXION":
        print("Closing connection...")
        break
      else:
        data = client.recv(1024)
        print(f"Received from server: {data.decode('utf-8')}")
  client.close()
  print("Connection closed.")
