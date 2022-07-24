#Parsing and Extracting from String

data = " You can find me at https://www.freecodecamp.org/LeBete02 "

pre_str = data.find("/L")
post_str = data.find(" ", pre_str)

extract_str = data[(pre_str + 1) : post_str]

print("Username: ", extract_str)