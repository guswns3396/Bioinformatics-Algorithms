import pandas as pd
import numpy as np


from .ba1g import HammingDistance


def Count(ser):
    return ser.value_counts()


def Entropy(counts: "pd.Series") -> float:
    tot = counts.sum()
    probs = counts / tot
    h = -1 * np.sum(probs * (np.log(probs) / np.log(2)))
    return h


def EntropyFromSeqs(seqs):
    df = pd.DataFrame([[nuc for nuc in seqs[i]] for i in range(len(seqs))])
    df = df.apply(Count, axis=0)
    return df.apply(Entropy, axis=0).sum()


def generate(s, l, it):
    if l == 0:
        return [s]
    res = []
    for i in it:
        res += generate(s + i, l - 1, it)
    return res


def MedianString(Dna: list, k: int) -> str:

    def DMinSeq(pattern, seq):
        # look at all kmers for seq
        # return the minimized d
        d_min = None
        for i in range(len(seq) - len(pattern) + 1):
            kmer = seq[i:i+len(pattern)]
            d = HammingDistance(pattern, kmer)
            if d_min is None or d_min > d:
                d_min = d
        return d_min

    # get all possible kmer patterns
    patterns = generate('', k, 'ATGC')

    # minimized d for pattern
    d_min = None
    for pattern in patterns:
        # d for each pattern
        d_pattern = 0
        for seq in Dna:
            d_pattern += DMinSeq(pattern, seq)
        if d_min is None or d_min > d_pattern:
            d_min = d_pattern
            pattern_min = pattern

    return pattern_min


def RunMedianString(*str_args):
    k = int(str_args[0])
    Dna = str_args[1:]
    return MedianString(Dna, k)