with open('row_dump.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("Printing lines 90-120 from row_dump.txt:")
for line in lines:
    if "Index" in line:
        try:
            idx = int(line.split(':')[0].replace('Index ', ''))
            if 90 <= idx <= 120:
                print(line.strip())
        except:
            pass
