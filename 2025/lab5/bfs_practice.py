def bfs(adj):
    # get number of vertices
    V = len(adj)

    # result list
    res = []
    # source node
    source = 0

    # create double ended queue
    from collections import deque
    queue = deque()

    # set all visited to false
    visited = [False] * V

    # set source as visited
    visited[source] = True
    # append source node to queue
    queue.append(source)

    while queue:
        current = queue.popleft()
        res.append(current)
        for node in adj[current]:
            if not visited[node]:
                # set unvisited node to true
                visited[node] = True
                # append to queue
                queue.append(node)

    return res


if __name__ == "__main__":
    # adjacency list
    adj_list = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]

    result = bfs(adj_list)
    for node in result:
        print(node, end = " ")
