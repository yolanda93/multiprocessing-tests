import test_execfile

@add_worker
def method_A():
    return "method A is executed"


@add_worker
def method_B():
    return "method B is executed"



@add_worker
def method_C():
    return "method C is executed"


