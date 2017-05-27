def combiner(args):
    strings = ""
    number = 0
    for arg in args:
        if isinstance(arg, str):
            strings = "{}{}".format(strings, arg)
        if isinstance(arg, (int, float)):
            number += arg
    return strings + str(number)

print(combiner(['a', 1, 'b', 2, 'c', 3]))