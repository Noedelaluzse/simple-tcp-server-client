def server(connection, address):
  print(f"New connection from {address}")
  while True:
    try:
      data = connection.recv(1024)
      if not data:
        break
      message = data.dacode('utf-8').strip()
      print(f"Received message from {address}: {message}")
      message = message.upper()
      if message == "DESCONEXION":
        print(f"Cliente {address} desconectado")
        break
      else:
        print(f"Enviando mensaje: {message}")
        connection.sendall(message.encode('utf-8'))
    except Exception as e:
      print(f"Error: {e}")
      break
  connection.close()
  print(f"Connection closed from {address}")
