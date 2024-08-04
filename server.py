import socket
import threading
import sys, os

os.system("clear")
print("running server.....")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9999))
server.listen()

clients = []
nicknames = []

def broadcast(msg):
    for client in clients:
        client.send(msg)

def handle(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)
        except:
            ind = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[ind]
            broadcast(f"{nickname} left the chat".encode("utf-8"))
            nicknames.remove(nickname)
            break

def receive():
    while True:
        client, addr = server.accept()
        print(f"connected with {str(addr)}")
        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)

        print(f"nickname of new client is {nickname}")
        broadcast(f"{nickname} entered the chat".encode("utf-8"))
        client.send("connected to the server".encode("utf-8"))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()


# run = True
# while run:
#     msg = client.recv(1024).decode("utf-8")
#     if msg == "quit":
#         run = False
#     else:
#         print(msg)
#     client.send(input("Message: ").encode("utf-8"))
