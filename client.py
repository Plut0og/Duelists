import socket
import pygame
from threading import Thread

class globals():
    coms = False

def Main():

    clientType = int(raw_input("search(1) or host(2): "))
    if(clientType == 2):
        hostAddr = "10.7.38.75"
        port = int(raw_input("Host on Port: "))
    elif(clientType == 1):
        hostAddr = raw_input("search for host: ")
        port = int(raw_input("Search on Port: "))

    s = socket.socket()

    if(clientType == 2):
        s.bind((hostAddr, port))
        s.listen(1)
        c, addr = s.accept()

        listener = Thread(target=hear, args=(c, s, 2))
        talker = Thread(target=speak, args=(c, s, 2))

    elif(clientType == 1):
        s.connect((hostAddr, port))

        listener = Thread(target=hear, args=(0, s, 1))
        talker = Thread(target=speak, args=(0, s, 1))

    listener.start()
    talker.start()

    while(not globals.coms):
        continue
    s.close()

def hear(connection, sock, type):
    while(not globals.coms):
        Listen(connection, sock, type)

def Listen(connection, sock , type):
        if(type == 1):
            data = sock.recv(1024)
        elif(type == 2):
            data = connection.recv(1024)
        print(data)

def speak(connection, sock, type):
    while(not globals.coms):
        talk(connection, sock, type)

def talk(connection, sock, type):
    data = raw_input()
    if(type == 1):
        sock.send(data)
    elif(type == 2):
        connection.send(data)
    if(data == "quit"):
        globals.coms = True
if __name__ == "__main__":
    Main()