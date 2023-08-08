from . import np

def ProfileMostProbableKmer(txt: str, k: int,
                                prof: 'List[Dict[str, float]]') -> str:
    kmers = set()
    # get all kmers in txt
    for i in range(len(txt) - k + 1):
        kmers.add(txt[i:i+k])

    # get probability of kmer
    def KmerP(kmer: str, prof: 'List[Dict[str, float]]'):
        # get p for each ind
        probs = [prof[i][kmer[i]] for i in range(len(kmer))]
        # get prob
        prob = 1
        for p in probs:
            prob *= p
        return prob

    # get max p iterating through kmers
    p_max = 0
    kmer_max = ''
    for kmer in kmers:
        p = KmerP(kmer, prof)
        if p > p_max:
            p_max = p
            kmer_max = kmer

    return kmer_max


def RunProfileMostProbableKmer(*args):
    txt = args[0]
    k = int(args[1])
    arr = []
    for l in args[2:]:
        arr.append([float(x) for x in l.split()])
    prof = []
    for col_ind in range(len(arr[0])):
        prof.append({nuc: arr[row_ind][col_ind] for nuc, row_ind in zip('ACGT', range(len(arr)))})
    return ProfileMostProbableKmer(txt, k, prof)