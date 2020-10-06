def isHappy(n):
    try:
        while n != 1:
            number = 0
            for i in str(n):
                number += int(i)**2
            n = number
            if n == 1:
                return True
    except:
        return False
print(isHappy(2))