
#  this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.
#
# Examples
# high_and_low("1 2 3 4 5")  # return "5 1"
# high_and_low("1 2 -3 4 5") # return "5 -3"
# high_and_low("1 9 3 4 -5") # return "9 -5"
# Notes
# All numbers are valid Int32, no need to validate them.
# There will always be at least one number in the input string.
# Output string must be two numbers separated by a single space, and highest number is first.


def high_and_low(numbers):
    # ...
    bib = []
    new_s = [i for i in numbers.split(' ')]
    u = list(map(int, new_s))
    maxix = max(u)
    minin = min(u)
    bib.append(maxix)
    bib.append(minin)
    g = list(map(str, bib))
    result =' '.join(g )
    nn = [int(s) for s in numbers.split(" ")]
    return "%i %i" % (max(nn), min(nn))
    return result
print(high_and_low('1 42 3 -9 5'))