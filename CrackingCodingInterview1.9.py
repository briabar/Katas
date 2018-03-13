def is_rotation(s1, s2):
    ''' String Rotation: Assume you have a method iSubstring which checks is one
    word is a substring of another. Given two strings, s1 and s2, write code to
    check if s2 is a rotation of s1 using only one call to isSubstring.'''
    if not len(s1) == len(s2):
        return False
    i = 1
    while i < len(s1):
        if s1[i:] == s2[0:-i] and s1[:i] == s2[-i:]:
            return True
        i += 1
    return False


# def is_rotation2(s1, s2):
#     ''' String Rotation: Assume you have a method isSubstring which checks if one
#     word is a substring of another. Given two strings, s1 and s2, write code to
#     check if s2 is a rotation of s1 using only one call to isSubstring.'''
#     if (not len(s1) == len(s2)) or len(s1) < 1:
#         return False
#     s1s1 = s1 + s1
#     return isSubstring(s1s1, s2)


print(is_rotation("waterbottle", "bottle"))
print(is_rotation("waterbottle", "erbottlewat"))
print(is_rotation("animal", "lanima"))
print(is_rotation("aaaabottle", "bottleeeea"))
