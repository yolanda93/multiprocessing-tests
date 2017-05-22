import multiprocessing
import unittest
import pickle
from functools import wraps

class _ProcessPool_(unittest.TestCase):

    workers = []

    def test_run(self):
        print(_ProcessPool_.workers)
        for i,f_n in enumerate(_ProcessPool_.workers):
            self.assertRaises(TypeError,multiprocessing.Process(target=f_n).start())

    def test_run2(self):
        print(_ProcessPool_.workers)
        for i,f_n in enumerate(_ProcessPool_.workers):
            self.assertRaises(TypeError,multiprocessing.Process(target=func_wrapper,args=(f_n,)).start())


def add_worker(funct,name=None):
    _ProcessPool_.workers.append(funct)

def func_wrapper(funct):
    return funct()

def exec_wrapper():
    execfile("./testA.py")


"""Decorator add_worker with a wrapper to preserve global space name"""
def add_worker2(funct, name=None):
    print "add_worker"

    @wraps(funct)
    def wrapper(*args, **kwargs):
        return funct(*args, **kwargs)

    print(wrapper)
    _ProcessPool_.workers.append((wrapper))

@add_worker
def method_C():
    print  "method C is executed"

if __name__ == '__main__':
     method_C()
     #execfile("./testA.py")

     print "asda",type(method_C)

     import sys
     sys.exit()
     unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(_ProcessPool_))

     exec_wrapper()
     unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(_ProcessPool_))

     pickle.dump(_ProcessPool_.test, open("save.p","wb"))
     execfile("./testA.py")
     unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(_ProcessPool_))




