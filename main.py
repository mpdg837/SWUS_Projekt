import generators
import queue
import packet

# Zmienne kotnrolne
queueIndex = 0

time = 0

waitToStepTime = 0
getFromQueueTime = 0

lastQueue = 0
initized = False

analysedPacket = None
# Zmienne globalne

myGenerators = []
queues = []
outQueue = []

h = 1
switchTime = []
N = 2

for n in range(N):
    queues.append([])
    myGenerators.append(generators.Generator(False,False,0))
    switchTime.append(5)
# Generatory

myGenerators[0] = generators.Generator(False,True,5)
myGenerators[1] = generators.Generator(False,True,5)

# Realizacja

print("t = 0 ")
print("Start: ")
for n in range(N):
    print("")
    print("Queue "+str(n+1))
    queue.printQueue(queues[n])

print("====== ")
while time <= 500:
    print("t = "+"{0:.3f}".format(time))

    for n in range(N):
        analysedGenerator = myGenerators[n]
        newPacket = analysedGenerator.generate(h,time,n)
        if not newPacket == None:
            print("Generate new packet in queue " + str(n+1))
            queue.addToQueue(queues[n],newPacket)

    if getFromQueueTime >= h or time == 0:
        if initized:

            if not analysedPacket == None:
                print("Finish sending packet from queue: " + str(lastQueue + 1)+" Value: '" + analysedPacket.packetValue + "' arrival time: " + str(analysedPacket.arrivalTime))
                analysedPacket.setTransmissionTime(time)
                outQueue.append(analysedPacket)

            analysedPacket = None
        else:
            initized = True

    if waitToStepTime >= switchTime[queueIndex] :
        waitToStepTime = 0

        queueIndex = queueIndex + 1
        if queueIndex >= N:
            queueIndex = 0

        print("-----")
        print("Switch to queue "+str(queueIndex + 1))

        for n in range(N):
            print("")
            print("Queue " + str(n + 1))
            queue.printQueue(queues[n])
        print("")
        print("Sent items:")
        queue.printSentItems(outQueue)
        print("")

    if getFromQueueTime >= h or time == 0:
        if waitToStepTime < switchTime[queueIndex]:

            analysedPacket = queue.getFromQueue(queues[queueIndex])
            if analysedPacket == None :
                print("No packet to send")
            else:
                print("Start sending packet from queue: " + str(queueIndex + 1) +" Value: '"+analysedPacket.packetValue+"' arrival time: "+str(analysedPacket.arrivalTime))

            getFromQueueTime = 0
            lastQueue = queueIndex
        else:
            initized = False

    time = time + 1
    waitToStepTime = waitToStepTime + 1
    getFromQueueTime = getFromQueueTime + 1