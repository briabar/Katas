
def is_rotation(s1,s2):
    i = 1
    s2temp = ""
    s1temp = ""
    while not s2temp == s1temp:
        s1temp = s1[i:-i]
        s2temp = s2[i:-i]
        print s1temp
        i += 1

is_rotation("waterbottle", "erbottlewat")
