def test_main_file() -> None:
    """
    Test that precompiling one file works
    use default settings
    """
    input_file = "project1/Modules/input.bas"
    expected_file = "files/project1output.bas"
    argv = [
    ]
    main()
    # assert fileExists(output location and name)
    assert expected and produced files match

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
