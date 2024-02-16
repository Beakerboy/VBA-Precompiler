from vba_precompiler.compiler_visitor import PrecompilerVisitor


def test_regex() -> None:
    like = "*ood"
    result = PrecompilerVisitor.like_to_regex(like)
    expected = ".*ood"
    assert result == expected
