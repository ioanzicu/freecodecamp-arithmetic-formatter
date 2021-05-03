def arithmetic_arranger(args, display_answer=False):
    '''
    Expected input: ['1 + 1', '4 - 2']
        - A single space between the operator
        - Only two operands
        - Accepted operands: +, -


    Example of call:
    arithmetic_arranger(['1 + 1', '4 - 2'])

    Result format:
        1
      + 1
      ---
        2
    '''

    args_len = len(args)
    if args_len > 5:
        return 'Error: Too many problems.'

    accepted_operators = ('+', '-')
    operand1_list = []
    operand2_list = []
    dashes_list = []
    result_list = []

    for problem in args:
        if not isinstance(problem, str):
            return "Error: Problem should be a string instance."

        problem_list = problem.split(' ')
        if len(problem_list) != 3:
            return f'Error: Incorrect problem format, expected operator1 +/- operator2 separated by one space (3 elements), obtained: {problem}.'

        operand1, operator, operand2 = problem_list
        if operator not in accepted_operators:
            return 'Error: Operator must be \'+\' or \'-\'.'

        # @TODO Negate
        if (operand1 := try_parse_number(operand1)) and (operand2 := try_parse_number(operand2)):
            # @TODO Extract in a separate function

            operand1_str = str(operand1)
            operand2_str = str(operand2)

            operand1_len = len(operand1_str)
            operand2_len = len(operand2_str)

            if operand1_len > 4 or operand2_len > 4:
                return 'Error: Numbers cannot be more than four digits.'

            # Happy Path
            total_space_count = max([operand1_len, operand2_len]) + 2

            operand1_space = str(operand1).rjust(total_space_count, ' ')
            operand2_space = f'{operator} ' + \
                str(operand2).rjust(total_space_count - 2, ' ')

            operand1_list.append(operand1_space)
            operand2_list.append(operand2_space)

            dashes_list.append('-' * total_space_count)

            result = 0
            if operator == '+':
                result = operand1 + operand2

            if operator == '-':
                result = operand1 - operand2

            result_str = str(result)
            result_space_count = total_space_count - len(result_str)

            result_space = ' ' * result_space_count
            result_space += result_str

            result_list.append(result_space)

        else:
            return 'Error: Numbers must only contain digits.'

    final_result = ''
    final_result += format_result_str(operand1_list)
    final_result += '\n'
    final_result += format_result_str(operand2_list)
    final_result += '\n'
    final_result += format_result_str(dashes_list)
    if display_answer:
        final_result += '\n'
        final_result += format_result_str(result_list)

    return final_result


def try_parse_number(str_number):
    try:
        number = int(str_number)
        return number
    except:
        return None


def format_result_str(item_list):
    first = True
    result_str = ''
    for item in item_list:
        if first:
            result_str += item
            first = False
        else:
            result_str += f'    {item}'
    return result_str


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
