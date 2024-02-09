import pytest
from pytest_mock import MockerFixture
from vba_precompiler.__main__ import main


def test_main_file(mocker: MockerFixture) -> None:
    """
    Test that an exception is thrown on a bad file.
    """
    input_file = "tests/files/project1/Modules/bad.bas"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_file,
        ],
    )
    with pytest.raises(Exception):
        main()

def test_main_directory() -> None:
    """
    Test that precompiling a directory processes all files.
    """
    pass

def test_alternate_environment() -> None:
    """
    Test different enviroment settings.
    """
    pass
