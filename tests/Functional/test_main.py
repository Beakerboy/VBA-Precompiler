def test_main_file() -> None:
    """
    Test that precompiling one file works
    use default settings
    """
    input_file = "tests/files/project1/Modules/input.bas"
    expected_file = "tests/files/build/input.bas"
    argv = [
    ]
    main()
    # assert fileExists(output location and name)
    assert expected_file == "tests/files/"

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
