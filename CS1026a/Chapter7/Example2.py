from random import randint
outfile = open("out.txt", "w")
for i in range(20):
    #print(randint(100,200), file=outfile,end=", ",)
    #outfile.write(str(randint(100,200))+ ", ")
    outfile.write("%d, "%(randint(100,200)))

outfile.close()