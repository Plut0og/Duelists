import socket
from globals import globals
from player import player
from threading import Thread
import json


class multiplayerHandler():

    def __init__(self):
        self.c = None
        self.address = None
        self.clientType = int(raw_input("search(1) or host(2): "))
        if (self.clientType == 2):
            self.hostAddr = self.getIP()
            print(self.hostAddr)
            self.port = int(raw_input("Host on Port: "))
        elif (self.clientType == 1):
            self.hostAddr = raw_input("search for host: ")
            self.port = int(raw_input("Search on Port: "))

        self.s = None
        self.main()

    def getIP(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com", 80))
        ip = (s.getsockname()[0])
        s.close()
        return ip

    def main(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.s.setblocking(0)

        if (self.clientType == 2):
            self.s.bind((self.hostAddr, self.port))
            self.s.listen(1)
            self.c, self.addr = self.s.accept()
        elif (self.clientType == 1):
            self.s.connect((self.hostAddr, self.port))
        self.establishConnection()

    def establishConnection(self):
        if(self.clientType == 2):
            dataToSend = {}

            dataToSend['hero'] = globals.localHost.data[0]
            dataToSend['x'] = globals.localHost.data[1]
            dataToSend['y'] = globals.localHost.data[2]
            dataToSend['angle'] = globals.localHost.data[3]

            self.c.send(json.dumps(dataToSend))
            dataToRecieve = json.loads(self.c.recv(1024))
            globals.externalHost = player("externalHost", dataToRecieve['x'], dataToRecieve['y'], dataToRecieve['hero'])
            globals.players.append(globals.externalHost)

        elif(self.clientType == 1):
            dataToRecieve = json.loads(self.s.recv(1024))
            globals.externalHost = player("externalHost", dataToRecieve['x'], dataToRecieve['y'], dataToRecieve['hero'])
            globals.players.append(globals.externalHost)
            dataToSend = {}

            dataToSend['hero'] = globals.localHost.data[0]
            dataToSend['x'] = globals.localHost.data[1]
            dataToSend['y'] = globals.localHost.data[2]
            dataToSend['angle'] = globals.localHost.data[3]

            self.s.send(json.dumps(dataToSend))

    def listen(self):
        while(globals.isRunning):
            if (self.clientType == 1):
                raw = (self.s.recvfrom(1024))[0]
                raw = self.checkRaw(raw)
                data = json.loads(raw)
            elif (self.clientType == 2):
                raw = (self.c.recvfrom(1024))[0]
                raw = self.checkRaw(raw)
                data = json.loads(raw)
            self.handleData(data)
    def checkRaw(self, rawData):
        raw = rawData
        print(raw)
        brack = 0
        for i, v in enumerate(raw):
            if (not i == 0):
                if (brack == 0 and v == "{"):
                    print("ehllo")
                    lengthToEnd = (len(raw)) - i
                    raw = raw[lengthToEnd:]
            if (v == '{'):
                brack += 1
            elif (v == '}'):
                brack -= 1
        print(raw)
        return raw

    def sendData(self):

        data = {}

        data['hero'] = globals.localHost.data[0]
        data['x'] = globals.localHost.data[1]
        data['y'] = globals.localHost.data[2]
        data['angle'] = globals.localHost.data[3]
        data['currentAttack'] = {}
        data['animation'] = {}
        if(globals.localHost.data[4] != None):
            data['currentAttack']['number'] = globals.localHost.data[4].attack_num
        else:
            data['currentAttack']['number'] = None
        data['animation']['number'] = globals.localHost.data[5].number
        data['animation']['currentFrame'] = globals.localHost.data[5].currentFrame

        if(self.clientType == 2):
            self.c.send(json.dumps(data))
        elif(self.clientType == 1):
            self.s.send(json.dumps(data))


    def handleData(self, data):

        if(globals.externalHost.currentAttack != None):
            globals.externalHost.fight(data['currentAttack']['number'])
        if(globals.externalHost.angle != data['angle']):
            print(str(globals.externalHost.angle) + " " + str(data['angle']))
            globals.externalHost.rotate(data['angle'])

        globals.externalHost.moveTo(data['x'], data['y'])