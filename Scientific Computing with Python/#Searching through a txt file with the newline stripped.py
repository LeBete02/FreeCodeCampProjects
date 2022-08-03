"""
#Searching through a txt file with the /n stripped and startswith function

fhand = open("File.txt")

for line in fhand:
    line = line.rstrip()
    if line.startswith("From:"):
        print(line)
"""


"""
#Skipping with continue

fhand = open("File.txt")

for line in fhand:
    line = line.rstrip()
    if not line.startswith("From:"):
        continue
    print(line)
"""


"""

#Using in to look for a string

fhand = open("File.txt")

for line in fhand:
    line = line.rstrip()
    if not "faiyaz" in line:
        continue
    print(line)

"""


"""
#Prompt for file name

fname = input("Enter the file name: ")
fhand = open(fname)
count = 0

for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject lies in", fname)
"""


"""
#Bad file name failsafe

fname = input("Enter the file name: ")

try:
    fhand = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

count = 0

for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1
print("There were", count, "subject lies in", fname)
"""