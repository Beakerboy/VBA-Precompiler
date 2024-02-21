from vba_precompiler.precompiler_visitor import PrecompilerVisitor as Visitor
def test_split_nl() -> None:
    tok_text = "\r\n\n\r"
    result = Visitor.split_nl(tok_text)
    assert result == ["\r\n", "\n", "\r"]
