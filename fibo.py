def fibo(n):
    """フィボナッチ数列を表示"""
    a, b = 0, 1
    while b < n:
        print(b)
        a, b = b, (a + b)

        
def fibo2(n):
    """フィボナッチ数列をリストで返す"""
    rtn = []
    a, b = 0, 1
    while b < n:
        rtn.append(b)
        a, b = b, (a + b)
    return rtn
