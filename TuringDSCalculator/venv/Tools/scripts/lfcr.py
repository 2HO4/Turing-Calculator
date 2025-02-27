#! /usr/bin/venv python3

"Replace LF with CRLF in argument files.  Print names of changed files."

import sys, re, os

def main():
    for filename in sys.argv[1:]:
        if os.path.isdir(filename):
            print(filename, "Directory!")
            continue
        with open(filename, "rb") as f:
            data = f.read()
        if b'\0' in data:
            print(filename, "Binary!")
            continue
        newdata = re.sub(b"\r?\n", b"\r\n", data)
        if newdata != data:
            print(filename)
            with open(filename, "wb") as f:
                f.write(newdata)

if __name__ == '__main__':
    main()
