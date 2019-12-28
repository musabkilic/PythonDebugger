def main(a, b):
    x = a + b
    y = x * 2
    r = list(range(a, y))
    r[0] = 9
    r[:3], r[-3:] = r[-3:], r[:3]
    y = x * y
    d = {"alice" : 86, "bob": 79}
    d["alice"] += 8
    d["chloe"] = 98
    for i in range(x):
        j = i ** i
    print('Sample: ' + str(y))

def primeNumbersUpTo(n):
    for i in range(2, n):
        for j in range(2, int(i**.5)+1):
            if i % j == 0:
                break
        else:
            print(i)

if __name__ == "__main__":
    primeNumbersUpTo(10)
    main(2, 4)
