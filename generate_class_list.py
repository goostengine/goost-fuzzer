#!/usr/bin/env python

import os
import sys

if not os.path.exists("goost"):
    print("ERROR: Goost repository is not checked out.")
    sys.exit(255)

if not os.path.exists("fuzzer"):
    print("ERROR: Fuzzer repository is not checked out.")
    sys.exit(255)

sys.path.insert(0, "goost")

from goost import classes

with open("fuzzer/classes.txt", "w") as f:
    for name in classes:
        if name == "ImageBlender":
            # TODO: infinite loop: https://github.com/goostengine/goost/issues/120
            continue
        f.write(name + "\n")

sys.path.remove("goost")
sys.modules.pop("goost")
