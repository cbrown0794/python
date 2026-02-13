# Print the first __ letters of a string, followed by ..., followed by the ____ __ letters of a string.

#initialize the string
string = "Polytechnic"

#display the result
print("%s...%s" % (string[0 : 3], string [len(string) - 3 : len(string)]))
