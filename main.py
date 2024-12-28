while (exp := input()):
    try:
        res = eval(exp)
        print(exp + ' = ' + str(res))
    except Exception as error:
        print(error)
    