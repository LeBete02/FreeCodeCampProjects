#Reading the txt file

fhand = open("File.txt")

fread = fhand.read()

print("No of characters:", len(fread))
print("Selected text:", fread[2:3])