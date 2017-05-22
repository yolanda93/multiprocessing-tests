import multiprocessing
import unittest

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

if __name__ == '__main__':

     execfile("./testA.py")
     unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(_ProcessPool_))

     exec_wrapper()
     unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(_ProcessPool_))

