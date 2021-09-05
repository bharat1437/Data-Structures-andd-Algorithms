# Google question
# Given an array = [2, 5, 1, 2, 3, 5, 1, 2, 4]
# It should return 2

# Given an array = [2, 1, 1, 2, 3, 5, 1, 2, 4]
# It should return 1

# Given an array = [1, 2, 3, 4]
# It should return None

# Time complexity of function is O(n)
# Space complexity of function is O(n)

def findFirstRecurringElement(array1):
    emptyDic = {}
    if len(array1) == 0:
        return "Empty Array!!!"
    else:
        for item in array1:
            if item in emptyDic.keys():
                return item
            else:
                emptyDic[item] = 1
                print(emptyDic)


print(findFirstRecurringElement([2, 5, 1, 2, 3, 5, 1, 2, 4]))