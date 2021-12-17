#!/usr/bin/env python3
# Makes Sequences for Testing

import numpy as np

SEED = 42
ALPHABET = ['A', 'C', 'T', 'G']
PHRED_MIN = 33
PHRED_MAX = 63


def make_seq(size):
    """
    randomly generates a sequence
    """
    return ''.join([ALPHABET[j] for j in np.random.choice(len(ALPHABET), size)])


def make_qual(size):
    """
    randomly generates a quality score
    """
    return ''.join([chr(j) for j in np.random.randint(PHRED_MIN, PHRED_MAX, size)])


def iter_seq(n=100, l=100, is_fastq=False):
    for i in range(n):
        header = f"seq{i}"
        seq = make_seq(l)

        if not is_fastq:
            yield (header, seq)
        else:
            qual = make_qual(l)
            yield (header, seq, qual)


def main():
    np.random.seed(SEED)
    
    with open("test.fa", "w+") as f:
        for h, s in iter_seq():
            f.write(f">{h}\n{s}\n")

    with open("test.fq", "w+") as f:
        for h, s, q in iter_seq(is_fastq=True):
            f.write(f"@{h}\n{s}\n+\n{q}\n")


if __name__ == "__main__":
    main()
