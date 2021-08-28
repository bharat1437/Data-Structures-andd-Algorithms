def printBoo(lst):
  for i in lst:
    print("Boooo!!!")

printBoo([1,2,3,4,5]) # O(1)

# Space is consumed when we create variables, data structures, functions etc.
# Inside above function we are not creating any additional variables except i. Therefore space complexity is O(1)


def printBoo2(lst):
  lst2 = []
  for i in lst:
    lst2.append(i)
  return lst2

l = printBoo2([1,2,3,4,5]) # O(n)
print(l)

# In this example, we are creating data structure of lenght n inside function which will consume space
# therefore space complexity is O(n)