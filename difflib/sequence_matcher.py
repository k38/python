import difflib

def main():
    # a = "aaa"
    # b = "bbb"
    a = "aba"
    b = "abc"
    c = difflib.SequenceMatcher(None, a, b)
    print("{}:{}={}".format(a, b, c.ratio()))
    print("{}:{}={}".format(a, b, c.quick_ratio()))
    print("{}:{}={}".format(a, b, c.real_quick_ratio()))

    for item in c.get_matching_blocks():
        print(item)

main()
