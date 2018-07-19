def compile(tokens):
    code_list = []
    for token in tokens:
        code_list.extend(compile_token(token))
    code_list.append('END')
    return code_list

def compile_token(token):
    if is_int(token):
        return ('PUSH', int(token))
    d = {'+':'PLUS', '.':'PRINT'}
    return (d[token], )

def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    return True
