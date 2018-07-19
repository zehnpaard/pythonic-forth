def init_state():
    return {
            'codes': [],
            'pos': 0,
            'stack': [],
            'branch': [],
            'vars': [],
            'end': False,
            }

def interpret(state, codes, var_count):
    state['codes'] = codes
    state['vars'].extend([0] * (var_count - len(state['vars'])))
    state['end'] = False

    while not state['end']:
        run(state)

def run(state):
    code = state['codes'][state['pos']]
    commands[code](state)

def run_push(state):
    v = state['codes'][state['pos']+1]
    state['stack'].append(v)
    state['pos'] += 2

def run_plus(state):
    a, b = state['stack'].pop(), state['stack'].pop()
    state['stack'].append(a + b)
    state['pos'] += 1

def run_print(state):
    a = state['stack'].pop()
    print(a, end='')
    state['pos'] += 1
    
def run_cr(state):
    print()
    state['pos'] += 1

def run_if(state):
    a = state['stack'].pop()
    if a == 0:
        state['pos'] = state['codes'][state['pos']+1]
    else:
        state['pos'] += 2

def run_else(state):
    state['pos'] = state['codes'][state['pos']+1]

def run_do(state):
    a, b = state['stack'].pop(), state['stack'].pop()
    state['branch'].extend((b, a))
    state['pos'] += 1

def run_loop(state):
    a, b = state['branch'].pop(), state['branch'].pop()
    a += 1
    if a < b:
        state['branch'].extend((b, a))
        state['pos'] = state['codes'][state['pos']+1]
    else:
        state['pos'] += 2

def run_i(state):
    state['stack'].append(state['branch'][-1])
    state['pos'] += 1

def run_get(state):
    a = state['stack'].pop()
    state['stack'].append(state['vars'][a])
    state['pos'] += 1

def run_set(state):
    a, b = state['stack'].pop(), state['stack'].pop()
    state['vars'][a] = b
    state['pos'] += 1

def run_end(state):
    state['end'] = True

commands = {
        'PUSH': run_push,
        '+': run_plus,
        '.': run_print,
        'CR': run_cr,
        'IF': run_if,
        'ELSE': run_else,
        'END': run_end,
        'DO': run_do,
        'LOOP': run_loop,
        'I': run_i,
        '@': run_get,
        '!': run_set,
        }
