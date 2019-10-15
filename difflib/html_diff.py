import difflib

def main():
    a = "、、ファイルとディレクトリの比較"
    b = "ファイル"
    # a = "aaa"
    # b = "aab"
    c = difflib.HtmlDiff()
    d = c.make_file(a, b)
    # d = c.make_table(a, b)
    print(d)

main()
