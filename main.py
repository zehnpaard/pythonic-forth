import sys

import tokenizer
import compiler
import interpreter

def run_file(filename):
    with open(filename) as f:
        s = ' '.join(f)
    tokens = tokenizer.tokenize(s)

    compiler_state = compiler.init_state()
    codes, var_count, last_ret = compiler.compile(compiler_state, tokens)

    interpreter_state = interpreter.init_state()
    interpreter.interpret(interpreter_state, codes, var_count, last_ret)

def run_repl():
    compiler_state = compiler.init_state()
    interpreter_state = interpreter.init_state()

    print("Starting Forth REPL...")

    while True:
        s = input('> ')
        if s == 'QUIT': break

        tokens = tokenizer.tokenize(s)
        codes, var_count, last_ret = compiler.compile(compiler_state, tokens)
        interpreter.interpret(interpreter_state, codes, var_count, last_ret)

if __name__ == '__main__':
    if len(sys.argv) == 2:
        run_file(sys.argv[1])
    else:
        run_repl()
