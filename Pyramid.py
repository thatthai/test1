row = int(input())
col = (2*row) - 1

n = 0
m = 0

while n < 3 :
    while m <= col :
        if m >= row - n and m <= row + n  :
            print("*", end = "")
        else :
            print(" ", end ="")
        m += 1
    n += 1
    print("")
    m = 0