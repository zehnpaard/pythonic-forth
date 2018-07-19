import tokenizer
import compiler
import interpreter

if __name__ == '__main__':
    with open('samples/sample1.forth') as f:
        s = ' '.join(f)
    tokens = tokenizer.tokenize(s)

    compiler_state = compiler.init_state()
    codes = compiler.compile(compiler_state, tokens)

    interpreter_state = interpreter.init_state()
    interpreter.interpret(interpreter_state, codes)
