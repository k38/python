import difflib

def main():
    print(''.join(difflib.context_diff('one\ntwo\nthree\nfour\n'.splitlines(True), 'zero\none\ntree\nfour\n'.splitlines(True), 'Original', 'Current')), end="")

main()
