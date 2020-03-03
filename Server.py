#importación de módulos
import socket

#Puerto y Nombre de Host
Puerto=65500
Hostname=socket.gethostname()

#Inicialización de Socket TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Hostname, Puerto))
s.listen(5)

print(f"Se inicio un Socket en {Hostname} en el puerto {Puerto}")

#Socket en espera de conexión TCP
while True:
    clientsocket, address = s.accept()
    print(f"La conexión desde {address} fue establecida")
 #Envió de mensaje de bienvenida al cliente 
    clientsocket.send(bytes(f"Bienvenido al servidor {Hostname}", "utf-8"))
