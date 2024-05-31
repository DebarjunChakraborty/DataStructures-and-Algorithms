from collections import deque
def tree_height(n, parents):
    tree = [[] for _ in range(n)]
    root = None
    for i in range(n):
        if parents[i] == -1:
            root = i
        else:
            tree[parents[i]].append(i)
    def bfs(root):
        max_height = 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            max_height = max(max_height, depth)
            for child in tree[node]:
                queue.append((child, depth + 1))
        return max_height
    return bfs(root)
n = int(input())
parents = list(map(int, input().split()))
print(tree_height(n, parents))
