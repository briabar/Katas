#find if a two strings are one edit apart from each other

def one_away(s1, s2):
    dif_counter = 0
    if len(s1) == len(s2):
        for ix in range(0,len(s1)):
            if s1[ix] != s2[ix]:
                dif_counter += 1
                if dif_counter > 1:
                    return False
        return True

    if len(s1) > len(s2):
        if s1[:-1] == s2:
            return True
        for ix in range(0, len(s1)):
         if s1[ix] != s2[ix]:
             if s1[:ix] + s1[ix+1:] != s2:
                 return False
             else: return True

    else:
        if s2[:-1] == s1:
            return True
        for ix in range(0, len(s2)):
         if s2[ix] != s1[ix]:
             if s2[:ix] + s2[ix+1:] != s1:
                 return False
             else: return True

print(one_away("hodrse", "horse"))
print(one_away("morse", "horse"))
print(one_away("horse", "horsg"))
print(one_away("orse", "horse"))
print(one_away("horse", "hors"))
print(one_away("dhodrse", "horse"))
