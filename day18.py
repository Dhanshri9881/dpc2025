def count_divisors(n):
    count=0
    limit=int(n**0.5)
    for i in range(1,limit+1):
        if n%i==0:
            if i*i==n:
                count+=1
            else:
                count+=2
    return count
N=int(input())
print(count_divisors(N))
