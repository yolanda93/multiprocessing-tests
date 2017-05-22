from multiprocessing import Process
import mock_module


class A(object):
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

    def __getstate__(self):
        print '__getstate__'
        return { 'a': self.a, 'b': self.b,
                 'c':0 }

def func():
    mock_module.value_mock = 1
    a = A()
    return a

def func1(a):
    print a.a, a.b, a.c
    print c
    print mock_module.value_mock

c = 2
if __name__ == '__main__':
    a = func()
    p = Process(target=func1, args=(a,))
    p.start()
    p.join()

"""
#Windows
__getstate__
1 2 0
2
None

#Unix
1 2 3
2
1
"""