from .ba2d import Score, ProfileMostProbableKmer


def Profile(motifs: 'list[str]') -> 'list[dict[str, float]]':
    prof = []
    # iterate through each column
    for i in range(len(motifs[0])):
        # profile for column of motifs
        prof_i = {n: 1 for n in 'ATGC'}
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


def GreedyMotifSearchPseudo(seqs: 'list[str]', k: int, t: int) -> 'list[str]':
    # initial best motifs
    motifs_opt = [seq[0:k] for seq in seqs]
    # iterate kmers in first seq
    for i in range(len(seqs[0]) - k + 1):
        # store motif from first seq
        motifs = [seqs[0][i:i + k]]
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
    return GreedyMotifSearchPseudo(seqs, k, t)
