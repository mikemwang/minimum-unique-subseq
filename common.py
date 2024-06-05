def get_all_subsequences(s: str) -> list:
    """
    Get all subsequences of a string s, ignoring the empty subsequence
    """
    result = []
    for i, c in enumerate(s):
        subseqs = get_all_subsequences(s[i+1:])
        result += [c]
        result += [c + subseq for subseq in subseqs]
    return result