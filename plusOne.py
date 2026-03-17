def plusOne(digits):
    i = len(digits) - 1
    while i >= 0:
        if (digits[i] < 9):
            digits[i] = digits[i]+1
            i = -1
            return digits
        digits[i] = 0
        i -= 1
    digits.insert(0, 1)
    return digits


def main():
    digits = [1,2,3,4,5,6,7,8,9]
    plusOne(digits)
    print(digits)

main()