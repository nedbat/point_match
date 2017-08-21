import random
import timeit

if 0:
    TRIES = 10000

    for z in range(7):
        n = int(10**z)
        stmt='random.randint(1, 999999) in d'
        setup='import random; d = {{random.randint(1, 999999): 1 for _ in xrange({N:d})}}'.format(N=n)

        total = timeit.timeit(stmt=stmt, setup=setup, number=TRIES)
        print("{N:>9d}: {time:.7f}s".format(time=total/TRIES, N=n))

if 0:
    TRIES = 2000

    for z in range(7):
        n = int(10**z)
        stmt='random.randint(1, 999999) in x'
        setup='import random; x = [random.randint(1, 999999) for _ in xrange({N:d})]'.format(N=n)

        total = timeit.timeit(stmt=stmt, setup=setup, number=TRIES)
        print("{N:>9d}: {time:.7f}s".format(time=total/TRIES, N=n))

if 1:
    TRIES = 200

    for z in range(7):
        n = int(10**z)
        stmt='sorted(x)'
        setup='import random; x = [random.randint(1, 999999) for _ in xrange({N:d})]'.format(N=n)

        total = timeit.timeit(stmt=stmt, setup=setup, number=TRIES)
        print("{N:>9d}: {time:.7f}s".format(time=total/TRIES, N=n))
