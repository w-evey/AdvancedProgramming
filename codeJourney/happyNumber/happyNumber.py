def main():
    print(isHappy(1)) # true 
    print(isHappy(19)) # true
    print(isHappy(4)) # false


def isHappy(number):
    number = int(number)
    seen = set()

    while number != 1 and number not in seen:
        seen.add(number)
        digits = [int(d) for d in str(number)]
        number = sum(d**2 for d in digits)
    return number == 1


main()