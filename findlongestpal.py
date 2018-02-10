def FindLongestPalRecursive(a):
    '''This is a dumb recursive function to find a palindrom.  It doesn't really
    work since it doesn't take into account unbalanced strings like:
    "XSDGREWEFmom"
    '''
    a = a.replace(" ","")
    if len(a) <= 1:
        a = False
        return a
    if a == a[::-1]:
        return a
    a = a[1:]
    if a == a[::-1]:
        return a
    a = a[:-1]
    if a == a[::-1]:
        return a
    return FindLongestPal(a)


def FindLongestPal(a):
    '''Same as above, but not recursive'''
    a = a.replace(" ","")
    while len(a) >= 1:
        if a == a[::-1]:
            return a
        a = a[1:]
        if a == a[::-1]:
            return a
        a = a[:-1]
        if a == a[::-1]:
            return a
    return False


def FindLongestPalReal(a):
    """This one actually works"""
    a = a.replace(" ", "")
    list_of_pal = []
    if a == a[::-1]:
        return a
    if len(a) <= 1:
        return a
    ix = 0
    #check2
    while ix < len(a) - 1:
        if a[ix] == a[ix+1]:
            list_of_pal.append([ix,ix + 1])
        if ix + 2 <= len(a)-1:
            if a[ix:ix+2] == a[ix+2:ix:-1]:
                list_of_pal.append([ix, ix + 1, ix + 2])
        ix += 1
    print list_of_pal
    ix = 0
    result = []
    for starts in list_of_pal:
        is_pal = True
        front = starts[0]
        end = starts[-1]
        while is_pal:
            result.append([len(starts), sorted(starts)])
            if front - 1 >= 0 and end + 1 <= len(a) - 1:
                if a[front - 1] == a[end + 1]:
                    starts.extend([front - 1, end + 1])
                    front -= 1
                    end += 1
                else: is_pal = False
            else: is_pal = False
    result = sorted(result)
    return a[result[-1][1][0]:result[-1][1][-1]+1]



print(FindLongestPalReal("cattaccattacblskddidmmooommm"))
# print(FindLongestPalRecursive("ac man a plan a canal panama"))
#
# print(FindLongestPal("ac man a plan a canal panama"))
