import time
import sys
import threading

class LamportsFastAlgo:
    b = list()
    y = 0

    thread = list()
    nthreads = 0
    sharedMemory = 0
    nRequests = 0
    noOfTimes = list()

    def __init__(self, noOfThreads, reqList):
        self.b = [False for i in range(noOfThreads)]
        self.y = -1

        self.thread = [0 for i in range(noOfThreads)]
        self.nthreads = noOfThreads

        self.nRequests = sum(reqList)
        self.noOfTimes = reqList[:]

        self.sharedMemory = 0

    def lock(self, myIdx):
        print ("Thread: ", myIdx, "requesting to enter CS")
        stayInLoop = True
        while stayInLoop:
            stayInLoop = False

            self.b[myIdx] = True
            x = myIdx
            if self.y != -1:
                self.b[myIdx] = False

                if self.y != -1:
                    pass

                stayInLoop = True
                continue

            self.y = myIdx
            if x != myIdx:
                self.b[myIdx] = False
                for j in range (self.nthreads):
                    if self.b[j] != False:
                        pass

                if self.y != myIdx:
                    if self.y != -1:
                        pass

                    stayInLoop = True
                    continue


    def unlock(self, myIdx):
        self.y = -1
        self.b[myIdx] = False

    def critical_section(self, myIdx):
        print ("Thread:", myIdx, "entering the critical section")

        self.sharedMemory = myIdx
#time.sleep (1)

        print ("Shared memory value:", self.sharedMemory)
        print ("Thread:", myIdx, "exiting critical section")

    def threaded_function(self, myIdx):
        for counter in range(self.noOfTimes[myIdx]):
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
