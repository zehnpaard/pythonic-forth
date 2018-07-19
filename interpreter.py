def interpret(code_list):
    counter = 0
    stack = []
    while True:
        if code_list[counter] == 'END':
            break
        elif code_list[counter] == 'PUSH':
            stack.append(code_list[counter+1])
            counter += 2
        elif code_list[counter] == '+':
            a, b = stack.pop(), stack.pop()
            stack.append(a+b)
            counter += 1
        elif code_list[counter] == '.':
            print(stack.pop(), end='')
            counter += 1
        elif code_list[counter] == 'CR':
            print()
            counter += 1
