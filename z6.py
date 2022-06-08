def main(x):
    if x[1]== 1979:
        return p1979(x)
    elif x[1]== 1980:
        return p1980(x)


def p1979(x):
    if x[2] == 'ZIMPL':
        if x[0]==1969:
            return 0
        elif x[0]==1980:
            return 1
        elif x[0] == 1957:
            return 2
    elif x[2] == 'METAL':
        if x[0] == 1969:
            return 3
        elif x[0]==1980:
            return 4
        elif x[0] == 1957:
            return 5
    elif x[2] == 'PLSQL':
        if x[0] == 1969:
            return 6
        elif x[0] == 1980:
            return 7
        elif x[0] == 1957:
            return 8




def p1980(x):
    if x[0] == 1969:
        if x[2] == 'ZIMPL':
            return 9
        elif x[2] == 'METAL':
            return 10
        elif x[2] == 'PLSQL':
            return 11
    elif x[0] == 1980:
            return 12
    elif x[0] == 1957:
            return 13


print(main([1980, 1979, 'METAL', 1995]))
print(main([1980, 1980, 'ZIMPL', 2015]))