from antlr4 import CommonTokenStream, FileStream
from pathlib import Path
from typing import TypeVar
from antlr4_vba.vba_ccLexer import vba_ccLexer as Lexer
from antlr4_vba.vba_ccParser import vba_ccParser as Parser
from vba_precompiler.precompiler_visitor import PrecompilerVisitor as Visitor


T = TypeVar('T', bound='Compiler')


class Compiler:
    # class default constructor
    def __init__(self: T, env: dict) -> None:
        if len(env) > 7:
            raise Exception("ENV: " + str(env))
        self.environment = env

    def compile(self: T, path: str) -> str:
        if Path(path).exists():
            input_stream = FileStream(path)
            lexer = Lexer(input_stream)
        else:
            raise Exception('file does not exist: ' + path)
        ts = CommonTokenStream(lexer)
        parser = Parser(ts)
        program = parser.startRule()
        visitor = Visitor()
        visitor.env = self.environment.copy()
        lines = visitor.visit(program)
        i = 1
        f = open(path, 'r')
        code = ""
        while True:
            line = f.readline()
            if not line:
                break
            if i in lines:
                code += "'"
            code += line
            i += 1
        return code
