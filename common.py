def get_all_subsequences(s: str) -> list:
    """
    Get all subsequences of a string s, ignoring the empty subsequence
    """
    result = []
    for i, c in enumerate(s):
        subseqs = get_all_subsequences(s[i+1:])
        result.append(c)
        for subseq in subseqs:
            result.append(c+subseq)
    return result