import os
import pytest
import filecmp
from pytest_mock import MockerFixture
from vba_precompiler.__main__ import main


def test_reused_ext_identifier(mocker: MockerFixture) -> None:
    """
    Test that an exception is thrown when attempting to
    redeclare a constanst that was provided from outside.
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


def test_reused_int_identifier(mocker: MockerFixture) -> None:
    """
    Test that an exception is thrown when attempting to
    redeclare a constanst that was declared within the file.
    """
    input_file = "tests/files/project3/Modules"
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
    expected_output_path = "./build/Modules/input.bas"
    target_output = "./tests/files/build/input.bas"
    assert os.path.exists(expected_output_path)
    assert filecmp.cmp(expected_output_path, target_output)
    os.remove(expected_output_path)


def test_boolean_literal_if(mocker: MockerFixture) -> None:
    """
    Test that if and endif lines are commented out.
    """
    input_dir = "tests/files/project3"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_dir,
        ],
    )
    main()
    expected_output_path = "./build/Modules/input.bas"
    target_output = "./tests/files/build/project3.bas"
    assert os.path.exists(expected_output_path)
    assert filecmp.cmp(expected_output_path, target_output)
