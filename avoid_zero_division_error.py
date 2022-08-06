def div_zero(object):
    def wrap(x, y):
        print(("Running Divison").center(20, '*'))
        if y == 0:
            print("can't Divid by zero")
            print(("Division Done").center(20,  '!'))
            return
        result = object(x, y)
        print(("Division Done").center(20, '*'))
        return result
    return wrap

@div_zero
def f(x, y):
    return print(x % y)

f(2, 2)



