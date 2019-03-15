import random
from fractions import Fraction

def zhengshu():
    fh = ['＋', '－', '×', '÷']
    a = random.randint(0, 3)
    n1 = random.randint(1, 100)
    n2 = random.randint(1, 100)
    result = 0
    if a == 0:
        result = n1 + n2
    elif a == 1:
        n1, n2 = max(n1, n2), min(n1, n2)
        result = n1 - n2
    elif a == 2:
        result = n1 * n2
    elif a == 3:
        n1, n2 = max(n1, n2), min(n1, n2)
        while n1 % n2 != 0:
            n1 = random.randint(1,100)
            n2 = random.randint(1,100)
            n1, n2 = max(n1, n2), min(n1, n2)
        result = int(n1/n2)
    print(n1, fh[a], n2, '=', end='')
    return result

def fenshu():
    fh = ['＋', '－', '×', '÷']
    a = random.randint(0, 3)
    t1 = random.randint(1, 100)
    t2 = random.randint(t1, 100)
    n1 = Fraction(t1, t2)
    t3 = random.randint(1, 100)
    t4 = random.randint(t1, 100)
    n2 = Fraction(t3, t4)
    result = 0
    if a == 0:
        result = n1 + n2
    elif a == 1:
        n1, n2 = max(n1, n2), min(n1, n2)
        result = n1 - n2
    elif a == 2:
        result = n1 * n2
    elif a == 3:
        n1, n2 = max(n1, n2), min(n1, n2)
        result = n1 / n2
    print(n1, fh[a], n2, '=', end='')
    return result

print('自动生成四则运算')
print('输入0000退出')
while True:
    a = random.randint(0, 4)
    if a == 0:
        result = fenshu()
        jg = input()
        if jg == '0000':
            break;
        sr = Fraction(jg)
        if sr == result:
            print('正确')
        else:
            print('错误，正确结果是:', result)
    else:
        result = zhengshu()
        jg = input()
        if jg == '0000':
            break;
        sr = int(jg)
        if sr == result:
            print('正确')
        else:
            print('错误，正确结果是:', result)