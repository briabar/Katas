#check if any permutation of a given string s is a palendrom
#Reasoning: Any palandrom will have at most one odd numbered character
#           the rest will be even.  catac would have t mommmom would have m
#           and moom has no odd character.
from collections import Counter
def palen_perm(s):
    counter = Counter()
    s = s.replace(' ', '')
    for char in s:
        counter[char] += 1
    for char in s:
        if counter[char] % 2 != 0:
            counter['single'] += 1
            if counter['single'] > 1:
                return False
    return True


print(palen_perm("caact"))
