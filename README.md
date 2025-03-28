## 🧪 Ejemplo de ejecución y uso

Al ejecutar el programa principal con `python main.py`, se inician automáticamente el **servidor** en segundo plano y el **cliente** en primer plano. A continuación, se muestra un ejemplo real de cómo funciona la interacción:
```bash
$ python main.py

---

## 📝 Explicación del flujo:

1. **Se inicia el servidor automáticamente** y se queda escuchando en `127.0.0.1:5000`.
2. El cliente se conecta al servidor y permite ingresar mensajes desde consola.
3. El usuario escribe: `Hola Servidor`.
   - El mensaje es enviado al servidor.
   - El servidor reemplaza `"SERVIDOR"` por `"CLIENTE"` y convierte el texto a mayúsculas.
   - Se recibe en el cliente: `HOLA CLIENTE`.
4. El usuario escribe: `DESCONEXION`.
   - El cliente envía el mensaje.
   - El servidor reconoce la palabra clave y cierra la conexión.
   - El cliente finaliza su ejecución.

---

## ✅ Resultado esperado

- El servidor **permanece activo** y puede aceptar nuevas conexiones.
- El cliente **se desconecta correctamente** cuando se envía `"DESCONEXION"`.
- Todos los mensajes normales son **respondidos en mayúsculas**, aplicando una lógica especial cuando se incluye la palabra `"SERVIDOR"` (reemplazándola por `"CLIENTE"`).