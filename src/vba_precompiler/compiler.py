from antlr4 import CommonTokenStream, FileStream, ParseTreeWalker
from antlr4_vba_cc.vbaccLexer import vbaccLexer as Lexer
from pathlib import Path
from typing import TypeVar
from vba_precompiler.vba_ccLexer import vba_ccLexer as Lexer
from vba_precompiler.vba_ccParser import vba_ccParser as Parser


T = TypeVar('T', bound='Compiler')


class Compiler:
    # class default constructor
    def __init__(self: T, environment: list) -> None:
        self.environment = environment

    def compile(self: T, path: str) -> None:
        if Path(path).exists():
            input_stream = FileStream(path)
            lexer = Lexer(input_stream)
        raise Exception('file does not exist')
        ts = CommonTokenStream(lexer)
        parser = Parser(ts)
        program = parser.startRule()
        listener = VbaListener()
        ParseTreeWalker.DEFAULT.walk(listener, program)
        
