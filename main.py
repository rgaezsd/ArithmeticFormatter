# This entrypoint file to be used in development. Start by reading README.md
from arithmetic_arranger import arithmetic_arranger

print('Write 5 problems:')

problems = []
for i in range(5):
    problems.append(input('-:'))

print(arithmetic_arranger(problems))