def topKFrequent(nums, no):
    freq = {}
    for i in nums:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print(freq)
    output = []
    for i in range(no):
        pp = max(freq, key=freq.get)
        output.append(pp)
        del freq[pp]
    return output
    # freq2 = {v: k for k, v in freq.iteritems()}
    # print(freq2)
    output = []
    freq2 = {}
    for k, v in freq.items():
        freq2[v] = freq2.get(v, [])
        freq2[v].append(k)
    print(freq2)
    for i in range(no):
        t = max(freq2)
        output.append(freq2[t][0])
        if len(freq2[t]) >0:
            freq2[t].pop()
        if len(freq2[t]) == 0:
            del freq2[t]
    return output

print(topKFrequent([1,1,1,2,2,3,3],2))