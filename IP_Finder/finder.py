import socket

hostname = socket.gethostname() # Получаем hostname
# Получить АЙПИ
ip = socket.gethostbyname(hostname)
# Ну и принт всей информации
print(f"HOSTNAME : {hostname}")
print(f"IP Adress : {ip}")
