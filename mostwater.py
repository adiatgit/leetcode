def mostwater(height):
    max_water = 0
    for i in range(len(height)):
        for j in range(i+1,len(height)):
            abs_diff = min(height[i],height[j])*(j-i)
            if(abs_diff > max_water):
                max_water = abs_diff
    return max_water
def mostwaterUsingTwoPtr(height):
    l = 0
    max_area =0
    r= len(height)-1
    while(l<r):
        if(min(height[l],height[r])*(r-l) > max_area):
            max_area= min(height[l],height[r])*(r-l)
        if(height[l] < height[r]):
            l= l+1
        else:
            r=r-1
    return max_area
print mostwaterUsingTwoPtr([1,8,6,2,5,4,8,3,7])
