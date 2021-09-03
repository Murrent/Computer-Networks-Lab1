def int2binary(i):
    if i == 0:
        return "0"
    b = ""
    while i > 0:
        if i % 2 == 1:
            b = '1' + b
        else:
            b = '0' + b
        i = int(i / 2)
    return b


print(int2binary(0))
print(int2binary(1))
print(int2binary(2))
print(int2binary(3))
print(int2binary(4))
print(int2binary(5))
print(int2binary(6))
print(int2binary(7))
print(int2binary(8))
print(int2binary(9))
