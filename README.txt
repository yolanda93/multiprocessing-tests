# Python-multiprocessing

In this repository, there are some tests carried out using the multiprocessing module available in Python to parallelize CPU-bounded tasks

Why multiprocessing?

The multiprocessing module works parallelizing tasks in a distributed-memory mode. This module represents a workaround for a well-known problem in python threads implementation (shared-memory oriented) and the mismatch with the GIL (Global Interpreter Lock)

Although this problem is well understood, the multiprocessing module still presents some pickling issues that could easily lead to bugs very difficult to detect on production. The goal of this project is to perform a series of test that could help to better understand the functionality of this module and document some bugs still present in this core-library addressing some platform-specific and pickling issues.
