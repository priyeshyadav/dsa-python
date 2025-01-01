original = 42.3
#below line prints the memomy location in a hex format
print(hex(id(original)))
temp = original
print(hex(id(temp)))
if hex(id(original)) == hex(id(temp)):
    print('Both are pointing to same location')
    print(original)
    print(temp)

temp = 43.3
print(hex(id(temp)),'-', hex(id(original)))
print(temp)
print(original)
print("Now both are pointing to diff location & variable")

