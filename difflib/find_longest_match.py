import difflib

def main():
    s = difflib.SequenceMatcher(None, " abcd", "abcd abcd")
    a = s.find_longest_match(0, 5, 0, 9)
    # a = difflib.Match(a=0, b=4, size=5)
    print(a)

main()
