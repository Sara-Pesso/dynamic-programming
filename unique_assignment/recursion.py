def dfs(assigned_count, assigned_node, obj, obj_to_node, total_nodes, total_objs):

    # Basis: if all objs have been assigned, return 1 to stop recursion
    if assigned_count == total_nodes:
        return 1

    # OR, if we've looked at all possible objs, but not all nodes are assigned, stop
    if obj > total_objs:
        return 0

    # Case: skip current obj (i.e., go straight to obj + 1)
    perms = dfs(assigned_count, assigned_node, obj + 1, obj_to_node, total_nodes, total_objs)

    # Assign the obj to each node it is allowed to be assigned to
    for node in obj_to_node[obj]:
        # Check if the node has already been assigned an obj
        if not assigned_node[node]:
            # Assign
            assigned_node[node] = True

            #Recurse 
            perms += dfs(assigned_count + 1, assigned_node, obj + 1, obj_to_node, total_nodes, total_objs)

            #Backtrack: unassign to evaluate other perms
            assigned_node[node] = False

    return perms

def num_perms(objs):
    num_nodes = len(objs)
    num_objs = max(map(max, objs))

    #Map each obj to the allowed nodes
    obj_to_nodes = [[] for _ in range(num_objs + 1)]
    for i in range(num_nodes):
        for obj in objs[i]:
            obj_to_nodes[obj].append(i)

    # initialize list to track assignments
    assigned_nodes = [False] * num_nodes

    # Recursion
    return dfs(0, assigned_nodes, 1, obj_to_nodes, num_nodes, num_objs)

if __name__ == "__main__":
  
    # caps = [[0, 1, 2], [0, 1], [2, 3], [3, 4]]
    caps = [[1, 2, 3], [1, 2], [3, 4], [4, 5]]

    # TODO: needs a leading, empty list in obj_to_nodes for some reason....
    print(num_perms(caps))