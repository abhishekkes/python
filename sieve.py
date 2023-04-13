def sieve(n):
    global primes
    primes=[True]*(n+1)
    primes[0]=False
    primes[1]=False
    for j in range(2,n+1):
        if primes[j]==False:
            continue
        for i in range (j*j,n+1,j):
                primes[i]=False
n=int(input('input n'))
sieve(n)
for i in range (2,n+1):
        if primes[i]:
            print(i,end=' ')

