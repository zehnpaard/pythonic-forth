import tokenizer
import compiler
import interpreter

if __name__ == '__main__':
    with open('samples/sample1.forth') as f:
        s = ' '.join(f)
    tokens = tokenizer.tokenize(s)
    code_list = compiler.compile(tokens)
    interpreter.interpret(code_list)
