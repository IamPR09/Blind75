"""
# Define a Tree

                      a
                     / \
                  None None            

"""

from typing import Optional


class Node :
    def __init__(self, data) :
        self.left = None
        self.right = None
        self.data = data

sampleTree = [Node]
sampleTree = ["a","b","j"]
print(sampleTree)