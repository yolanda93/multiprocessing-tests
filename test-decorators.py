import multiprocessing

class Test_bounding(object):

   def method_bound(self):
       print(self)
       pass

   @staticmethod
   def method_unbound():
       print Test_bounding

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


def A(B):
    B("x")
    pass
    #return Test_bounding.method_unbound2()

def B():
    print "bbb"

print "a"


if __name__ == '__main__':

    ###################### Unbound and bound methods

   # Works.
   #test1 = Test_bounding()
   #test1.method_bound()
   #multiprocessing.Process(target=test1.method_bound).start()
   # Fails.
   #multiprocessing.Process(target=test1.method_unbound).start()
   #multiprocessing.Process(target=Test_bounding.method_unbound).start()
   multiprocessing.Process(target=A, args=(get_text,)).start()

    ######################  Using decorators

   # Works.
   #print get_text("Parent")
   # Fails.
   #multiprocessing.Process(target=get_text, args=("Child",)).start()