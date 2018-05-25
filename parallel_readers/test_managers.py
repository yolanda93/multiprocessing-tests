from multiprocessing import Process, Manager, freeze_support
import sys
import os
import time


def read_in_chunks(file_object, lines):
    while True:
        data  = file_object.readlines(lines)
        if not data:
              break
        yield data

def load_in_memory(ns):
     print "ProcessPID:"  + str(os.getpid()) + " - " " Reading lines: " +  str(4)
     for i in range(4):
           tmp = ns.ls 
           ns.ls.append(66) # append to the matrix
           ns.ls = tmp

def test_inNamespace(ns):

    for i in range(4):
        tmp = ns.ls
        tmp.append(66)
        ns.ls = tmp

if __name__ == '__main__':
    file_path = sys.argv[1]

    time1 = time.time()
    try:
        f = open(file_path)
    except IOError:
        print("The file {} does not exist.".format(file_path))
        

    manager = Manager()
    ns = manager.Namespace()
    
    ns.ls = manager.list()

    n =10
    print 'before', ns.ls
    p = [Process(target=test_inNamespace, args=(ns,)) for i in range(n-1)]

    for each in p:
        each.start()

    for each in p:
        each.join()

    print 'after',  ns.ls
