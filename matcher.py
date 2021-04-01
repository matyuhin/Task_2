def check_brackets(text, opening):
    try:
        flag = True
        err = None
        not_closed = None
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}',
            '<': '>'
        }
        closing = []
        stack = []
        cl = False
        for bracket in opening:
            closing.append(brackets[bracket])
        for i in range(len(text)):
            if text[i] in opening: # Если текущий символ является открывающей скобкой
                stack.append((text[i], i))
            elif text[i] in closing and len(stack): # Если текущий символ является закрывающей скобкой и уже была открывающая скобка
                if brackets[stack[-1][0]] == text[i]:
                    stack.pop()
                else:
                    flag = False
                    err = (text[i], i)
                    cl = True
                    break
            elif text[i] in closing and not len(stack): # Если текущий символ является закрывающей скобкой и открывающей скобки еще не было
                flag = False
                err = (text[i], i)
        if len(stack):
            flag = False
            not_closed = stack[-1]
            if not cl:
                err = not_closed
        return print(f"{flag}, {err}, {not_closed}")
    except KeyError:
        print("Введены неверные символы")


text = list(input("Введите строку: "))
brackets = list(input("Введите проверяемые скобки: "))
check_brackets(text, brackets)
