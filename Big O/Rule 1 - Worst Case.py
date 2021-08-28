
nemo = ['bharat','shweta','nemo']

def findNemo1(arr):
  for i in arr:
    if (i == 'nemo'):
      print("Found Nemo!!")
      break
    print("running!!!!")

findNemo1(nemo)

# We have to always consider worst case in which the code can execute.
# As in the case of above code, nemo can be first element which will give us O(1)
# but it can also be last element which gives us O(n).
# Therefore in such cases always go for O(n) as Big O notation