#!/usr/bin/env python3
# Makes Sequences for Testing

import numpy as np

ALPHABET = ['A', 'C', 'T', 'G']
PHRED_MIN = 33
PHRED_MAX = 63

def iter_fasta(n=100, l=100):
    for i in range(n):
        header = f"seq{i}"
        seq = ''.join([ALPHABET[j] for j in np.random.choice(len(ALPHABET), l)])
        yield (header, seq)

def iter_fastq(n=100, l=100):
    for i in range(n):
        header = f"seq{i}"
        seq = ''.join([ALPHABET[j] for j in np.random.choice(len(ALPHABET), l)])
        qual = ''.join([chr(j) for j in np.random.randint(PHRED_MIN, PHRED_MAX, l)])
        yield (header, seq, qual)

def main():
    with open("test.fa", "w+") as f:
        for h, s in iter_fasta():
            f.write(f">{h}\n{s}\n")

    with open("test.fq", "w+") as f:
        for h, s, q in iter_fastq():
            f.write(f"@{h}\n{s}\n+\n{q}\n")
     


if __name__ == "__main__":
    main()
