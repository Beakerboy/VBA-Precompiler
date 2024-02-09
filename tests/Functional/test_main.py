import os
import pytest
from pytest_mock import MockerFixture
from vba_precompiler.__main__ import main


def test_reused_identifier(mocker: MockerFixture) -> None:
    """
    Test that an exception is thrown when attempting to
    redeclare a constanst.
    """
    input_file = "tests/files/project1/Modules"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_file,
        ],
    )
    with pytest.raises(Exception):
        main()


def test_const(mocker: MockerFixture) -> None:
    """
    Test that a constant line is commented out of the compiled file.
    """
    input_file = "tests/files/project2"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_file,
        ],
    )
    main()
    assert os.path.exists("tests/files/build/project2/Modules/input.bas")


def test_alternate_environment() -> None:
    """
    Test different enviroment settings.
    """
    pass
