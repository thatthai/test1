row = int(input())
col = (2*row) - 1

n = 1
m = 1

while n <= 3 :
    while m <= col :
        if m >= row - (n-1) and m <= row + (n-1)  :
            print("*", end = "")
        else :
            print(" ", end ="")
        m += 1
    n += 1
    print("")
    m = 1
    