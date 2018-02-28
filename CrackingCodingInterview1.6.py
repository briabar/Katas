def s_comp(s):
    result_array = []
    result_string = ''
    result_array.append([s[0]])
    ix = 1
    while ix < len(s):
        if s[ix] == result_array[-1][-1]:
            result_array[-1].extend(s[ix])
            ix += 1
        else:
            result_array.append([s[ix]])
            ix += 1
    for ix in range(0, len(result_array)):
        if len(result_array[ix]) > 1:
            result_array[ix] = result_array[ix][0] + str(len(result_array[ix]))
        else:
            result_array[ix] = result_array[ix][0]
    return result_string.join(result_array)

print(s_comp("aaabccdeeee"))
