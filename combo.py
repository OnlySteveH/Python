def combo(iter1, iter2):
    output = []
    for i in range(0, len(iter1)):
        # tuple = (iter1[i], iter2[i])
        output += (iter1[i], iter2[i]),
    return output


print(combo("abcdefghijklmnopqrstuvwxyz", "12345678901234567890123456"))
