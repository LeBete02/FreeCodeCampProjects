#Counting lines in a txt file

fhand = open("File.txt")

count = 0

for line in fhand:
    count = count + 1

print("Line Count: ", count)