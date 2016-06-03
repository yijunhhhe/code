openFile = open("","r")
price = []
amount = []
for line in openFile:
    line = line.rsplit(",",2)
    amount.append(int(line[2]))
    if "," in line[0]:
        x = line[0].split(",")
        num = ""
        for s in x:
            num = num + s
        line[0] = num
    price.append(float(line[0].lstrip("$")))
print(price)
print(amount)

