import time
import sys
import threading

class LamportsBakeryAlgo:
    choosing = list()
    num = list()

    thread = list()
    nthreads = 0
    sharedMemory = 0
    nRequests = 0
    noOfTimes = list()

    def __init__(self, noOfThreads, reqList):
        self.choosing = [False for i in range(noOfThreads)]
        self.num = [0 for i in range(noOfThreads)]

        self.thread = [0 for i in range(noOfThreads)]
        self.nthreads = noOfThreads

        self.nRequests = sum(reqList)
        self.noOfTimes = reqList[:]

        self.sharedMemory = 0

    def lock(self, myIdx):
        print ("Thread: ", myIdx, "requesting to enter CS")

        self.choosing[myIdx] = True
        self.num[myIdx] = 1 + max (self.num)
        self.choosing[myIdx] = False

        for j in range(self.nthreads):
            while self.choosing[j]:
                pass

            while (self.num[j] != 0) and ((self.num[j] < self.num[myIdx]) or
                    ((self.num[j] == self.num[myIdx]) and (j < myIdx))):
                pass

    def unlock(self, myIdx):
        self.num[myIdx] = 0

    def critical_section(self, myIdx):
        print ("Entering the critical section of thread:", myIdx)

        self.sharedMemory = myIdx
#time.sleep (1)

        print ("Shared memory value: ", self.sharedMemory)
        print ("Thread:", myIdx, "exiting critical section")

    def threaded_function(self, myIdx):
        for counter in range (self.noOfTimes[myIdx]):
            self.lock (myIdx)
            self.nRequests -= 1
            self.critical_section (myIdx);
            self.unlock (myIdx)

    def create_threads(self, numOfThreads):
        for i in range(numOfThreads):
            self.thread[i] = threading.Thread (target = self.threaded_function,
                                args = (i, ))
            self.thread[i].start()

        for i in range(numOfThreads):
            self.thread[i].join()

    def mainFn(self, numOfThreads, numOfRequests):
        self.create_threads(numOfThreads)

        print ("Done with all the threads. Exiting...")
