import re

def calc_sub_expr(sub: tuple[str, ...]) -> float | None:
    n1, o, n2 = sub
    n1, n2 = float(n1), float(n2)
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
        case _:
            raise Exception('Not implemented')

def calculate(input: str) -> float:
    def process_operations(matches: list[str | float]) -> int | float:
        operations_order = ['**', '*', '/', '+', '-']

        # handle parentheses
        parentheses_counter: dict[str, list[int]] = {'left': [], 'right': []}
        parentheses_pairs: list[tuple[int, int]] = []
        for i, m in enumerate(matches):
            if m == '(':
                parentheses_counter['left'].append(i)
            elif m == ')':
                parentheses_counter['right'].append(i)
            if all(parentheses_counter.values()) and \
                    len(parentheses_counter['left']) == len(parentheses_counter['right']):
                parentheses_pairs.append((parentheses_counter['left'][0], parentheses_counter['right'][-1]))
                parentheses_counter = {'left': [], 'right': []}

        # process parentheses
        for start, end in reversed(parentheses_pairs):
            tmp = process_operations(matches[start+1:end])
            del matches[start:end+1]
            matches.insert(start, tmp)

        # calculate
        for o in operations_order:
            for i, m in reversed(list(enumerate(matches))):
                if m == o:
                    sub_expr: tuple[str, str, str] = tuple(matches[i-1:i+2]) # type: ignore
                    del matches[i-1:i+2]
                    matches.insert(i - 1, calc_sub_expr(sub_expr)) # type: ignore
        
        return matches[0] # type: ignore
    
    regex = r'((\*{1,2}|[+-\/]|^)-)?\d+|\*{1,2}|[+-\/\(\)]'

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
    
    return process_operations(matches) # type: ignore
    

# inputs = ['(6 / (5 - 2)) * (10 - 7)',
#           '((2 + 2) * 2)',
#           '((3 - 1) * (9 - 7)) / 4',
#           '(1 + 2 + 3 + 4 - 1) * (8 / (7 - (2 ** (5 - 1) - 7) / 3))']

# for inp in inputs:
#     assert calculate(inp) == eval(inp)
