import difflib

def main():
    a = "ファイルとディレクトリの比較"
    b = "ファイル"
    # a = "aaa"
    # b = "aab"
    c = difflib.Differ()
    d = c.compare(a, b)
    print(list(d))

main()
