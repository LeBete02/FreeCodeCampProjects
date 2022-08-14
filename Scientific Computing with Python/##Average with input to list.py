##Average with input to list

num_list = list()

while True:
    inp = input("Enter number: ")
    if inp == "done":
        break
    num_list.append(float(inp))

average = sum(num_list)/len(num_list)

print("List of numbers =", num_list)
print("Average number = ", average)