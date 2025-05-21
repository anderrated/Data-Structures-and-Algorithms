def bfs(adj):
    # get number of vertices
    # length of adjacent list will be the number of vertices
    V = len(adj)

    # array for storing traversal
    result = []
    source_node = 0

    # create a queue for BFS
    # import double ended queue
    from collections import deque
    queue = deque()

    # mark all vertices as not visited
    visited = [False] * V

    # mark source node as visited an enqueue it
    visited[source_node] = True
    queue.append(source_node)

    # iterate over the queue
    while queue:
        current = queue.popleft()
        # append popped node to result
        result.append(current)

        # get all adjacent nodes of the current node
        # check if visited or not
        # if not visited, mark as visited and append to queue
        for x in adj[current]:
            if not visited[x]:
                visited[x] = True
                queue.append(x)

    return result


if __name__ == "__main__":
    adj_list = [[1,2], [0,2,3], [0,4], [1,4], [2,3]]
    ans = bfs(adj_list)
    for i in ans:
        print(i, end=" ")
