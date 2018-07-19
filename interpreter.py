def init_state():
    return {
            'codes': [],
            'pos': 0,
            'stack': [],
            'end': False,
            }

def interpret(state, codes):
    state['codes'] = codes
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
        }
