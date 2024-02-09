from antlr4 import CommonTokenStream, FileStream
from pathlib import Path
from typing import TypeVar
from vba_precompiler.vba_ccLexer import vba_ccLexer as Lexer
from vba_precompiler.vba_ccParser import vba_ccParser as Parser
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
        raise Exception('file does not exist')
        ts = CommonTokenStream(lexer)
        parser = Parser(ts)
        program = parser.startRule()
        visitor = Visitor()
        visitor.env = self.environment
        visitor.ts = ts
        code = visitor.visit(program)
        return code
        

        
