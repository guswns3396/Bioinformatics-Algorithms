from .ba2d import ProfileMostProbableKmer, Score
from .ba2e import Profile

import random


def RandomizedMotifSearch(seqs: 'list[str]', k: int, t: int) -> 'list[str]':
    assert len(seqs) == t
    N = len(seqs[0])
    # randomly select motifs
    motifs_opt = []
    for i in range(t):
        ind = random.randrange(0, N - k + 1)
        motifs_opt.append(seqs[i][ind:ind+k])
    while True:
        # construct profile
        prof = Profile(motifs_opt)
        # find motifs using profile
        motifs = []
        for seq in seqs:
            motifs.append(ProfileMostProbableKmer(seq, k, prof))
        # compare score of motifs
        if Score(motifs) < Score(motifs_opt):
            motifs_opt = motifs
        else:
            return motifs_opt


def iterate(seqs: 'list[str]', k: int, t: int, n: int) -> 'list[str]':
    set_opt = None
    for i in range(n):
        motif_set = RandomizedMotifSearch(seqs, k, t)
        if set_opt is None or Score(motif_set) < Score(set_opt):
            set_opt = motif_set
    return set_opt


def RunIterate(*args):
    [k, t] = [int(x) for x in args[0].split()]
    seqs = args[1].split()
    return iterate(seqs, k, t, 100)
