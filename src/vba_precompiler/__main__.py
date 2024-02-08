import argparse
from vba_precompiler.compiler import Compiler


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--system", default="Win16",
                        help="Mac, Win16, Win32, or Win64")
    parser.add_argument("-v", "--version", default=6,
                        help="VBA version, 6 or 7")
    parser.add_argument("-o", "--output", default="./build",
                        help="Output directory")
    parser.add_argument("directory", default='.',
                        help="The source directory.")
    args = parser.parse_args()
    win16 = False
    win32 = False
    win64 = False
    mac = False
    vba6 = False
    vba7 = False
    if args.system == "Mac":
        mac = True
    elif args.system == "Win16":
        win16 = True
    elif args.system == "Win22":
        win32 = True
    elif args.system == "Win16":
        win32 = True
        win64 = True
    else:
        raise Exception("version unsupported")
    if args.version == 6:
        if win32 or mac:
            vba6 = True
    elif args.version == 7:
        vba7 = True
    else:
        raise Exception("Version unsupported")

    env = [win16, win32, win64, mac, vba6, vba7]
    compiler = Compiler(env)
    # foreach file
    result = compiler.compile(args.directory)
    # write file


if __name__ == '__main__':
    main()
