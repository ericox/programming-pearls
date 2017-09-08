BITSPERWORD = 32
SHIFT = 5
MASK = 0x1F


class IntBitVec(object):
    def __init__(self, nmax):
        self.nmax = nmax
        self.arr = [0 for i in range(1 + nmax / BITSPERWORD)]
        self.n = 0

    def set(self, i):
        self.arr[i >> SHIFT] |= (1 << (i & MASK))

    def clear(self, i):
        self.arr[i >> SHIFT] &= ~(1 << (i & MASK))

    def test(self, i):
        return self.arr[i >> SHIFT] & (1 << (i & MASK))

    def insert(self, i):
        if self.test(i):
            return
        self.set(i)
        self.n += 1

    def size(self):
        return self.n

    def remove(self, i):
        if not self.test(i):
            return
        self.clear(i)
        self.n -= 1

    def report(self, v):
        for i in range(0, self.nmax):
            if self.test(i):
                v.append(i)


if __name__ == "__main__":

    bitmap = IntBitVec(10)

    bitmap.insert(0)
    bitmap.insert(2)
    bitmap.insert(4)
    bitmap.insert(6)
    bitmap.insert(8)

    assert bitmap.n == 5
    for i in range(10):
        if i % 2 != 0:
            assert bitmap.test(i) == 0
        else:
            assert bitmap.test(i) > 0

    bitmap.remove(2)
    assert bitmap.n == 4
    assert bitmap.test(2) == 0

    v = []
    bitmap.report(v)
    print v
