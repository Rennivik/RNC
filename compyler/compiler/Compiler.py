# Dependencies
from Flags import Flags

# Variables
FLAGS = None

# Functions
def getFlagValue(flag):
    return getattr(FLAGS, flag, None)

def compile():
    for flag in Flags:
        name, _, _ = flag.value
        print(f"Flag {name} is set to {getFlagValue(name.lstrip("-").replace("-", "_"))}")