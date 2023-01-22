import packet


def isEmptyAllQueues(queues):
    for queue in queues:
        if len(queue) > 0:
            return False

    return True

def addToQueue(queue,packet):
    queue.append(packet)

def getFromQueue(queue):

    if len(queue) > 0:
        return queue.pop(0)
    else:
        return None

def printQueue(queue):
    if len(queue) > 0:
        print("Size : " + str(len(queue)))
        for items in queue:
            print("Packet: " + items.packetValue+" ,arrvial time: "+"{0:.3f}".format(items.arrivalTime)+ " delay time: infitive")
    else:
        print("(Empty)")

def printSentItems(queue):
    if len(queue) > 0:
        print("Size : " + str(len(queue)))

        n = 0
        sum = 0
        for items in queue:
            n = n + 1
            delay = items.transmissionTime - items.arrivalTime
            sum = sum + delay
            print("Queue: " + str(items.numberOfQueue + 1)+ " Packet: " + items.packetValue+" ,arrvial time: "+ "{0:.3f}".format(items.arrivalTime)+ " transmission time: "+"{0:.3f}".format(items.transmissionTime)+ " delay: "+"{0:.3f}".format(delay))

        print("Average: "+str(sum/n))

    else:
        print("(Empty)")


def isEmpty(queue):
    return len(queue) == 0