if __name__ == '__main__':
    m = list(range(1, 21))
    print("Введите начало диапазона:\n")
    a = int(input())
    print("\n")
    print("Введите конец диапазона:\n")
    b = int(input())
    print("\n")
    # массив индексов
    im = []
    for i in range(len(m)):
        if (m[i] >= a) and (m[i] <= b):
            im.append(i)

    print(im)