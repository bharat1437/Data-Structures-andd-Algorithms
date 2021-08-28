def printFirstItemThenFirstHalfThenSayHi100Times(items):
    print(items[0])

    middleIndex = items.length / 2
    index = 0;

    while (index < middleIndex):
        print(items[index])
        index + 1

    for i in range(100):
        print('Hi')

# In above case one for loop is running contantly for 100 times irrespective of number  of elements in items.
# Therefore we can ignore the constant loop since items goes with 1M elements then looping through 100 items is negligible.
# Also we can ignore O(1) as well.

# while loop with O(n/2) can also be considered as O(n) since complexity is increasing lenearly.