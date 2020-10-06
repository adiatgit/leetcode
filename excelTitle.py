import string
def excelTitle(n):
    mapping = {}
    index = 0
    title = ''
    for i in list(string.ascii_uppercase):
        mapping.update({index: i})
        index += 1
    while(n > 0):
        title += mapping[(n-1) % 26]
        n = (n-1) // 26
    return title[::-1]
print(excelTitle(700))
