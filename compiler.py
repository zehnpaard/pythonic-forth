def init_state():
    return {
            'tokens': [],
            'pos': 0,
            'codes': [],
            'branch': [],
            'vars': {},
            'end': False
            }

def compile(state, tokens):
    state['tokens'].extend(tokens)
    if state['codes']:
        state['codes'].pop()
    state['end'] = False

    while not state['end']:
        run(state)
    return state['codes'], len(state['vars'])

def run(state):
    if state['pos'] == len(state['tokens']):
        state['codes'].append('END')
        state['end'] = True
        return

    token = state['tokens'][state['pos']]
    if is_int(token):
        state['codes'].extend(('PUSH', int(token)))
    elif token in primitives:
        primitives[token](state)
    elif token in state['vars']:
        state['codes'].extend(('PUSH', state['vars'][token]))
    state['pos'] += 1

def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    return True

def run_if(state):
    state['branch'].append(len(state['codes']) + 1)
    state['codes'].extend(('IF', None))

def run_else(state):
    if_pos = state['branch'].pop()
    state['codes'][if_pos] = len(state['codes']) + 2

    state['branch'].append(len(state['codes']) + 1)
    state['codes'].extend(('ELSE', None))

def run_then(state):
    else_pos = state['branch'].pop()
    state['codes'][else_pos] = len(state['codes'])

def run_do(state):
    state['branch'].append(len(state['codes']) + 1)
    state['codes'].append('DO')

def run_loop(state):
    do_pos = state['branch'].pop()
    state['codes'].extend(('LOOP', do_pos))

def run_variable(state):
    var_name = state['tokens'][state['pos']+1]
    state['vars'][var_name] = len(state['vars'])
    state['pos'] += 1

primitives = {
        '+': lambda state: state['codes'].append('+'),
        '.': lambda state: state['codes'].append('.'),
        'CR': lambda state: state['codes'].append('CR'),
        'IF': run_if,
        'ELSE': run_else,
        'THEN': run_then,
        'DO': run_do,
        'LOOP': run_loop,
        'I': lambda state: state['codes'].append('I'),
        'VARIABLE': run_variable,
        '@': lambda state: state['codes'].append('@'),
        '!': lambda state: state['codes'].append('!'),
        }
