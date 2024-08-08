def bank(x, y):
    for i in range(y):
        x = x + (x * 0.1)
    print(x)

bank(10000, 3)