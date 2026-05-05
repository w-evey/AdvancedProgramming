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
    print(ThreeNPlusOne(1, 10))
    print(ThreeNPlusOne(100, 200))
    print(ThreeNPlusOne(201, 210))
    print(ThreeNPlusOne(900, 1000))

main()

# for x in range(n1, n2):
#     if n1 == 1:
#         return count
#     else:
#         if n1 % 2 == 0: # if even
#             n1 = n1/2
#             count = count + 1
#         else: #if odd
#             n1 = 3 * n1 + 1
#             count = count + 1

# count = 0
# while n1 != n2:
#     if n1 % 2 == 0: # if even
#         n1 = n1/2
#         count = count + 1
#     else: #if odd
#         n1 = 3 * n1 + 1
#         count = count + 1
# return count