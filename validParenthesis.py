class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_par = { '(' : ')', "[" : ']', "{" :"}" }
        stack1 = []
        stackptr = -1
        for i in s:
            if i in dict_par:
                stack1.append(i)
                stackptr=stackptr+1
            else:
                if(len(stack1) >0):
                    first = stack1.pop()
                    if(dict_par[first] == i):
                        stackptr=stackptr-1
                else:
                    return False
        if(stackptr == -1):
            return True
        return False
