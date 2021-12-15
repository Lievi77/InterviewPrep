"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # remember, graph problems often require a modification of graph traversing algorithms
        if not node:
            return node

        # my approach: DFS

        visited = {}  # holds original -> clone mapping

        stack = [node]

        # initial clone
        visited[node] = Node(node.val)

        while stack:
            curr = stack.pop(-1)

            # for every edge
            for neighbor in curr.neighbors:
                # do DFS
                # how do we avoid cycles?
                # use the visited dict

                if not visited.get(neighbor):
                    # Clone and add to visited
                    visited[neighbor] = Node(val=neighbor.val)
                    # add to stack
                    stack.append(neighbor)

                # in the neighbors of the cloned node, append the cloned neighbor
                visited[curr].neighbors.append(visited[neighbor])

        return visited[node]
