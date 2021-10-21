def calculate_expression(expression):
    """
    str -> int
    calculates expressions.
    if expression is not valid returns 'Неправильний вираз!'

    >>> calculate_expression("Скільки буде 8 відняти 3?")
    5
    >>> calculate_expression("Скільки буде 7 додати 3 помножити на 5?")
    50
    >>> calculate_expression("Скільки буде 10 поділити на -2 додати 11 мінус -3?")
    9
    >>> calculate_expression("Скільки буде 3 в кубі?")
    'Неправильний вираз!'
    """
    expression = expression.replace("Скільки буде ", "")
    expression = expression.replace("?", "")
    expression = expression.replace(" поділити на ", "/")
    expression = expression.replace(" помножити на ", "*")
    expression = expression.replace(" додати ", "+")
    expression = expression.replace(" плюс ", "+")
    expression = expression.replace(" відняти ", "-")
    expression = expression.replace(" мінус ", "-")
    for i in expression:
        if i not in "1234567890+-*/":
            return 'Неправильний вираз!'
    ind = [""]
    for i, v in enumerate(expression):
        if v in "+-*/":
            if i > 0 and expression[i-1] == ' ':
                continue
            ind.append(v)
            expression = expression[:i] + " " + expression[i+1:]
    nexpression = expression.split()
    res = int(nexpression[0])
    for i, v in enumerate(nexpression):
        if i == 0:
            continue
        else:
            if ind[i] == "+":
                res += int(nexpression[i])
            if ind[i] == "*":
                res *= int(nexpression[i])
            if ind[i] == "-":
                res -= int(nexpression[i])
            if ind[i] == "/":
                try:
                    res /= int(nexpression[i])
                except ZeroDivisionError:
                    return 'Неправильний вираз!'
    return int(res)
