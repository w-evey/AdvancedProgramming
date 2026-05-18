def main():
    t = int(input())   # number of test cases

    for i in range(1, t + 1):
        print(maxSlices(i))

def maxSlices(n):
    n = int(n)
    if 0 <= n <= 210000000:
        result = (n * (n+1) // 2) + 1
        return result
    else:
        return False

main()
