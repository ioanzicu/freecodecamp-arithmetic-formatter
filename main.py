
from arithmetic_arranger import arithmetic_arranger

if __name__ == '__main__':
    # Too many problems error
    print(arithmetic_arranger(
        ['1 + 2', '1 + 2', '1 + 2', '1 + 2', '1 + 2', '1 + 2']))
    # Error: Incorrect problem format, expected operator1 +/- operator2 separated by one space, obtained: ...
    print(arithmetic_arranger(['1 + 2 4']))

    # Error: Numbers must only contain digits.
    print(arithmetic_arranger(
        ['1 + 2T']))

    # Error: Numbers must only contain digits.
    print(arithmetic_arranger(
        ['1T + 2']))

    # Error: Numbers cannot be more than four digits.
    print(arithmetic_arranger(
        ['112345 + 2']))

    # Error: Operator must be '+' or '-'.
    print(arithmetic_arranger(
        ['1 * 2']))

    # Error: Operator must be '+' or '-'.
    print(arithmetic_arranger(
        ['1 \ 2']))

    # Error: Operator must be '+' or '-'.
    print(arithmetic_arranger(
        ['1 & 2']))

    # Happy path
    print(arithmetic_arranger(
        ['1 + 2', '11 - 2'], True))

    print(repr(arithmetic_arranger(
        ['1 + 2'])))

    print(arithmetic_arranger(
        ['3 + 855', '3801 - 2', '45 + 43', '123 + 49']))
