def plusOne(digits):
    i = len(digits) - 1
    while i >= 0:
        if (digits[i] < 9):
            digits[i] = digits[i]+1
            i = -1
            return digits
        digits[i] = 0
        i -= 1
    return digits


def main():
    digits = [5,9]
    plusOne(digits)
    print(digits)

main()