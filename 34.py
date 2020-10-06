def searchRange(nums, target):
    locs = []
    def binarySearch(nums, l, r, target):
        if r >= l:
            m = int(l + (r - l) / 2)
            if nums[m] == target:
                return m
            elif target < nums[m]:
                return binarySearch(nums, l, m - 1, target)
            else:
                return binarySearch(nums, m + 1, r, target)
        return -1
    if len(nums) ==1:
        return [0, 0]
    pos = binarySearch(nums, 0, len(nums) - 1, target)
    locs.append(pos)
    if pos == -1:
        locs.append(-1)
        return locs
    if pos + 1 < len(nums):
        if nums[pos + 1] == target:
            locs.insert(1, pos + 1)
    if pos > -1:
        if nums[pos - 1] == target:
            locs.insert(0, pos - 1)
    if len(locs) == 1:
        locs.append(locs[0])
        return locs
    return locs
searchRange([1], 1)