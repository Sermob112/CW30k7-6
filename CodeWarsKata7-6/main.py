#
# Complete the function that counts the number of unique consonants in a string (made up of printable ascii characters).
#
# Consonants are letters used in English other than "a", "e", "i", "o", "u". We will count "y" as a consonant.
#
# Remember, your function needs to return the number of unique consonants - disregarding duplicates. For example,
# if the string passed into the function reads "add", the function should return 1 rather than 2, since "d" is a duplicate.
#
# Similarly, the function should also disregard duplicate consonants of differing cases.
# For example, "Dad" passed into the function should return 1 as "d" and "D" are duplicates.
# "add" ==> 1
# "Dad" ==> 1
# "aeiou" ==> 0
# "sillystring" ==> 7 "abcdefghijklmnopqrstuvwxyz" ==> 21


text =  "sillystring"
# "Count my unique consonants!!" ==> 7
CONSONANTS = set('bcdfghjklmnpqrstvwxyz')
def count_consonants(text):
    result = 0
    ss = [i for i in text.lower() if i in 'bcdfghjklmnpqrstvwxyz']
    output = []
    for x in ss:
        if x not in output:
            output.append(x)
    return len('CONSONANTS'.intersection(text.lower()))
    return len(output)




print(count_consonants(text))

# for i in new_ss:
#     if (i == new_ss[j]):
#         j = + 1
#         if (j >= len(new_ss)):
#             j = len(new_ss)
#         result = len(new_ss) - 1
#     else:
#         result = len(new_ss)
#     j = j + 1
#     if (j >= len(new_ss)):
#         return result
# return result