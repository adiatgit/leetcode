from rcviz import callgraph, viz
@viz
def generateParenthesis(n,arr,i):
    if i == n:
        print(arr)
        output.append(arr)
        print("output ->", output)
        return
    arr[i] = 0
    generateParenthesis(n, arr, i + 1)
    arr[i] = 1
    generateParenthesis(n, arr, i + 1)
    return output
n = 2
arr = [None] * n

# Print all binary strings
output = []
print generateParenthesis(n, arr, 0, output)
callgraph.render
("parenthesis.png")
