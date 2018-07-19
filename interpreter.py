def init_state():
    return {
            'codes': [],
            'pos': 0,
            'stack': [],
            'end': False,
            }

def interpret(state, codes):
    state['codes'] = codes
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

def run_end(state):
    state['end'] = True

commands = {
        'PUSH': run_push,
        '+': run_plus,
        '.': run_print,
        'CR': run_cr,
        'END': run_end,
        }
