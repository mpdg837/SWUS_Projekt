import packet
import numpy as np

class Generator:

    parameter = 0

    time = 0
    lastTime = 0
    savedPoisson = 0


    def __init__(self,parameter):
        self.parameter = parameter

    def generate(self,time,queue):

        packets = []

        los = np.random.poisson(self.parameter)

        for n in range(los):
            packets.append(packet.QueuePacket(time,queue))

        return packets