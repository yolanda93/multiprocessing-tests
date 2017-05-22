import multiprocessing
import unittest

class BoundingMethods(object):

   def method_bound(self):
       print(self)
       pass

   @staticmethod
   def method_unbound():
       print BoundingMethods

   @staticmethod
   def method_unbound2():
       print get_text("x")

def deco(func):
   def func_wrapper(name):
       return "<p>{0}</p>".format(func(name))
   return func_wrapper

@deco
def get_text(name):
   return "Test using decorators, it is called from: {0}".format(name)


def warping_function():
    return get_text('Parent')


def warping_function(funct):
    return funct()

class TestBounding(unittest.TestCase):

    def test_method_bound(self):
         test = BoundingMethods()
         self.assertRaises(TypeError, multiprocessing.Process(target=test.method_bound).start())

    def test_method_unbound(self):
        test = BoundingMethods()
        self.assertRaises(TypeError, multiprocessing.Process(target=test.method_unbound).start())


class TestDecorators(unittest.TestCase):

    def test_parent(self):
        self.assertRaises(TypeError,get_text("Parent"))

    def test_child(self):
        self.assertRaises(TypeError, multiprocessing.Process(target=get_text, args=("Child",)).start())

    def test_child_encapsulated(self):
        self.assertRaises(TypeError, multiprocessing.Process(target=warping_function).start())

    def test_child_encapsulated_arg(self):
        self.assertRaises(TypeError, multiprocessing.Process(target=warping_function, args=(get_text,)).start())


if __name__ == '__main__':

    ###################### Unbound and bound methods
    print('Unbound and bound methods')
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestBounding))

    ######################  Using decorators
    print('Decorators')
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestDecorators))