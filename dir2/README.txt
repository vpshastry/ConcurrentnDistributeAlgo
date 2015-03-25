Name: Varun Shastry
Date: 18th March 2015

This project implements the Agrawala and El Abaddi algorithm for distributed
mutual exclusion in 3*sqrt(n) message exchanging only within the quorum set.
The algorithm also provides the method to create the quorum set for a given set
of nodes. The references for the algorithm is specified in the reference
section.

The code to test correctness and performance are added to the implementation
and the report can be seen by uncommenting the code corresponding to that in
the method 'run' of the main class.

Correctness:
The entering and exit of the critical section is printed with the timestamp.
This also sleeps for n seconds inside the critical section to artifically yield
to other process and thereby provide the chance to enter the critical section.
If the critical section is truly mutually exclusive in the implementation there
would not be any messages other critical section message inbetween the current
message.

Performance:
The time to take the lock is noted and averaged over all the attempts. This can
be printed by uncommenting that part in the implementation from the method
'run' in the main class of main.da.

References:
* http://en.wikipedia.org/wiki/Maekawa's_algorithm
* An Efficient and Fault Tolerant Solution for Distributed Mutual Exclusion by
Divyakant Agrawal and Amr El Abbadi.
* A sqrt(n) Algorithm for Mutual Exclusion in Decentralized Systems by Mamoru
Maekawa
* http://sourceforge.net/p/distalgo/ for distAlgo specific documents
* stackoverflow.com and docs.python.org for python specific queries.
