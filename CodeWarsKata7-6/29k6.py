# Given n, take the sum of the digits of n. If that value has more than one digit,
# continue reducing in this way until a single-digit number is produced. The input will be a non-negative integer.
#
# Examples
#     16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
#MY SOLUTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def digital_root(n):
#     sum = 0
#     if(len(str(n)) == 1):
#         sum = n
#         return sum
#     new_l = []
#     nn = [int(s) for s in list(str(n))]
#     while len(nn) != 1:
#         sum = 0
#
#         for i in nn:
#             sum = sum + i
#
#         nn = [int(s) for s in str(sum)]
#     return sum
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
print(digital_root(444))
# s = 23
# st = str(s)
# e = st.split()
# new = [int(i) for i in st]
# print(new)
# def digital_root(n):
#     if len(list(str(n))) == 1:
#         return n
#     else:
#         nn = [int(s) for s in list(str(n))]
#         for i in nn:
#             nn.remove(i)
#             g = int(''.join(map(str, nn)))
#             return i + digital_root(g)



# n = 6
# print(len(list(str(n))))
# print(int(str(12)[1:]) + 3)
# if len(list(str(n))) > 1:
#     nn = [int(s) for s in list(str(n))]
# def factorial_recursive(n):
#     if n == 1:
#         return n
#     else:
#         return n*factorial_recursive(n-1)

# print(factorial_recursive(4))