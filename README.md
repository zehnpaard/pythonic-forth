# Simple Forth Interpreter written in Python

Based on http://moi2.sakura.ne.jp/fswiki/wiki.cgi?page=Forth%A4%F2%BA%EE%A4%C3%A4%C6%A4%DF%A4%EB

Usage:

- `python main.py` to activate REPL
- `python main.py samples/sample1.forth` to run single source file

Currently implements:

* Pushing integers to stack
* Adding two integers on the stack
* Printing integers from stack
* Carriage return
* Interactive REPL
* IF-ELSE-THEN
* DO-LOOP
* Variable definition, get/set

TODO:

* User-defined Word
* Multi-line REPL input
* Printing strings
* Error handling
* Arithmetic operators
* Stack manipulation operators
