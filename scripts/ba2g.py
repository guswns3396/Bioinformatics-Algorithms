import random

from .ba2d import Score, KmerP
from .ba2e import Profile


def ProfileRandomKmer(txt: str, k: int,
                                prof: 'List[Dict[str, float]]') -> str:
    # get probabilities of all kmers
    kmers = []
    probs = []
    for i in range(len(txt) - k + 1):
        kmers.append(txt[i:i+k])
        probs.append(KmerP(kmers[-1], prof))
    # pick kmer weighted by their probability
    return random.choices(kmers, weights=probs)[0]


def GibbsSampler(k: int, t: int, N: int, seqs: 'list[str]') -> 'list[str]':
    assert len(seqs) == t

    # randomly select motifs
    motifs_opt = []
    for i in range(t):
        ind = random.randrange(0, len(seqs[0]) - k + 1)
        motifs_opt.append(seqs[i][ind:ind+k])

    # repeat N times
    for i in range(N):
        # randomly select sequence
        ind = random.randrange(t)
        # construct profile (without selected sequence)
        prof = Profile([motifs_opt[j] for j in range(len(motifs_opt)) if j != ind])
        # get motifs
        motifs = [motifs_opt[j] if j != ind else ProfileRandomKmer(seqs[ind], k, prof) for j in range(t)]

        # score & update motifs_opt
        if Score(motifs) < Score(motifs_opt):
            motifs_opt = motifs

    return motifs_opt


def iterate(seqs: 'list[str]', k: int, t: int, N: int, n: int) -> 'list[str]':
    set_opt = None
    for i in range(n):
        motif_set = GibbsSampler(k, t, N, seqs)
        if set_opt is None or Score(motif_set) < Score(set_opt):
            set_opt = motif_set
    return set_opt


def RunIterate(*args):
    [k, t, N] = [int(x) for x in args[0].split()]
    seqs = args[1].split()
    return iterate(seqs, k, t, N, 100)
