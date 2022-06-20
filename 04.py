numberTree = [1, 2, 3, [4, 5], [6, [7, 8, 9]]]

def showNumber(tree):
    if isinstance(tree, list):
        for number in tree:
            showNumber(number)
    else:
        print("Number",tree)

showNumber(numberTree)