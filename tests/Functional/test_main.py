import difflib
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
    input_dir = "tests/files/project4"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_dir,
        ],
    )
    main()
    expected_output_file = "./build/Modules/test.bas"
    target_output = "./tests/files/build/project4.bas"
    assert_files_identical(expected_output_file, target_output)


def test_missing_if_identifier(mocker: MockerFixture) -> None:
    """
    Test that an exception is thrown when an expression contains
    an unknown identifier.
    """
    input_file = "tests/files/project5
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_file,
        ],
    )
    with pytest.raises(Exception):
        main()


def assert_files_identical(new_file: str, target_output: str) -> bool:
    # if they are the same, just make the assertion
    # if not, raise an exception with details.
    assert os.path.exists(new_file)
    if filecmp.cmp(new_file, target_output):
        assert True
    else:
        result = ""
        with open(target_output, 'r') as file0:
            with open(new_file, 'r') as file1:
                diff = difflib.unified_diff(
                    file0.readlines(),
                    file1.readlines(),
                    fromfile=target_output,
                    tofile=new_file,
                )
                for line in diff:
                    result += line
        raise Exception(result)
