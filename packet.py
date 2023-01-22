import random


def randomCharacter():
    los = int(random.random() * 61)
    if los < 10:
        return chr(los + ord('0'))
    elif los < 36:
        return chr(los - 10 + ord('A'))
    else:
        return chr(los - 36 + ord('a'))


def randomPacket():
    packetLen = 16

    packetArray = []
    for n in range(packetLen):
        packetArray.append(randomCharacter())

    return ''.join(packetArray)



class QueuePacket:
    numberOfQueue = 0
    arrivalTime = 0
    transmissionTime = 0

    packetValue = ""

    def __init__(self,arrivalTime,numberOfQueue):
        self.packetValue = randomPacket()
        self.arrivalTime = arrivalTime
        self.numberOfQueue = numberOfQueue

    def setTransmissionTime(self,transmissionTime):
        self.transmissionTime = transmissionTime


