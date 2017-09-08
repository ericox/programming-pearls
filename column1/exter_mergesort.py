#!/usr/bin/env python
"""
External Mergesort!
"""
import os


class ExternalMergeSort(object):
    def __init__(self, infile, outfile, mem_limit=1024):
        self.infile = infile
        self.outfile = outfile
        self.mem_limit = mem_limit
    
    def split(self):
        """
        Splits input file into nchunks based on mem_limit for interal
        sorting.
        """
        import pdb
        pdb.set_trace()
        infstat = os.stat(self.infile)
        size = infstat.st_size

        # will read mstmp file pairs into one buffer and use qsort
        nchunk = self.mem_limit / 2
        nchunk += 1 # int floor div

        outfile = open(self._outfile_name(self.outfile, 0), 'w')
        infileptr = open(self.infile, 'r')

        m = 1
        bytes_read = 0
        for line in infileptr:
            if bytes_read > m*nchunk:
                outfile.flush()
                outfile.close()
                outfile = open(self._outfile_name(self.outfile, m), 'w')
                m += 1
            bytes_read += len(line) 
            outfile.write(line)
        outfile.flush()
        outfile.close()
        infileptr.close()

    def _outfile_name(filename, m):
        return 'mstmp-{0}-{1}'.format(filename.rstrip('.txt'), m)

if __name__ == "__main__":
    mergesort = ExternalMergeSort('phone.txt', 'mergesort-out.txt', 100)
    mergesort.split()
