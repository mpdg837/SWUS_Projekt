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


workingTime = []
workingAndTransmitTime = []

myGenerators = []
queues = []
outQueue = []
switchTime = []

priority = True

h = 1
N = 2

for n in range(N):
    queues.append([])

    workingTime.append(0)
    workingAndTransmitTime.append(0)

    myGenerators.append(generators.Generator(0))
    switchTime.append(10)
# Generatory

switchTime[0] = 10
switchTime[1] = 10

myGenerators[0] = generators.Generator(0.35)
myGenerators[1] = generators.Generator(0.35)

# Realizacja

print("t = 0 ")
print("Start: ")
for n in range(N):
    print("")
    print("Queue " + str(n + 1))
    queue.printQueue(queues[n])

print("====== ")
while time <= 100000:
    print("t = " + "{0:.3f}".format(time))

    for n in range(N):
        analysedGenerator = myGenerators[n]
        newPackets = analysedGenerator.generate(time, n)
        if len(newPackets) > 0:
            print("Generate new " + str(len(newPackets)) + "packets in queue " + str(n + 1))
            for newPacket in newPackets:
                queue.addToQueue(queues[n], newPacket)

    if getFromQueueTime >= h or time == 0:
        if initized:

            if not analysedPacket == None:
                print("Finish sending packet from queue: " + str(
                    lastQueue + 1) + " Value: '" + analysedPacket.packetValue + "' arrival time: " + str(
                    analysedPacket.arrivalTime))
                analysedPacket.setTransmissionTime(time - 1)
                outQueue.append(analysedPacket)
                workingAndTransmitTime[lastQueue] = workingAndTransmitTime[lastQueue] + 1

            workingTime[lastQueue] = workingTime[lastQueue] + 1
            analysedPacket = None
        else:
            initized = True

    if waitToStepTime >= switchTime[queueIndex]:
        waitToStepTime = 0

        queueIndex = queueIndex + 1
        if queueIndex >= N:
            queueIndex = 0

        print("-----")
        print("Switch to queue " + str(queueIndex + 1))

    if getFromQueueTime >= h or time == 0:
        if waitToStepTime < switchTime[queueIndex]:

            actN = queueIndex
            analysedPacket = None

            if priority:
                lastN = queueIndex

                while analysedPacket is None:
                    print(str(actN + 1))
                    analysedPacket = queue.getFromQueue(queues[actN])

                    actN = actN + 1
                    if actN >= N:
                        actN = 0

                    if actN == lastN:
                        break
            else:
                analysedPacket = queue.getFromQueue(queues[queueIndex])

            if analysedPacket is None:
                print("No packet to send")
            else:
                print("Start sending packet from queue: " + str(
                    queueIndex + 1) + " Value: '" + analysedPacket.packetValue + "' arrival time: " + str(
                    analysedPacket.arrivalTime))

            getFromQueueTime = 0
            lastQueue = queueIndex
        else:
            initized = False

    time = time + 1
    waitToStepTime = waitToStepTime + 1
    getFromQueueTime = getFromQueueTime + 1

for n in range(N):
    print("")
    print("Queue " + str(n + 1))
    queue.printQueue(queues[n])
print("")
print("Sent items:")
queue.printSentItems(outQueue)
print("")

for n in range(N):
    proc = workingAndTransmitTime[n] / workingTime[n] * 100
    print("Working time: " + "{0:.3f}".format(proc) + "%")
