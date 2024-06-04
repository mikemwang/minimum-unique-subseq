# Minimum Unique Subsequences
## Introduction
A *subsequence* of a string is any sequence of characters that appears in the 
same order in the string, not necessarily contiguously.

For example: "tw" is a subsequence of "typewriter". The characters "t" and "w"
appear in "typewriter" in that order, and it does not matter that they are 
separated by other characters in the string.

A *unique* subsequence of a string is a subsequence that is present in only 
that string among a collection of strings. 

A *minimum* unique subsequence is the shortest unique subsequence of a string.
There may be multiple minimum unique subsequences.

## Properties
A string $s$ of length $n$ has $2^n-1$ subsquences. There are 2 choices for 
each character (included or not included in the subsequence) so there are
$2^n$ ways to choose characters to include. This includes the case where no
characters are picked - the empty subsequence - so we subtract 1 yielding
$2^n-1$.

It's possible that a minimum unique subsequence does not exist for $s$ among a
group of strings $G$, since $s$ itself may be a subsequence of another string
in the group.

## Algorithm
### Brute Force
Keep a dictionary `D` of subsequences to strings. 

Keep a dictionary `S` of strings to a sets of subsequences.

Keep a dictionary `N` of strings to ints, initialized to null. This will track
the shortest subsequence found for that string.

For each string compute its subsequences. 

For each subsequence check if it is present in the dictionary. 

If so, remove that subsequence from `S[D[sub]]` and move on.

Otherwise,

If `len(sub)` is less than `N[string]`, `N[string]=len(sub)` and 
`S[string]={sub}`, `D[sub]=string`

If `len(sub)` is equal to `N[string]`, `S[string].add(sub)`, `D[sub]=string`

Else do nothing

The dictionary `S` is the final answer, containing all the minimum
unique subsequences (if any) for each string.

The time complexity of this solution is $O(n2^m)$, where $n$ is the number of
strings and $m$ is the maximum length of a string.

The space complexity is $O(n2^m)$, since in the worst case we store every
subsequence of every string.