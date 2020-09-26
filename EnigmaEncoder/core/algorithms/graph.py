import collections
# BFS algorithm
def bfs(graph, root, dest, dist):
    dist[root] = 0
    visited, queue = set(), collections.deque([root])
    visited.add(root)
    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                dist[neighbour] = dist[vertex] + 1
                #pred[neighbour] = vertex
                visited.add(neighbour)
                queue.append(neighbour)
                if neighbour == dest:
                    return True,dist
    return False,dist

def find_node(graph, marked):
    result = [[0,float('inf')]]
    for vertex in graph.keys():
        if vertex in marked:
            continue
        result_now = [0,0]
        result_now[0] = vertex
        for mark in marked:
            distance = collections.defaultdict(lambda: float('inf'))
            (is_connected, dist_from_vertex) = bfs(graph, vertex, mark, distance)
            if(is_connected):
                result_now[1] += dist_from_vertex[mark]
        if result_now[1] < result[0][1] and result_now[0] not in marked:
            result.clear()
            result = [[0,0]]
            result[0] = [result_now[0],result_now[1]]
        elif result_now[1]==result[0][1]:
            result.append([result_now[0],result_now[1]])    
    return result