text = "My name is Bharat Chavan"
text1 = ""
text2 = "B"
# We need to reverse the string. One way is to create  one more list and append items backwards to it and we will achieve our goal
# However the time complexity for the problem would be O(n) and space  complexity would be O(n) since we are creating new list


def reverse1(text):
    if text == "" or len(text) == 1:
        return "Cannot perform reverse operation"
    lstSplit = list(text)
    reverseLst = []
    for i in range(len(lstSplit) - 1, -1, -1):
        reverseLst.append(lstSplit[i])
    return "".join(reverseLst)

#There are build in functions as well which we can use to get more cleaner code as shown below
def reverse2(text):
    if text == "" or len(text) == 1:
        return "Cannot perform reverse operation"
    lstSplit = list(text)
    lstSplit.reverse()
    return "".join(lstSplit)


reverse = reverse1(text1)
print(reverse)
