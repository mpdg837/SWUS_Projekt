import packet
import numpy as np

class Generator:
    poisson = False
    linear = False

    parameter = 0

    time = 0
    lastTime = 0
    savedPoisson = 0

    def __init__(self,poisson,linear,parameter):
        self.poisson = poisson
        self.parameter = parameter
        self.linear = linear

    def generate(self,h,time,queue):
        if self.linear:
            if self.time >= self.parameter * h:
                self.time = 0
                self.time = self.time + 1

                return packet.QueuePacket(time,queue)

        if self.poisson:
            if self.time >= self.savedPoisson:
                self.time = 0
                self.time = self.time + 1
                self.savedPoisson = np.random.poisson(self.parameter) * h

                return packet.QueuePacket(time, queue)

        self.time = self.time + 1

        return None