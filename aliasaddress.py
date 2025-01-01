original = 42.3
#below line prints the memomy location in a hex format
print(hex(id(original)))
temp = original #intiating another variable & pointing it to another variable
print(hex(id(temp)))
if hex(id(original)) == hex(id(temp)): #Checking if both variable are pointing to same memory location
    print('Both are pointing to same location')
    print(original)
    print(temp)

temp = 43.3 # Updating the temp variable value manually
#Now we are verifying that both varibale now has different value & pointing to new location as well.
print(hex(id(temp)),'-', hex(id(original)))
print(temp)
print(original)
print("Now both are pointing to diff location & variable")

