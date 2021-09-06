# Below is example of tree
#               1
#           /        \
#        2       3       4
#              /    \
#            5       6
#   Above tree has
# Parent Node = 1 , 3
# Child Nodes = 2, 3, 5, 5, 6
# Leaf node = 2, 4, 5, 6

# Linked list are also trees where they have only one node at each level
#
# Binary trees - Binary trees are the ones where parent will have max 2 child nodes. You can say 0/1.
#        Perfect Binary Tree                                 Full Binary Tree
#                 1                                                 1
#               /   \                                              /  \
#             2       3                                         2       3
#            /   \   /  \                                      /  \
#         4       5 6     7                                 4       5
#
# Perfect binary tree are very efficient and at all levels number of nodes will double.

# Binary trees have O(log N) big O Notation as explained below.
# Suppose we have a perfect Binary tree

# Level 0: 2^0 = 1
# Level 1: 2^1 = 2
# Level 2: 2^2 = 4
# Level 3: 2^3 = 8

# Number of nodes = 2^level-1 = 2^4 -1 = 15 Nodes
# log Nodes = level
# log 100 = 2
# 10^2 = 100

# Big O
# lookup - O(log N)
# insert - O(log N)
# delete - O(log N)

# Binary Search Trees
# There are two important aspects of binary search tree.
# 1. Each node on the left has values less than parent node and on the right has value greater than parent node
# 2. Each node has only two child nodes
# Example

#         101
#        /    \
#     33      106
#    /   \    /   \
# 31      53 45   150

# Above is example of balanced binary search tree.
# In case of unbalanced binary search tree - if
# 1. all the nodes get added to right
# 2. all nodes get added to left
# 3. some on left and all other on right
# 4. some on right and all other on left

# Such tree can have O(n) big O for lookup, insert and delete, since we are traversing on one side of tree as linked
# list

# If the tree are unbalanced then we can use AVL tree or Red/Black tree to make it more balanced.
# These are libraries available in all languages which we can use directly and it is not asked for implementation.
# Both these trees will automatically move nodes whenever they feel that tree is unbalanced as per algorithm.

# Binary Heap Tree
# 1. There can be max two child for each node.
# 2. Value of parent node is always greater than child nodes but cannot guarantee that left is smaller and right is
# larger as binary tree.
#               101
#              /   \
#           70      33
#          /    \    | \
#       55      65  28  1
#
# Insertion will be O(log N)
# Remove will be O(log N)
# However lookup can be O(N) - This is because if we can to search 1 in above tree, we may have to traverse through all
# nodes since we can't divide and rule here.

# Use below to visualize binary heap
# https://visualgo.net/en/heap?slide=1

# One example where we can use Binary heap rather than binary search tree is implementing priority queues.
# Priority queues are way of arranging nodes in a way where highest priority node gets to be top node
# If priority of someone more than top node arrives than top node is moved as child node and new node is placed as
# top node.
# Insertion happens from left to right and this is most of the times a balanced tree

