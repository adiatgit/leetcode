def removeOuterParentheses(S):
    def checkBalanced(pString):
        pStack=[]
        for i in pString:
            if i =="(":
                pStack.append("(")
            else:
                pStack.pop()
            if(len(pStack) == 0):
                return False
        return
    print(S[1:-1])                
    if(checkBalanced(S[1:-1])):
        print S[1:-1]
    else:
        print ""
    return
removeOuterParentheses("(()())(())")
