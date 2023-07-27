def Neighbors(pat: str, d: int):
    # return case
    if d == 0 or pat == '':
        return [pat]
    # recurse case
    else:
        # branching
        result = []
        for nt in "ATGC":
            # if same run neighbors on rest with same d
            if nt == pat[0]:
                result += [nt + neighbor for neighbor in Neighbors(pat[1:], d)]
            # else run neighbors on rest with d-1
            else:
                result += [nt + neighbor for neighbor in Neighbors(pat[1:], d - 1)]
        return result


def FrequentWordsWithMismatches(txt: str, k: int, d: int):
    freq = {}
    max = 0
    kmers = []
    # scan txt
    for i in range(len(txt) - k + 1):
        # get pat
        pat = txt[i:i + k]
        # get neighbors of pat
        neighbors = Neighbors(pat, d)
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

    return kmers


def RunFrequentWordsWithMismatches(*str_args):
    print(str_args)
    args = str_args[1].split()
    args = [int(x) for x in args]
    return FrequentWordsWithMismatches(str_args[0], *args)
