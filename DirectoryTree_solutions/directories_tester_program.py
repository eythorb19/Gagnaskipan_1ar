import sys

import directories_program_class as directories

def run_directories_test():
    orig_stdin = sys.stdin
    fin = open(sys.path[0] + "/commands.txt")
    sys.stdin = fin
    directories.run_directories_program()
    sys.stdin = orig_stdin

if __name__ == "__main__":
    run_directories_test()