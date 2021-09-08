# Graph are data structures where each node can be connected to multiple nodes. There is no fixed structure/sequence
# in which they will be connected like social networking sites. Each individual can have multiple friends and they
# can eventually be connected to different friends.
# Trees, linked lists are also kind on graphs.

# Types of graphs
# 1. Directed vs undirected graphs - https://www.educative.io/edpresso/directed-graphs-vs-undirected-graphs
# Directed - kind of graph used by LinkedIn where one individual can follow another but other doesn't have to follow
# back. Undirected is used in facebook where once friend request is accepted both can friends now.
# 2. Weighted vs unweighted graphs - https://medium.com/tebs-lab/types-of-graphs-7f3891303ea8
# 3. Cyclic vs acyclic - Cyclic are the ones where one can come back to first node.

############################### test code###################################################
# import pandas as pd
# data = pd.read_csv('C://Users//BHARAT//Desktop//Test.csv')
# dataNew = data.set_index(data['Col1']).to_dict()
# test = dataNew['Col2']
# # test = {'A': 'B', 'B': 'C', 'C': 'D', 'E': 'F', 'X': 'Y', 'Y': 'Z'}
# for val in test.keys():
#     initialVal = test[val]
#     while initialVal in test.keys():
#         initialVal = test[initialVal]
#     test[val] = initialVal
#
# new = pd.DataFrame(list(test.items()), columns=['column1', 'column2'])
# print(test)
# print(new)

############################### test code###################################################

# Graph data.

# There are various ways in which we can build graphs. DAG(Direct Acyclic Graph) is used  in multiple  use cases
# even spark generates DAG for execution which is steps in which code will get executed.
# DAG is nothing but combination of trees and linked lists.
# Suppose we need to build below graph
#           2------0
#          /  \
#         1 -- 3
# In above example, 0 is connected to 2, 2 is connected to 1 & 3, 1 is connected to 2 & 3, 3 is connected to 1 & 2
# this can be implemented in three ways
# 1. Edge list - List of all connections(edge)
# [[0, 2],[1, 2], [2, 3], [1, 3]]
# 2. Adjacent list
# {0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]}
# 3. Matrix
# [
#    [0, 0, 1, 0],
#    [0, 1, 1, 0]
#    [1, 1, 0, 1]
#    [0, 1, 1, 0]
# ]
