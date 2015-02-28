The project tries to implement the 2 mutual exclusion algorithms
i. Lamport's Fast Mutual Exclusion Algorithm for n processes
ii. Lamport's Bakery Algorithm
This also contains a wrapper code to test the algorithm.

The algorithm can be found from the links mentioned in the reference section
below.

The wrapper program to test does the following.
1. Takes the input of number of threads and number requests
2. Creates that many number of threads and runs them in parallel the critical
   section of the code
3. The critical section of the code just assigns a value to the thread global
   variable and prints it. It also sleeps for a second between assignment and
   printing to yield to other threads and since the lock is held the value is
   not changed and prints the same value so by ensuring the integrity of the
   lock.
4. This is done for number request times including all the threads (each thread
   runs random number of times)

The file lamportsFastAlgorithm.py contains the Lamport's Algorithm
implementation and lamportsBakeryAlgorithm.py contains the LamportsBakery
algorithm implementation.

How to run:
python3.4 main.py <number-of-threads> <number-of-requests>

References:
http://en.wikipedia.org/wiki/Lamport's_bakery_algorithm
A Fast Mutual Exclusion Algorithm - Leslie Lamport - Nov 14, 1985
