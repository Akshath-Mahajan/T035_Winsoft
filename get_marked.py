
def get_marked(graph, decrypted):
    marked = []
    for vertex in graph.keys(): #graph is a dict
        if vertex in decrypted:
            marked.append(vertex)
    return marked

