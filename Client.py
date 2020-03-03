#importación de módulos
import socket

#Puerto y Nombre de Host destino
Puerto=65500
Hostname=socket.gethostname()

#Inicialización de conexión con el Socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Hostname, Puerto))
print(f"Se está intentando establecer comunicación con el servidor  {Hostname} en el puerto {Puerto}")

#Mensaje de respuesta del servidor
msg=s.recv(1024)
print(msg.decode("utf-8"))
