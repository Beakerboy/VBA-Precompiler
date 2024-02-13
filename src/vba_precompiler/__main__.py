import argparse
import sys
from pathlib import Path
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
    path = Path(args.directory).resolve()
    file_list = find_files(path)
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
    elif args.system == "Win32":
        win32 = True
    elif args.system == "Win64":
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

    env = {"WIN16": win16, "WIN32": win32, "WIN64": win64,
           "MAC": mac, "VBA6": vba6, "VBA7": vba7}
    compiler = Compiler(env)
    Path(args.output).mkdir(parents=True, exist_ok=True)
    for file_name in file_list:
        new_file_rel_path = Path(file_name).relative_to(path)
        output_path = Path(args.output).resolve()
        new_path = output_path.joinpath(new_file_rel_path)
        try:
            result = compiler.compile(file_name)
        except Exception as e:
            print("File Failed: " + file_name, file=sys.stderr)
            print(str(e), file=sys.stderr)
        else:
            new_path.parent.mkdir(parents=True, exist_ok=True)
            with new_path.open(mode='a') as fi:
                fi.write(result)


def find_files(path: Path) -> list:
    """
    Find all gives of given types within a directory
    """
    files = []
    for child in path.rglob("*"):
        if child.suffix in [".bas", ".cls", ".frm"]:
            files.append(child)
    return files


if __name__ == '__main__':
    main()
