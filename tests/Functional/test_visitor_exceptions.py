import pytest
from pytest_mock import MockerFixture
from vba_precompiler.__main__ import main


def test_null_literal(mocker: MockerFixture) -> None:
    """
    Test that an exception is thrown when an unknown system
    type is specified.
    """
    input_file = "tests/files/project14/"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_file
        ],
    )
    with pytest.raises(Exception):
        main()


def test_like_operator(mocker: MockerFixture) -> None:
    """
    Test that an exception is thrown when an unknown version
    is specified.
    """
    input_file = "tests/files/project15/"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_file
        ],
    )
    with pytest.raises(Exception):
        main()
