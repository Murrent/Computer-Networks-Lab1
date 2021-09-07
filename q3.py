def changeChar(str, index, newChar):
    if index < 0 or index > len(str) - 1:   # index is out of range
        return str                              # return input str
    tmp = ""                                # Create new temporary string
    for i in range(len(str)):               # Loop through str
        if i == index:                          # If we are at the index we want to change
            tmp += newChar                          # Add the new char to tmp instead of the original char
        else:
            tmp += str[i]                           # Otherwise we add the original to tmp
    return tmp                              # return the modified string


thing = "Let's walk"

print(thing)
thing = changeChar(thing, 6, 'G')
thing = changeChar(thing, 7, 'O')
thing = changeChar(thing, 8, '!')
thing = changeChar(thing, 9, '!')
print(thing)
