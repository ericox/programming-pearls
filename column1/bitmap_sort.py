import sys
from intbitvec import IntBitVec


def main():
    args = sys.argv[1:]
    if args:
        infile = args[0]
        del args[0]
        print "reading input: " + infile

        outfile = args[0]
        del args[0]

    bitmap = IntBitVec(10000000)

    with open(infile, 'r') as fp:
        for line in fp:
            x = line.rstrip('\n')
            bitmap.insert(int(x))

    print "writing output: " + outfile
    with open(outfile, 'wb') as fp:
        for i in range(10000000):
            if bitmap.test(i):
                fp.write(str(i) + '\n')

if __name__ == "__main__":
    main()
