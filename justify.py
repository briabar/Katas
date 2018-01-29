# Your task in this Kata is to emulate text justification in monospace font.
#You will be given a single-lined text and the expected justification width.
#The longest word will never be greater than this width.
#
# Here are the rules:
#
#     Use spaces to fill in the gaps between words.
#     Each line should contain as many words as possible.
#     Use '\n' to separate lines.
#     Gap between words can't differ by more than one space.
#     Lines should end with a word not a space.
#     '\n' is not included in the length of a line.
#     Large gaps go first, then smaller ones: 'Lorem---ipsum---dolor--sit--amet' (3, 3, 2, 2 spaces).
#     Last line should not be justified, use only one space between words.
#     Last line should not contain '\n'
#     Strings with one word do not need gaps ('somelongword\n').
#
# Example with width=30:
#
# Lorem  ipsum  dolor  sit amet,
# consectetur  adipiscing  elit.
# Vestibulum    sagittis   dolor
# mauris,  at  elementum  ligula
# tempor  eget.  In quis rhoncus
# nunc,  at  aliquet orci. Fusce
# at   dolor   sit   amet  felis
# suscipit   tristique.   Nam  a
# imperdiet   tellus.  Nulla  eu
# vestibulum    urna.    Vivamus
# tincidunt  suscipit  enim, nec
# ultrices   nisi  volutpat  ac.
# Maecenas   sit   amet  lacinia
# arcu,  non dictum justo. Donec
# sed  quam  vel  risus faucibus
# euismod.  Suspendisse  rhoncus
# rhoncus  felis  at  fermentum.
# Donec lorem magna, ultricies a
# nunc    sit    amet,   blandit
# fringilla  nunc. In vestibulum
# velit    ac    felis   rhoncus
# pellentesque. Mauris at tellus
# enim.  Aliquam eleifend tempus
# dapibus. Pellentesque commodo,
# nisi    sit   amet   hendrerit
# fringilla,   ante  odio  porta
# lacus,   ut   elementum  justo
# nulla et dolor.

def justify2(array, width):
    result = ''
    for line in array:
        # print("line top: "+line)
        num_spaces = line.count(' ')
        smallest_space = ' '
        if num_spaces > 0:
            smallest_space = ' '
            if len(line) < width:
                line2 = ''
                for char in line:
                    print(char)
                    if char is smallest_space:
                        print(2)
                        char += ' '
                    line2 += char
                smallest_space += ' '
                line = line2
            num_spaces -= 1
        result += line + '\n'
    return result[:-1]
    # return result

def justify(text, width):
    word_array = text.split()
    line = ""
    i = -1
    result = []
    for word in word_array:
        i += 1
        if len(line) + len(word) <= width:
            line += word + ' '
        else:
            result.append(line[0:-1])
            line = ""
            line += word + ' '
        if i == len(word_array) - 1:
            result.append(line[:-1])
            final = ''
            print "CHEESE: " + str(result)
            for line in result:
                # print("line top: "+line)
                num_spaces = line.count(' ')
                smallest_space = ' '
                if num_spaces > 0:
                    smallest_space = ' '
                    if len(line) < width:
                        line2 = ''
                        for char in line:
                            if char is smallest_space:
                                char += ' '
                            line2 += char
                        smallest_space += ' '
                        line = line2
                    num_spaces -= 1
                final += line + '\n'
            return final[:-1]



print(justify("Lorem ipsum dolor sit     amet,", 30))
