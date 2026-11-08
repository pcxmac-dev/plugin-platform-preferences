"""`python -m plugin_platform_preferences status | theme [NAME]`: the UI's preferences from the command line (the
platform's page asks the same hooks)."""
from __future__ import annotations

import json
import sys

from liminal_libs import ui

from . import MACHINE

USAGE = f"python -m plugin_platform_preferences status | theme [{'|'.join(ui.THEMES)}]"


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    what, rest = (argv[0], argv[1:]) if argv else ("status", [])
    if what == "status" and not rest:
        print(json.dumps(MACHINE.status(), indent=1))
        return 0
    if what == "theme" and len(rest) <= 1:
        if not rest:
            print(MACHINE.status()["theme"])
            return 0
        try:
            print(f"theme: {MACHINE.theme(rest[0])['theme']}")
            return 0
        except ValueError as e:
            print(str(e), file=sys.stderr)
            return 2
    print(USAGE, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
