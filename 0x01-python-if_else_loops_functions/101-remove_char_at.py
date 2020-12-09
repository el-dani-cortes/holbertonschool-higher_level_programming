#!/usr/bin/python3
def remove_char_at(str, n):
    str_copy = ""
    lenght = len(str)
    for i in range(0, lenght):
        if(i != n):
            str_copy = str_copy + str[i]
    return (str_copy)
