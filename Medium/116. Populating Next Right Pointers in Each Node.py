# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def bfs(self, nodes: List[Node]) -> None:
        # Base Case
        if None in nodes:
            return None

        # Connect Same Level Nodes
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i + 1]
        else:
            nodes[-1].next = None

        # BFS
        next_nodes = []
        for node in nodes:
            next_nodes.append(node.left)
            next_nodes.append(node.right)

        self.bfs(next_nodes)

    def connect(self, root: Optional[Node]) -> Optional[Node]:
        nodes = [root]
        self.bfs(nodes)
        return root
