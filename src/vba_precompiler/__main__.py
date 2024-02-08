import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--os", default="Win16",
                        help="Mac, Win16, Win32, or Win64")
    parser.add_argument("-v", "--version", default=6,
                        help="VBA version, 6 or 7")
    args = parser.parse_args()
    win16 = False
    win32 = False
    win64 = False
    mac = False
    vba6 = False
    vba7 = False
    if args.os == "Mac":
        mac = True
    elif args.os == "Win16":
        win16 = True
    elif args.os == "Win22":
        win32 = True
    elif args.os == "Win16":
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
    
if __name__ == '__main__':
    main()
