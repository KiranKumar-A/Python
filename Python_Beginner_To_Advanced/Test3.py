def IsPrime(n):
    for x in range(2, n//2+1):
        if not n%x:
            return False;
    return True;

def PrimesTo(n):
    for x in range(2,n):
        if IsPrime(x):
            print(x)
PrimesTo(50)
pdb.pm()