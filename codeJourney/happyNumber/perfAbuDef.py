def main():
    n = int(input())
    divisors=find_divisors(n)
    sum=0   
    for i in divisors:
        if i == n:
            pass
        else:
            sum = i+sum
    if sum==n:
        print("perfect")
    elif sum>n:
        print("abundant")
    else:
        print("deficient")

def find_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

main()