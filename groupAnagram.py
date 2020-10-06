def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    output = []
    indices = {}
    for i in strs:
        x = sorted(list(i))
        print(i,x)
        output.append(('').join(x))
    for j in range(len(output)):
        if output[j] in indices:
            indices[output[j]].append(j)
        else:
            indices.update({output[j]:[j]})
    twolist = []
    for k in indices.values():
        new =[]
        for m in k:
            new.append(strs[m])
        twolist.append(new)
    return twolist

print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))