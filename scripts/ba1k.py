from .ba1j import Neighbors
from .ba1c import ReverseComplement

def RCFrequentWordsWithMismatches(txt: str, k: int, d: int):
    freq = {}
    max = 0
    kmers = []
    # scan txt
    for i in range(len(txt) - k + 1):
        # account for RC
        pat = txt[i:i + k]
        for p in [pat, ReverseComplement(pat)]:
            # get neighbors
            neighbors = Neighbors(p, d)
            # update frequency
            for neighbor in neighbors:
                if neighbor in freq:
                    freq[neighbor] += 1
                else:
                    freq[neighbor] = 1
                # update max
                if freq[neighbor] > max:
                    max = freq[neighbor]
    # get maximum frequency
    for kmer in freq:
        if freq[kmer] == max:
            kmers.append(kmer)
    # print(max)
    return kmers


def RunRCFrequentWordsWithMismatches(*str_args):
    print(str_args)
    args = str_args[1].split()
    args = [int(x) for x in args]
    return RCFrequentWordsWithMismatches(str_args[0], *args)
