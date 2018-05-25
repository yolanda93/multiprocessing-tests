from multiprocessing import Process, Manager, Queue

# Expected result: threads modify locally ns and then the local results are joined together
# Actual result:  The ns object remains inmutable
def test_sharedObject(ns):
    ns.y.append(2)
    ns.ls.append(4)


# Expected result: threads modify locally ns and then the local result are joined together
# Actual result: there concurrency problems 
def test_inNamespace(ns):
    ns.x += 1
    ns.ls.append(8)
    ns.ls.append(8)

    tmp = ns.y  # retrieve the shared value
    tmp.append(10)
    ns.y = tmp

    tmp = ns.ls
    tmp.append(8)
    ns.ls = tmp

# Expected result: threads modify locally out_q and the local result is merger in the main process
# Actual result:  This test works fine

def test_Queue(out_q):
    out_q.put(1)

if __name__ == '__main__':
    manager = Manager()
    ns = manager.Namespace()
    ns.x = 1
    ns.y = [1]
    ns.ls = manager.list([1, 1, 1])

    print """ Test 1 FAILED - Single process example"""

    print 'before', ns.ls, ns.x, ns.y
    p = Process(target=test_inNamespace, args=(ns,))
    p.start()
    p.join()
    print 'after',  ns.ls, ns.x, ns.y

    print """ Test 2 FAILED - Namespace - Multiple process example"""

    n=10
    ns.x = 1
    print 'before', ns.ls, ns.x, ns.y
    p = [Process(target=test_inNamespace, args=(ns,)) for i in range(n -1)]

    for each in p:
        each.start()

    for each in p:
        each.join()

    print 'after', ns.ls, ns.x, ns.y

    print """ Test 3 PASSED - Queue - Multiple process example"""

    n=10
    out_q = Queue()
    result = []
    print 'before', result
    p = [Process(target=test_Queue, args=(out_q,)) for i in range(n -1)]

    for each in p:
        each.start()

    for i in p:
       result.append(out_q.get())

    for each in p:
        each.join()

    print 'after', result
