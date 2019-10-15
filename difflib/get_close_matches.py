import difflib

def main():
    # a = difflib.get_close_matches('appel', ['ape', 'apple', 'peach', 'puppy'])
    a = difflib.get_close_matches('宮川大助', ['井上大助', '宮内義彦', '宮川大輔', '松坂大輔'])
    print(a)

main()
