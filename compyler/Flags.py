from enum import Enum

class Flags(Enum):
    FILE = ("--file", "PATH", {"help": "The file to compile"})
    DIRECTORY = ("--dir", "PATH", {"help": "The directory to compile"})

    OUTPUT = ("--output", "PATH", {"help": "Output directory"})