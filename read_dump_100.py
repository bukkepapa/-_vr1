with open('row_dump.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Printing lines with 'Index 10' (100-109):")
for line in lines:
    if "Index 10" in line:
        print(line.strip())
