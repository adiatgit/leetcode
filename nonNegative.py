def solution(N):
    x = sorted(str(N))[::-1]
    print(''.join(x))
    return x
solution(553)