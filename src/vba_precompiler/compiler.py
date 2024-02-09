from antlr4 import CommonTokenStream, FileStream
from pathlib import Path
from typing import TypeVar
from vba_precompiler.grammar.vba_ccLexer import vba_ccLexer as Lexer
from vba_precompiler.grammar.vba_ccParser import vba_ccParser as Parser
from vba_precompiler.compiler_visitor import PrecompilerVisitor as Visitor


T = TypeVar('T', bound='Compiler')


class Compiler:
    # class default constructor
    def __init__(self: T, environment: dict) -> None:
        self.environment = environment

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
        visitor.env = self.environment
        lines = visitor.visit(program)
        i = 1
        f = open(path, 'r')
        code = ""
        line_end = visitor.le
        while true:
            line = f.readline()
            if not line:
                break
            if line in lines:
                code += "'"
            code += line + line_end
            i += 1
        return code
