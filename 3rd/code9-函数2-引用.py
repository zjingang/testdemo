
# 2、引用当做实参
def test1(a):
    print(a)
    print(id(a))
    a += a
    print(a)
    print(id(a))
b = 100
test1(b)
c = [11,22]
test1(c)


