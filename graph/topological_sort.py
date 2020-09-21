import collections

def topological():
    """トポロジカルソート (有向グラフ)

    Vars:
        n (int):     頂点数
        edge (list): 辺に関するリスト (edge[i]: iを始点に持つ辺の終点のリスト)
    
    Returns:
        list: トポロジカル順序
    """
    in_degree = [0] * n
    for i in range(n):
        for v in edge[i]:
            in_degree[v] += 1
    
    nodelist = collections.deque()
    for i in range(n):
        if in_degree[i] == 0:
            nodelist.append(i)
    
    res = []
    while nodelist:
        p = nodelist.popleft()
        for q in edge[p]:
            in_degree[q] -= 1
            if in_degree[q] == 0:
                nodelist.append(q)
        
        res.append(p)
    
    return res


# Driver Code
if __name__ == "__main__":
    n = 6
    edge = [[1],
            [2],
            [],
            [1, 4],
            [5],
            [2]
            ]
    print(topological())
    # [0, 3, 1, 4, 5, 2]