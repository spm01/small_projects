user_input = input("What's on your mind today? ") # getting the user's input

word_count = len(user_input.split()) #take the length of the string and break it into substrings (typically uses whitespace)
print("You just told me how you're doing in " + str(word_count) + " words!") #remember to convert word_count back into a string when printing
