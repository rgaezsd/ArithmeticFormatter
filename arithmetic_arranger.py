import re
from errors import *

def arithmetic_arranger(problems):
  if len(problems) > 5:
    return f'Error: {TOO_MANY_PROBLEMS_ERROR}.'

  operations = []

  for problem in problems:
    parts = problem.split()
    operations.append(list(parts))

  first_line = ''
  second_line = ''
  third_line = ''
  quarter_line = ''

  for op in operations:
    if op[1] != '+' and op[1] != '-':
      return f'Error {INVALID_OPERATORS_ERROR}.'

    if re.search('[a-zA-Z]', op[0]) != None or re.search('[a-zA-Z]', op[2]) != None:
      return f'Error {INVALID_NUMBERS_ERROR}.'

    if len(op[0]) > 4 or len(op[2]) > 4:
      return f'Error {OPERATOR_MAX_LIMIT_EXCEEDED_ERROR}.'

    sum_res = str(int(op[0]) + int(op[2]))
    sum_width = len(max(op, key=len)) + 2
    extra_space = sum_width - len(op[2]) - 1

    first_line += f'{op[0]:>{sum_width}}{"":<4}'
    second_line += f'{op[1]}{"".ljust(extra_space, " ")}{op[2]:<{len(op[2]) + 4}}'
    third_line += f'{"".ljust(sum_width, "-")}{"":>4}'
    quarter_line += f'{sum_res:>{sum_width}}{"":<4}'

  print(f'{first_line}\n{second_line}\n{third_line}\n{quarter_line}')