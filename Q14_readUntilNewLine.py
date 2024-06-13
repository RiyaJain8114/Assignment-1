lines = []
while True:
    line = input()
    if not line:
        break
    lines.append(line)
print("You entered:")
for line in lines:
    print(line)
