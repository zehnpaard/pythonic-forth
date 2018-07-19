def init_state():
    return {
            'tokens': [],
            'pos': 0,
            'codes': [],
            'branch': [],
            'end': False
            }

def compile(state, tokens):
    state['tokens'].extend(tokens)
    if state['codes']:
        state['codes'].pop()
    state['end'] = False

    while not state['end']:
        run(state)
    return state['codes']

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
    state['pos'] += 1

def is_int(s):
    try:
        int(s)
    except ValueError:
        return False
    return True

def run_plus(state):
    state['codes'].append('+')

def run_print(state):
    state['codes'].append('.')

def run_cr(state):
    state['codes'].append('CR')

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

primitives = {
        '+': run_plus,
        '.': run_print,
        'CR': run_cr,
        'IF': run_if,
        'ELSE': run_else,
        }
