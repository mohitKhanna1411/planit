out = ""
for string in range(1, 101):
    if string % 3 == 0 and string % 5 == 0:
        out += "PlanitTesting "
        continue
    elif string % 3 == 0:
        out += "Planit "
        continue
    elif string % 5 == 0:
        out += "Testing "
        continue
    out += str(string) + " "
print(out.strip())
