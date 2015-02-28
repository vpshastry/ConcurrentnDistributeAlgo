import time
from lamportsFastAlgorithm import LamportsFastAlgo
from lamportsBakeryAlgorithm import LamportsBakeryAlgo
import random
import sys

def genRandNosWithSum(number, length):
    templist = [random.randrange(1, number) for i in range(length-1)]
    templist.append (number)
    templist.insert (0, 0)
    templist.sort ()
    randList = [0 for i in range(length)]

    for i in range(length):
        randList[i] = templist[i+1] - templist[i]
        if randList[i] == 0:
            randList[i] = 1

    return randList

def main():
    if len(sys.argv) != 3:
        print("Usage:", sys.argv[0], "<number-of-threads> <number-of-requests>")
        return 1

    numOfThreads = int (sys.argv[1])
    numOfRequests = int (sys.argv[2])
    if numOfRequests == numOfThreads:
        reqList = [1 for i in range(numOfThreads)]
    else:
        reqList = genRandNosWithSum (numOfRequests, numOfThreads)

    BakeryAlgo = LamportsBakeryAlgo (numOfThreads, reqList)
    FastAlgo = LamportsFastAlgo (numOfThreads, reqList)

    print ("Running Lamport's Bakery Algorithm")
    BakeryAlgo.mainFn(numOfThreads, sum(reqList))

    print ("Running Lamport's Fast Algorithm")
    FastAlgo.mainFn(numOfThreads, reqList)

main()
