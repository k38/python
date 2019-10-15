import difflib

def main():
    a = difflib.ndiff('one\ntwo\nthree\n'.splitlines(keepends=True), 'ore\ntree\nemu\n'.splitlines(keepends=True))
    print(''.join(a), end="")

main()
