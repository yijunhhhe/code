#$34.34,table salt,3
#$1,245.00,ipad,2
inf = open('Example3.txt', 'r')
itemList = []
costList = []

for line in inf:
    elements = line.rsplit(',',2)
    itemList.append(int(elements[2]))
    if "," in elements[0]:
        x = elements[0].split(',')
        num = ""
        for e in x:
            num = num+e
        elements[0] = num
    costList.append(float(elements[0].lstrip('$')))

average = sum(costList)/sum(itemList)
print("The average cost of ",sum(itemList) , " items is" ,"$"+str(round(average,2)))
