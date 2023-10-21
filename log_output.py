"""
Condenses a terminal print statement and a file write to the same function call

Author: Nicholas Butzke
"""


def log_output(output: str, file, e="\n"):
    """Condenses a terminal print statement and a file write to the same function call"""
    file.write(output + e)
    print(output, end=e)
