def isAlienSorted(words, order) -> bool:
    alien_dict = {}
    counter = 0
    for i in order:
        alien_dict[i] = counter
        counter += 1
    min_len = 9223372036854775807
    for i in words:
        if len(i) < min_len:
            min_len = len(i)
    for i in range(min_len):
        prev = alien_dict[words[0][i]]
        for j in words:
            if alien_dict[j[i]] < prev:
                return False
    return True
isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz")