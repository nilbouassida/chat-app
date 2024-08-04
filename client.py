import socket
import threading

nickname = input("input nickname: ")
ip = input("server: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((str(ip), 9999))


def receive():
    while True:
        try:
            msg = client.recv(1024).decode("utf-8")
            if msg == "NICK":
                client.send(nickname.encode("utf-8"))
            
            elif not(msg.startswith(nickname)):
                #if not msg.beginswith(nickname):
                print(msg)
        except:
            print("error")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        if message == "exit":
                print("*********goodbye*********")
                client.close()
                break
        client.send(message.encode("utf-8"))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

#client.close()