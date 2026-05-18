def main():
    t = int(input())   # number of test cases

    for i in range(1, t + 1):
        n = int(input())

        if isHappy(n):
            print("Case #" + str(i) + ": " + str(n) + " is a Happy number.")
        else:
            print("Case #" + str(i) + ": " + str(n) + " is an Unhappy number.")


def isHappy(number):
    number = int(number)
    seen = set()

    while number != 1 and number not in seen:
        seen.add(number)
        digits = [int(d) for d in str(number)] # splits number into digits
        number = sum(d**2 for d in digits) # adds the digits back into a number
    return number == 1


main()