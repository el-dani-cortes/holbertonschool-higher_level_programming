#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    list_names = dir(hidden_4)
    for names in list_names:
        if (names[0:1] != "_"):
            print("{:s}".format(names))
