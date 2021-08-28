arr = ['a', 'b', 'c']

def printAllItems(arr):
  for i in arr:
    for j in arr:
      print(i+j)

printAllItems(arr)

# for recursive loops Big O notation is O(n*n) or O(n^2)