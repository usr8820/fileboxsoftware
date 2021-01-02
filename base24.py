command = ['base']

l1 = ['A', 'B', 'C', 'D', 'E', 'F']
l2 = ['10', '11', '12', '13', '14', '15']
def base(num, base, tbase):
    try:
        a = 0
        b = 0
        num = list(num)
        for i in num:
            if i in l1:
                num[num.index(i)] = l2[l1.index(i)]
        for i in range(len(num)):
            a += int(num[b]) * (base ** (len(num) - b - 1))
            b += 1
        num = [str(a % tbase)]
        a = a // tbase
        while (a != 0):
            num = [str(a % tbase)] + num
            a = a // tbase
        for i in num:
            if i in l2:
                num[num.index(i)] = l1[l2.index(i)]
        return ''.join(num)
    except Exception as e:
        print('Something was wrong...')
        print('Traceback:', repr(e))
        return