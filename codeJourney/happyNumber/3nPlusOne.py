def ThreeNPlusOne(n1, n2):

    max_length = 0

    for x in range(min(n1, n2), max(n1, n2) + 1):
        count = 1
        n=x

        while n != 1:
            if n % 2 == 0: # if even
                n = n //2
            else: #if odd
                n = 3 * n + 1
            count += 1

        if count > max_length:
            max_length = count

    return max_length


    
def main():
    while True:
        try:
            n1, n2 = map(int, input().split())

            result = ThreeNPlusOne(n1, n2)

            print(n1, n2, result)

        except EOFError:
            break

main()

