
def list_files(current_node, current_path=""):
    path_list = []
    new_path = ""
    for node in current_node:
        new_path = current_path + '/' + str(node)
        if current_node[node] == None:
            
            path_list.append(new_path)
        else:
            
            path_list.extend( list_files( current_node[ node ], new_path ) ) 
    return path_list