n = int(input())
sum = 0
while n > 1:
    m = n % 10
    n = n/10
    sum += int(m)
    if n < 1 and sum >= 10 :
        n = sum
        sum = 0
        
print(sum)
