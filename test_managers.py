import multiprocessing

def f(ns):
    ls.append(8)
    ls.append(8)



if __name__ == '__main__':
    manager = multiprocessing.Manager()
    ls = manager.list([1, 1, 1])

    print 'before', ls
    p = multiprocessing.Process(target=f, args=(ls,))
    p.start()
    p.join()
    print 'after', ls