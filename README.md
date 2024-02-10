[![Coverage Status](https://coveralls.io/repos/github/Beakerboy/VBA-Precompiler/badge.png?branch=main)](https://coveralls.io/github/Beakerboy/VBA-Precompiler?branch=main) ![Build Status](https://github.com/Beakerboy/VBA-Precompiler/actions/workflows/python-package.yml/badge.svg)
# VBA-Precompiler

## About
The Microsoft VBA language includes a simple precompilation language (Conditional Compilation). This tool allows users to specify environment parameters to convert a conditional-module-body into a preprocessed-module-body.

This software operates as recommended in the [Microsoft VBA Language Specification](https://winprotocoldoc.blob.core.windows.net/productionwindowsarchives/MS-CFB/%5bMS-CFB%5d.pdf).

## Requirements
vba_precompiler is tested on python 3.8 and higher.

## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install VBA-Precompiler.
```
pip install 'vba_precompiler @ git+https://github.com/Beakerboy/VBA-Precompiler@dev'
```

## Getting Started
vba_precompiler will take a specified directory that contains vba source code, and a set of environment values, and produce a set of matching vba source files in which code is excluded as directed by the precomiler directives.

For example, the following
```
Attribute VB_Name = "Input"
#Const TestType="testing"
#If Win16 Or Then
    foo = 6
#ElseIf Win32
    foo = 7
#EndIf
'Additional VBA code follows
```

Will be transformed to the following:
```
Attribute VB_Name = "Input"
'#Const TestType="testing"
'#If Win16 Then
    foo = 6
'#ElseIf Win32
'    foo = 7
'#EndIf
'Additional VBA code follows
```
To run the program
```
python vba_precompiler.py [-h] [-s SYSTEM] [-v VERSION] [-o OUTPUT] directory

positional arguments:
  directory             The source directory.

options:
  -h, --help            show this help message and
                        exit
  -s, --system          System Type, Win16, Win32, Win64, or Mac.
  -v, --version         VBA version, 6 or 7.
  -o, --output         output path, defaults to ./build.

examples:
  python -m vba_precompiler -s Win32 -v 7 -o ./build32_7 ./project
```

## Tests
The tests directory contains complete unit and functional tests.

## Contributing
Contributions are welcome. Please ensure new features include unit tests to maintain 100% coverage. All code must adhere to the [PEP8 Standards](https://peps.python.org/pep-0008/) for both formatting and naming. Method signatures must be fully annotated.
