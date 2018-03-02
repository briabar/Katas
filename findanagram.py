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

print(question1("udacity", "ua"))
