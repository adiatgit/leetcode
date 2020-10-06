def BFS(root, level, dict1):
    if level in dict1:
        dict1[level].append(root.val)
    else:
        dict1[level] = [root.val]
    if(root.left):
        BFS(root.left, level+1, dict1)
    if(root->right):
        BFS(root.right, level+1, dict1)

BFS[3,9,20,null,null,15,7]