import pytest
from pytest_mock import MockerFixture
from vba_precompiler.__main__ import main


def test_unsupported_system(mocker: MockerFixture) -> None:
    """
    Test that an exception is thrown when an unknown system
    type is specified.
    """
    input_file = "tests/files/project1/Modules"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            "-sFoo",
        ],
    )
    with pytest.raises(Exception):
        main()


def test_unsupported_version(mocker: MockerFixture) -> None:
    """
    Test that an exception is thrown when an unknown version
    is specified.
    """
    input_file = "tests/files/project1/Modules"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            "-v2",
        ],
    )
    with pytest.raises(Exception):
        main()
