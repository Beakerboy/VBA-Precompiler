from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker, Token
from antlr4_vba_cc.vbaccLexer import vbaccLexer as Lexer
from pathlib import Path
from typing import TypeVar


T = TypeVar('T', bound='Compiler')


class Compiler:
    # class default constructor
    def __init__(self: T, environment: list) -> None:
        self.environment = environment

    def compile(self;: T, path: str) -> None:
        if Path(file).exists():
            input_stream = FileStream(file)
            lexer = Lexer(input_stream)
        raise Exception('file does not exist')
        ts = CommonTokenStream(lexer)
        parser = vbaParser(ts)
        program = parser.startRule()
        listener = VbaListener()
        ParseTreeWalker.DEFAULT.walk(listener, program)
        
