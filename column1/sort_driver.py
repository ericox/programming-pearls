import sys
import timeit
from intbitvec import IntBitVec


def bitmap_sort(infile, outfile):
    bitmap = IntBitVec(10000000)

    print "reading input: " + infile

    t0 = timeit.default_timer()
    with open(infile, 'r') as fp:
        for line in fp:
            x = line.rstrip('\n')
            bitmap.insert(int(x))
    tin = timeit.default_timer() - t0

    t0 = timeit.default_timer()
    v = []
    bitmap.report(v)
    tsort = timeit.default_timer() - t0

    print "writing output: " + outfile
    t0 = timeit.default_timer()
    with open(outfile, 'wb') as fp:
        for x in v:
            fp.write(str(x) + '\n')
    tout = timeit.default_timer() - t0
    report_time(tin, tsort, tout, method='bitmap')


def system_sort(infile, outfile):
    arr = []

    print "reading input: " + infile
    t0 = timeit.default_timer()
    with open(infile, 'r') as fp:
        for line in fp:
            x = line.rstrip('\n')
            arr.append(int(x))
    tin = timeit.default_timer() - t0

    t0 = timeit.default_timer()
    out = sorted(arr)
    tsort = timeit.default_timer() - t0

    print "writing output: " + outfile

    t0 = timeit.default_timer()
    with open(outfile, 'wb') as fp:
        for x in out:
            fp.write(str(x) + '\n')
    tout = timeit.default_timer() - t0

    report_time(tin, tsort, tout)


def report_time(tin, tsort, tout, method='system'):
    print "input time (s): ", tin
    print method + " sort time (s): ", tsort
    print "ouput time (s): ", tout


def main():
    args = sys.argv[1:]
    if args:
        infile = args[0]
        del args[0]

        outfile = args[0]
        del args[0]

        sort = args[0]
        del args[0]

        if sort == 'bitmap':
            bitmap_sort(infile, outfile)
        elif sort == 'system':
            system_sort(infile, outfile)


if __name__ == "__main__":
    main()
