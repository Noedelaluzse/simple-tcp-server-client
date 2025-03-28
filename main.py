from client import start_client
from serverApp import start_server
import threading
import time

def main():
    print("Iniciando servidor en segundo plano...")
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()

    # Espera opcional para dar tiempo a que el servidor arranque
    time.sleep(1)

    print("Iniciando cliente...")
    start_client()

if __name__ == "__main__":
    main()