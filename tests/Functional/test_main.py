import difflib
import os
import pytest
import shutil
import filecmp
from pytest_mock import MockerFixture
from vba_precompiler.__main__ import main


@pytest.fixture(autouse=True)
def run_around_tests() -> None:
    # Code that will run before your test.

    # A test function will be run at this point
    yield

    # Code that will run after your test.
    shutil.rmtree('./build')


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
    with pytest.raises(SystemExit):
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
    with pytest.raises(SystemExit):
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


def test_win32(mocker: MockerFixture) -> None:
    """
    Test that one file has different output if the environment
    changes.
    """
    input_dir = "tests/files/project4"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_dir,
            "-sWin32",
            "-v7",
        ],
    )
    main()
    expected_output_file = "./build/Modules/test.bas"
    target_output = "./tests/files/build/project4_32.bas"
    assert_files_identical(expected_output_file, target_output)


def test_mac(mocker: MockerFixture) -> None:
    """
    Test that one file has different output if the environment
    changes.
    """
    input_dir = "tests/files/project4"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_dir,
            "-sMac",
            "-v6",
        ],
    )
    main()
    expected_output_file = "./build/Modules/test.bas"
    target_output = "./tests/files/build/project4_mac.bas"
    assert_files_identical(expected_output_file, target_output)


def test_missing_identifier(mocker: MockerFixture) -> None:
    """
    Test that an unknown identifier evaluates as False
    """
    input_path = "tests/files/project5"
    file_name = "missing_identifier.bas"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_path,
        ],
    )
    main()
    expected_output_file = "./build/" + file_name
    target_output = "./tests/files/build/" + file_name
    assert_files_identical(expected_output_file, target_output)


def test_elseif(mocker: MockerFixture) -> None:
    """
    Test that a simple if-elseif block works in both directions.
    """
    input_dir = "tests/files/project6"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_dir,
        ],
    )
    main()
    expected_output_file = "./build/elseif.bas"
    target_output = "./tests/files/build/elseif.bas"
    assert_files_identical(expected_output_file, target_output)


def test_ifelse(mocker: MockerFixture) -> None:
    """
    Test that a simple if-elseif block works in both directions.
    """
    input_dir = "tests/files/project7"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_dir,
        ],
    )
    main()
    expected_output_file = "./build/ifelse.bas"
    target_output = "./tests/files/build/ifelse.bas"
    assert_files_identical(expected_output_file, target_output)


def test_literals(mocker: MockerFixture) -> None:
    """
    Test that an unknown identifier evaluates as False
    """
    input_path = "tests/files/project0"
    file_name = "literal.bas"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_path,
        ],
    )
    main()
    expected_output_file = "./build/" + file_name
    target_output = "./tests/files/build/" + file_name
    assert_files_identical(expected_output_file, target_output)


def test_int_literals(mocker: MockerFixture) -> None:
    """
    Test that an unknown identifier evaluates as False
    """
    input_path = "tests/files/project8"
    file_name = "intliteral.bas"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_path,
        ],
    )
    main()
    expected_output_file = "./build/" + file_name
    target_output = "./tests/files/build/" + file_name
    assert_files_identical(expected_output_file, target_output)


def test_arithmetic_operators(mocker: MockerFixture) -> None:
    """
    Test that an the arithmetic operators work as expected.
    """
    input_path = "tests/files/project9"
    file_name = "arithmetic.bas"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_path,
        ],
    )
    main()
    expected_output_file = "./build/" + file_name
    target_output = "./tests/files/build/" + file_name
    assert_files_identical(expected_output_file, target_output)


def test_relational_operators(mocker: MockerFixture) -> None:
    """
    Test that an the arithmetic operators work as expected.
    """
    input_path = "tests/files/project10"
    file_name = "relational.bas"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_path,
        ],
    )
    main()
    expected_output_file = "./build/" + file_name
    target_output = "./tests/files/build/" + file_name
    assert_files_identical(expected_output_file, target_output)


def test_boolean_operators(mocker: MockerFixture) -> None:
    """
    Test that an the arithmetic operators work as expected.
    """
    input_path = "tests/files/project11"
    file_name = "boolean.bas"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_path,
        ],
    )
    main()
    expected_output_file = "./build/" + file_name
    target_output = "./tests/files/build/" + file_name
    assert_files_identical(expected_output_file, target_output)


def test_parenthesis(mocker: MockerFixture) -> None:
    """
    Test that an the arithmetic operators work as expected.
    """
    input_path = "tests/files/project12"
    file_name = "parenthesis.bas"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_path,
        ],
    )
    main()
    expected_output_file = "./build/" + file_name
    target_output = "./tests/files/build/" + file_name
    assert_files_identical(expected_output_file, target_output)


def test_nesting(mocker: MockerFixture) -> None:
    """
    Test that nesting if blocks works.
    """
    input_path = "tests/files/project13"
    file_name = "nested.bas"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_path,
            "-sWin64",
            "-v7",
        ],
    )
    main()
    expected_output_file = "./build/" + file_name
    target_output = "./tests/files/build/" + file_name
    assert_files_identical(expected_output_file, target_output)


def test_date_literal(mocker: MockerFixture) -> None:
    """
    Test that an the arithmetic operators work as expected.
    """
    input_path = "tests/files/project16"
    file_name = "date.bas"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            input_path,
        ],
    )
    main()
    expected_output_file = "./build/" + file_name
    target_output = "./tests/files/build/" + file_name
    assert_files_identical(expected_output_file, target_output)


def test_define(mocker: MockerFixture) -> None:
    """
    Test that an the arithmetic operators work as expected.
    """
    input_path = "tests/files/project17"
    file_name = "define.bas"
    mocker.patch(
        "sys.argv",
        [
            "vba_precompiler.py",
            '-DIntTest=42,FloatTest=3.1415926535,BoolTest=True,StringTest="Yes"'
            input_path,
        ],
    )
    main()
    expected_output_file = "./build/" + file_name
    target_output = "./tests/files/build/" + file_name
    assert_files_identical(expected_output_file, target_output)


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
