# Martin Vickgren

def int2binary(i):
    if i == 0:              # If int is 0, binary = 0
        return "0"              # return binary number "0"
    b = ""                  # Create new string to build binary value
    while i > 0:            # We loop until i is 0 or less
        if i % 2 == 1:          # If the rest of i / 2 is equal to 1:
            b = '1' + b             # We add '1' to the front of the string
        else:                   # Otherwise:
            b = '0' + b             # We add '0' to the front of the string
        i = int(i / 2)          # We then divide i with 2 and clamp it down to nearest integer
    return b                # returns the newly built binary string


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
# for i in range(100):
#     print(int2binary(i))
