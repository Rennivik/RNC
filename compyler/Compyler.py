# Dependencies
import sys
import os
import argparse
import compiler.Compiler as Compiler

from Flags import Flags

# Variables
parser = argparse.ArgumentParser(description="RNC Compiler")

for flag in Flags:
    name, metavar, kwargs = flag.value

    parser.add_argument(
        name,
        **({"metavar": metavar} if metavar else {}),
        **kwargs
    )

Compiler.FLAGS = parser.parse_args()
Compiler.compile()