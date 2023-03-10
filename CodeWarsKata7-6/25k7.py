# The parameters (divisor, bound) passed to the function are only positive values .
# It's guaranteed that a divisor is Found .
# Input >> Output Examples
# maxMultiple (2,7) ==> return (6)
# Explanation:
# (6) is divisible by (2) , (6) is less than or equal to bound (7) , and (6) is > 0 .
#
# maxMultiple (10,50)  ==> return (50)
# Explanation:
# (50) is divisible by (10) , (50) is less than or equal to bound (50) , and (50) is > 0 .*
#
# maxMultiple (37,200) ==> return (185)
# Explanation:
# (185) is divisible by (37) , (185) is less than or equal to bound (200) , and (185) is > 0 .



def max_multiple(divisor, bound):
    # for i in range(bound+1):
    #     if i % divisor == 0:
    #         b = i
    #         if(b >= 0):
    #             t = b
    return bound - (bound % divisor)
    # return t
print(max_multiple(37,200))