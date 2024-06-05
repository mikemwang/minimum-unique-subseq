from common import get_all_subsequences


def get_minimum_substrings_brute_force(strings):
    from collections import defaultdict
    word_to_subseqs = {s: set(get_all_subsequences(s)) for s in strings if s}
    
    result = {}
    for word, subseqs in word_to_subseqs.items():
        t = subseqs.copy()
        for w, s in word_to_subseqs.items():
            if w == word:
                continue
            t.difference_update(s)
        result[word] = t
    
    for word, subseqs in result.items():
        if not subseqs: continue
        d = defaultdict(set)
        for s in subseqs:
            d[len(s)].add(s)
        result[word] = d[min(list(d.keys()))]

    return result


if __name__=='__main__':
    print(get_minimum_substrings_brute_force(['a', 'a']))