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
            break
        result_now = [0,0]
        result_now[0] = vertex
        for mark in marked:
            distance = collections.defaultdict(lambda: float('inf'))
            (is_connected, dist_from_vertex) = bfs(graph, vertex, mark, distance)
            if(is_connected):
                result_now[1] += dist_from_vertex[mark]
                print('dist of {0} from {1}'.format(vertex, mark),result_now[1])
        if result_now[1] < result[0][1] and result_now[0] not in marked:
            result.clear()
            result = [[0,0]]
            result[0] = [result_now[0],result_now[1]]
        elif result_now[1]==result[0][1]:
            result.append([result_now[0],result_now[1]])    
    return result

graph = {0: [1, 2, 3], 1: [0,2], 2: [0,4], 3:[0], 4:[2]}
marked = [3, 4]
# dist = collections.defaultdict(lambda: float('inf'))
# bfs(graph, 0, 4, dist)
print(find_node(graph,marked))