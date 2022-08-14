#Average with input

net_val = 0
n = 0

while True:
    inp = input("Enter number: ")
    if inp == "done":
        break
    net_val = net_val + float(inp)
    n= n+1

average = net_val/n

print("Average number = ", average)