def loopThroughBoxes(boxes, boxes1):
  for i in boxes:
    print(i)
  for j in boxes1:
    print(j)

#In this case big O notation won't be O(n) since elements in boxes and boxes1 can be different and both loops are different as well.
# Therefore Big O for this is O(a + b)