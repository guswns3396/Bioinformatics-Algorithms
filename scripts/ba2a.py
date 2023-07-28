from .ba1j import Neighbors


def MotifEnumeration(Dna: list, k: int, d: int):
    patterns = set()
    dna_s0 = Dna[0]
    # iterate through all kmers in initial dna string
    for i in range(len(dna_s0) - k + 1):
        kmer = dna_s0[i:i + k]
        # get neighbors of kmer
        neighbors = Neighbors(kmer, d)
        # look at each neighbor of kmer
        for neighbor in neighbors:
            # default add
            inAllDNA = True
            # look at each dna
            for dna in Dna[1:]:
                # look at each kmer of dna
                # and create neighbors
                inDNA = False
                for j in range(len(dna) - k + 1):
                    pat = dna[j:j + k]
                    neighbors_pat = Neighbors(pat, d)
                    # see if given kmer in neighborhood
                    # no need to iterate rest of kmers if found
                    # go to next dna
                    if neighbor in neighbors_pat:
                        inDNA = True
                        break
                # if after looking at all kmers and their neighbors
                # and cannot find then not in all dna
                # thus no need to look at other dna
                if not inDNA:
                    inAllDNA = False
                    break
            if inAllDNA:
                patterns.add(neighbor)
    return patterns


def MotifEnumerationEff(Dna: list, k: int, d: int):
    # get all kmers & neighbors for all Dnas
    kmers_list = []
    for dna in Dna:
        kmers = set()
        for i in range(len(dna) - k + 1):
            kmers.update(Neighbors(dna[i:i+k], d))
        kmers_list.append(kmers)

    # find all kmers in kmers0 that are in all sets of kmers
    result = kmers_list[0]
    for i in range(1, len(kmers_list)):
        result.intersection_update(kmers_list[i])

    return result


def RunMotifEnumerationEff(*str_args):
    k, d = str_args[0].split()
    Dna = list(str_args[1].split())
    return MotifEnumerationEff(Dna, int(k), int(d))


def RunMotifEnumeration(*str_args):
    k, d = str_args[0].split()
    Dna = list(str_args[1].split())
    return MotifEnumeration(Dna, int(k), int(d))
