import socket
import threading

nickname = input("Choose your Nickname")

FORMAT = 'ascii'
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREAM means that it is a TCP socket.
client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try: 
            message = client.recv(1024).decode(FORMAT)
            if message == 'NICK':
                client.send(nickname.encode(FORMAT))
                pass
            else: 
                print(message)
        except:
            print("An error occured!")
            client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode(FORMAT))

receive_thread = threading.Thread(target=receive)
receive_thread.start()
write_thread = threading.Thread(target=write)
write_thread.start()