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

def newtest():
    opr = ['＋', '－', '×', '÷']
    print('输入题库所需要的题目数量')
    n=int(input())
    rjg=[]
    m=0
    while m<=(n-1):
        fh = random.randint(0, 4)
        if fh==0:
            print(m+1,end='、')
            rjg.append(zhengshu())
            print(' ')
        else:
            print(m+1,end='、')
            rjg.append(fenshu())
            print(' ')
        m=m+1
    m=0
    print('答案：')
    while m<=(n-1):
        print(m+1,'、',rjg[m])
        m=m+1


print('1、四则运算')
print('2、制作题库')
n=int(input())
if n==1:
    print('input "0000" to Quit')
    while True:
        fh = random.randint(0, 4)
        if fh == 0:
            rjg = zhengshu()
            jg = input()
            if jg == '0000':
                break;
            sr = Fraction(jg)
            if sr == rjg:
                print('right')
            else:
                print('error. the Tight answer is', rjg)
        else:
            rjg = fenshu()
            jg = input()
            if jg == '0000':
                break;
            sr = int(jg)
            if sr == rjg:
                print('right')
            else:
                print('error. the Tight answer is', rjg)
if n==2:
    newtest()