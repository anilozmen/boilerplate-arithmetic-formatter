# https://replit.com/@anilozmen/boilerplate-arithmetic-formatter

MAX_PROBLEM_LIMIT = 5
VALID_OPERATORS = ['+', '-']
MAX_DIGIT = 4


def arithmetic_arranger(problems, display_answer=False):
    results = list()

    if len(problems) > MAX_PROBLEM_LIMIT:
        return "Error: Too many problems."

    for problem in problems:
        splitted_problem = problem.split()
        first_operand = splitted_problem[0]
        operator = splitted_problem[1]
        second_operand = splitted_problem[2]

        if len(splitted_problem) != 3:
            return "Error: Invalid Format."

        if operator not in VALID_OPERATORS:
            return "Error: Operator must be '+' or '-'."

        if first_operand.isdigit() == False or second_operand.isdigit() == False:
            return "Error: Numbers must only contain digits."

        if len(first_operand) > MAX_DIGIT or len(second_operand) > MAX_DIGIT:
            return "Error: Numbers cannot be more than four digits."

        if operator == '+':
            result = [
                first_operand,
                operator,
                second_operand,
                line_creator(first_operand, second_operand),
                int(first_operand) + int(second_operand)
            ]
        else:
            result = [
                first_operand,
                operator,
                second_operand,
                line_creator(first_operand, second_operand),
                int(first_operand) - int(second_operand)
            ]

        results.append(result)

    return output_creator(results, display_answer)


def line_creator(first, second):
    count = len(first)
    if len(second) > count:
        count = len(second)
    return "-" * count + "--"


def output_creator(results, show_result=False):
    first_line = []
    second_line = []
    lines = []
    result_line = []

    for result in results:
        base_length = len(result[0])
        if (len(result[1]) > base_length):
            base_length = len(result[1])
        base_length += 1

        first_line.append(result[0].rjust(len(result[3])))

        second = result[1] + "" + result[2].rjust(len(result[3]) - 1)
        second_line.append(second)
        lines.append(result[3])

        if (show_result):
            result_line.append(str(result[4]).rjust(len(result[3])))

    result_str = '    '.join(first_line) + '\n'
    result_str += '    '.join(second_line) + '\n'
    result_str += '    '.join(lines)
    if (show_result):
        result_str += '\n' + '    '.join(result_line)

    return result_str
