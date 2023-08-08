def Score(Motifs: 'list[str]'):
    score = 0
    # get counts for each nucleotide at pos i
    for i in range(len(Motifs[0])):
        counts = {}
        for motif in Motifs:
            nuc = motif[i]
            if nuc in counts:
                counts[nuc] += 1
            else:
                counts[nuc] = 1
        # get most frequent
        base_mode = None
        for base in counts:
            if base_mode is None or counts[base] > counts[base_mode]:
                base_mode = base
        # get score
        for base in counts:
            if base != base_mode:
                score += counts[base]
    return score


def Profile(motifs: 'list[str]') -> 'list[dict[str, float]]':
    prof = []
    # iterate through each column
    for i in range(len(motifs[0])):
        # profile for column of motifs
        prof_i = {n: 0 for n in 'ATGC'}
        # iterate through motifs for nucleotides
        for j in range(len(motifs)):
            nuc = motifs[j][i]
            prof_i[nuc] += 1
        # turn into proportion
        for nuc in prof_i:
            prof_i[nuc] /= len(motifs)
        # add profile of column to profile
        prof.append(prof_i)
    return prof


# redefine ProfileMostProbableKmer to use list instead of set
# in order to preserve order & match expected answer
def ProfileMostProbableKmer(txt: str, k: int,
                                prof: 'List[Dict[str, float]]') -> str:

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
    kmer_max = None
    for i in range(len(txt) - k + 1):
        kmer = txt[i:i+k]
        p = KmerP(kmer, prof)
        if kmer_max is None or p > p_max:
            p_max = p
            kmer_max = kmer

    return kmer_max


def GreedyMotifSearch(seqs: 'list[str]', k: int, t: int) -> 'list[str]':
    assert len(seqs) == t

    # initial best motifs
    motifs_opt = [seq[0:k] for seq in seqs]
    # iterate kmers in first seq
    for i in range(len(seqs[0]) - k + 1):
        # store motif from first seq
        motifs = [seqs[0][i:i+k]]
        # look at other sequences
        # and greedily get motif
        for j in range(1, t):
            prof = Profile(motifs[0:j])
            motifs.append(ProfileMostProbableKmer(seqs[j], k, prof))
        # score motifs
        if Score(motifs) < Score(motifs_opt):
            motifs_opt = motifs
    return motifs_opt


def RunGreedyMotifSearch(*args):
    [k, t] = [int(x) for x in args[0].split()]
    seqs = args[1].split()
    return GreedyMotifSearch(seqs, k, t)
