def handle_client(connection, address):
  print(f"New connection from {address}")
  while True:
    try:
      data = connection.recv(1024)
      if not data:
        break
      message = data.decode('utf-8').strip()
      print(f"Received message from {address}: {message}")

      # SI el mensaje incluye un "HOLA" y "SERVIDOR", Cambiamos SERVIDOR por CLIENTE
      if "HOLA" in message and "SERVIDOR" in message:
        message = message.replace("SERVIDOR", "CLIENTE")
      message = message.upper()
      if message == "DESCONEXION":
        print(f"Cliente {address} desconectado")
        break
      else:
        connection.sendall(message.encode('utf-8'))
    except Exception as e:
      print(f"Error: {e}")
      break
  connection.close()
  print(f"Connection closed from {address}")
