def PatternCount(txt, pat):
    count = 0
    for i in range(len(txt) - len(pat) + 1):
        if txt[i:i + len(pat)] == pat:
            count += 1
    return count
