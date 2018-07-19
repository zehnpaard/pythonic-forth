def init_state():
    return {
            'tokens': [],
            'pos': 0,
            'codes': [],
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

primitives = {
        '+': run_plus,
        '.': run_print,
        'CR': run_cr,
        }
