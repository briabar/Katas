# Given two strings s and t, determine whether some anagram of t is a substring
# of s. For example: if s = "udacity" and t = "ad", then the function returns
# True. Your function definition should look like: question1(s, t) and return a
# boolean True or False.

def question1(s,t):
    for char in t:
        answer = True
        if char in s:
            pass
        else:
            return False
    return answer



def question1_2(s,t):
    if len(t) > len(s):
        return False
    front = 0
    back = len(t)
    while back <= len(s):
        if set(s[front:back]) == set(t):
            return True
        else:
            front += 1
            back += 1
    return False

print(question1_2("udacity", "adic"))
print(question1_2("udacity", ""))  #True
print(question1_2("chicken is the  best meat money can buy", "uy"))  #True
print(question1_2("a", "chicken is the  best meat money can buy"))  #False
print(question1_2("", "asd"))  #False
