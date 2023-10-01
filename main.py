import re

def calc_sub_expr(sub: tuple[str, str, str]) -> int | float:
    n1, o, n2 = sub
    n1, n2 = int(n1), int(n2)
    match o:
        case '**':
            return n1 ** n2
        case '*':
            return n1 * n2
        case '/':
            return n1 / n2
        case '+':
            return n1 + n2
        case '-':
            return n1 - n2

def calculate(input: str) -> int | float:
    regex = r'((\*{1,2}|[+-\/]|^)-)?\d+|\*{1,2}|[+-\/\(\)]'

    # input = input('Input expression:\t')  # '-22 + 0 / -2 - 100 * 10**-9 * -2'
    expr = input.replace(' ', '')

    matches = [*map(lambda m: m.group(), re.finditer(regex, expr, re.MULTILINE))]

    # joins numbers with their sign, but also joins with their operations
    bugs = [*filter(lambda e: re.search(r'(\*{1,2}|[+-\/\(\)])-\d+', e[1]), enumerate(matches))]

    # split negative numbers with their operations
    for count, (ind, bug) in enumerate(bugs):
        matches.pop(ind + count)
        op, mod = bug.split('-')
        matches.insert(ind + count, op)
        matches.insert(ind + count + 1, f'-{mod}')

    operations_order = ['**', '*', '/', '+', '-']

    # calculate
    for o in operations_order:
        for i, m in reversed(list(enumerate(matches))):
            if m == o:
                sub_expr: tuple[str, str, str] = tuple(matches[i-1:i+2])
                del matches[i-1:i+2]
                matches.insert(i - 1, calc_sub_expr(sub_expr))
    
    return matches[0]
    
input = input('Input expression:\t')
res = calculate(input)
print(f'Expected:\t{eval(input)}', f'Actually:\t{res}', sep='\n')