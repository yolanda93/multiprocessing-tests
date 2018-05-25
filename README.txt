# Python-multiprocessing

In this repository, there are some tests carried out using the multiprocessing module available in Python to parallelize CPU-bounded tasks

Why multiprocessing?

The multiprocessing module works parallelizing tasks in a distributed-memory mode. This module represents a workaround for a well-known problem in C Python threads implementation (shared-memory oriented) and the mismatch with the Global Interpreter Lock (GIL) [1][2]

Although this problem is well understood, the multiprocessing module still presents some pickling issues that could easily lead to bugs very difficult to detect on production. The goal of this project is to perform a series of test that could help to better understand the functionality of this module and document some bugs still present in this core-library addressing some platform-specific and pickling issues.

Asynchronous programming vs Multiprocessing

Asynchronous programming in Python is becoming more and more popular. This programming paradigm could be seen also as a method to parallilize CPU-bounded tasks and it is
less error prone and sometimes more efficient than the processing module.

There are many different libraries in Python for asynchronous programming but the most popular is asyncio. The main advantage of this method in contrast to Multithreading
is that it does not actually run parallel threads on shared resources; instead it allows us to efficiently schedule the application process to manage all the tasks with different priority. Of course, this is only useful if we have an appplication with different cpu load-level tasks. 

In this case, the program does not suffer from CPU context switching in non-deterministic time intervals order the CPU share resources; so it could significantly reduce the complexity of the application program while mainting the same performance as the multiprocessing module.

In asynchronous programming, there is a queue of events/jobs and a loop that just constantly pulls jobs off the queue and runs then[3]. This is achieved through callbacks functions, the code inside a callback function is executed inmedialty after the main job finished and when it recibes an update.

Callback disadvantages:
 
Callbacks swallows exceptions: Any exception thrown in a callback will bread the event loop and the program, therefore errors have to be passed as objects rather than raised.


### References
[1] http://www.dabeaz.com/GIL/
[2] https://eli.thegreenplace.net/2012/01/16/python-parallelizing-cpu-bound-tasks-with-multiprocessing/
[3] https://hackernoon.com/asynchronous-python-45df84b82434
