def increasing(line):
    for i in range(0,len(line)-1):
        if line[i] > line[i+1]:
             return False

    return True

