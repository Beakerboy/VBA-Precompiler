import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--os", default="Win16",
                        help="Mac, Win16, Win32, or Win64")
    parser.add_argument("-v", "--version", default=6,
                        help="VBA version, 6 or 7")
    args = parser.parse_args()
    Win16 = False
    Win32 = False
    Win64 = False
    Mac = False
    Vba6 = False
    Vba7 = False
    if args.os == "Mac":
        Mac = True
    else if args.os == "Win16":
        Win16 = True
    elif args.os == "Win22":
        Win32 = True
    elif args.os == "Win16":
        Win32 = True
        Win64 = True
    else:
        raise Exception("version unsupported")
    if args.version == 6:
        if Win32 or Mac:
            Vba6 = True
    elif args.version == 7:
        Vba7 = True
    else:
        raise Exception("Version unsupported")
    
if __name__ == '__main__':
    main()
