import random


def gen_rand_file(filename, nmax, n):
    """
    generates a file of n random integers with no dups, ints in file
    will be in the range [0, nmax).
    Args:
        filename (str): output filename
        nmax (int): max val of int range
        n (int): number of ints to generate
    """
    seen = {}
    cnt = 0

    with open(filename, 'wb') as fp:
        while cnt < n:
            x = random.randint(0, nmax-1)
            if x not in seen:
                fp.write(str(x) + '\n')
                seen[x] = True
                cnt += 1


if __name__ == "__main__":
    import sys
    args = sys.argv[1:]

    outfile = args[0]
    del args[0]

    nmax = int(args[0])
    del args[0]

    n = int(args[0])
    del args[0]

    assert n <= nmax
    gen_rand_file(outfile, nmax, n)
