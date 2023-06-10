def func(a, n, d):
    an = a + (n-1) * d
    return an


if __name__ == '__main__':
    m = []
    print("Введите первый элемент арифмитической прогрессии:\n")
    a = int(input())
    print("\n")
    print("Введите количество элементов прогрессии:\n")
    n = int(input())
    print("\n")
    print("Введите разность прогрессии:\n")
    d = int(input())
    print("\n")
    m.append(a)

    for i in range(n):
        if i == 0:
            continue
        else:
            m.append(func(m[0], i+1, d))

    print(m)



