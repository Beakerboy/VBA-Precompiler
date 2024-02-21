import pytest
from vba_precompiler.compiler import Compiler


def test_file_not_exist_exception() -> None:
    compiler = Compiler([])
    with pytest.raises(Exception):
        compiler.compile("foo.bas")
