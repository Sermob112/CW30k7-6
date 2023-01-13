# There is an array with some numbers. All numbers are equal except for one. Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.

# def find_uniq(arr):
#     for i in arr:
#         for j in arr:
#             if(i != j):
#                 return j
#     return i

def find_uniq(arr):
    arr1 = []
    arr2 = []
    for i in range(0, len(arr) // 2):
        arr1.append(arr[i])
    for i in range(len(arr) // 2, len(arr)):
        arr2.append(arr[i])
    cont = set(arr1)
    cont2 = set(arr2)
    cont3 = cont ^ cont2
    a = list(cont3)
    s = a[0]

    s = set(arr)
    for e in s:
        if arr.count(e) == 1:
            return e
    return type(s)

print(find_uniq([0.55,1,1,1,1,1,1]))
# print(find_uniq([1,1,1,5,1,1,1]))
# arr1= []
# arr2 = []
# arr = [1,1,1,4,1,1,1]
# for i in range(0,len(arr)//2):
#     arr1.append(arr[i])
# for i in range(len(arr)//2,len(arr)):
#     arr2.append(arr[i])
# cont = set(arr1)
# cont2 = set(arr2)
# cont3 =cont ^ cont2
# print(cont3)