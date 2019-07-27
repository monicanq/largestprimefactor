import math

def primefactor(mynumber):
    myset = set()
    factorset = set()
    limit = 1+ int(math.sqrt(mynumber))
    for x in range (2,limit):
        if mynumber % x == 0:
            l = mynumber/x
            factorset.add(l)
            factorset.add(x)
        for x in factorset:
            for y in range (2,x):
                if x % y != 0:
                    isprime = True
                else:
                    isprime = False
                    break
            if isprime == True:
                myset.add(x)
    r = max(myset)
    return(r)

mynumber = int(input('Enter a very large number: '))
largestprime = primefactor(mynumber)
print('The largest prime factor of ' + str(mynumber) +' is '+ str(largestprime))
