from .ba1b import FrequencyTable


def FindClumps(txt: str, k: int, L: int, t: int):
    pats = set()
    for i in range(len(txt) - L + 1):
        counts = FrequencyTable(txt[i:i + L], k)
        for pat in counts:
            if counts[pat] >= t:
                pats.add(pat)
    return pats


def FindClumpsEff(txt: str, k: int, L: int, t: int):
    pats = set()
    kmer_indices = {}
    # scan txt to get all k-mers
    for i in range(len(txt) - k + 1):
        kmer = txt[i:i + k]
        # add position of kmer to the list if already seen
        if kmer in kmer_indices:
            kmer_indices[kmer].append(i)
        # otherwise map kmer to position as a list
        else:
            kmer_indices[kmer] = [i]
    # check each kmer frequency
    for kmer, indices in kmer_indices.items():
        # check window if occurs more than t times
        if len(indices) >= t:
            for i in range(len(indices) - t + 1):
                if (indices[i + t - 1] + k) - indices[i] <= L:
                    pats.add(kmer)
    return pats


def RunFindClumps(txt: str, str_args: str):
    args = str_args.split()
    args = [int(x) for x in args]
    return FindClumps(txt, *args)


def RunFindClumpsEff(txt: str, str_args: str):
    args = str_args.split()
    args = [int(x) for x in args]
    return FindClumpsEff(txt, *args)
