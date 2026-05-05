def main():
    print(maxSlices(5))
    print(maxSlices(10))
    print(maxSlices(-100))

def maxSlices(n):
    n = int(n)
    if 0 <= n <= 210000000:
        result = (n * (n+1) // 2) + 1
        return result
    else:
        return False

main()
