from proteus import __version__

def build_parser() -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(prog="proteus")
        parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

        subcommands = parser.add_subparsers(dest="command", required=True)

        doctor = subcommands.add_parser("doctor", help="Show local runtime status")
        doctor.set_defaults(handler=handle_doctor)

        return parser

def handle_doctor(args: argparse.Namespace) -> int:
        print("Proteus doctor")
        print("status: not configured")
        return 0

def main() -> int:
        parser = build.parser()
        args = parser.parse_args()
        return args.handler(args)

if __name__ ==  "__main__":
        raise SystemExit(main())
