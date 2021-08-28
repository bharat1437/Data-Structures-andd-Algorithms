#Merge sorted array
# Array1 = [2, 4, 6, 31]
# Array2 = [3, 5, 7, 30]
# Output = [2, 3, 4, 5, 6, 7, 30, 31]

# First approach would be to join two list and sort them. We need to iterate through only one array which is small and then sort them.
# Second approch would be to use any existing in build functions to join two list and then sort them.

####################### Solution 1 ###########################################

Array1 = [2, 4, 6, 31]
Array2 = [3, 5, 7, 30]


def mergeArray(arr1, arr2):
    newArray = arr1.copy()
    for item in arr2:
        newArray.append(item)
    return newArray


def mergeSortedArray(narray1, narray2):
    len1 = len(narray1)
    len2 = len(narray2)

    if len1 >= len2:
        mergedArr = mergeArray(narray1, narray2)
    else:
        mergedArr = mergeArray(narray2, narray1)

    return mergedArr


new = mergeSortedArray(Array1, Array2)
new.sort()
print(new)

####################### Solution 1 ###########################################

####################### Solution 2 ###########################################

# Since both arrays are already sorted, we can compare items in both arrays at same position and insert into new array.

def mergeSortedArray2(array1, array2):

    merged = []
    if len(array1) == 0:
        return array1
    if len(array2) == 0:
        return array2

    lenArray1 = len(array1)
    lenArray2 = len(array2)

    i = 0
    j = 0

    while lenArray1 != i and lenArray2 != j:
        if array1[i] <= array2[j]:
            merged.append(array1[i])
            i += 1
        else:
            merged.append(array2[j])
            j += 1
    return merged + array1[i:] + array2[j:]

print(mergeSortedArray2(Array1, Array2))

####################### Solution 2 ###########################################

####################### Solution 3 ###########################################


newArray = Array1 + Array2
newArray.sort()
print(newArray)

####################### Solution 3 ###########################################






