import pdb

def fun1(a):
    if a % 2:
        return True
    else:
        return False
def fun2(x):
    if type(x) is int:
        pdb.set_trace()
        print(fun1(x))
    else:
        print('Not defined')
fun2(3)