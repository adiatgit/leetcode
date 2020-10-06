s="IX"
d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
count = temp = 0
for i in s:
    if ((temp == 1) & (i != "I")):
        count = count + d[i] - 2
    else:
        count = count + d[i]
    if i == "I":
        temp = 1
    else:
        temp = 0
print(count)