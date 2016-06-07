episode4 = {"Luke","Leia","Han","Chewie","C3PO","R2-D2","Vader","Greedo","Kenobi"}
episode5={"Luke","Leia","Han","Chewie","C3PO","R2-D2","Vader","Tauntaun","Yoda","Lando"}
episode6={"Luke","Leia","Han","Chewie","C3PO","R2-D2","Vader","Palpatine","Ackbar","Jabba","Rancor","Boba","Yoda"}

#code to create intersection of 4 and 5 then take episode 6 and difference that with the intersection of 4 and 5
interserction = episode4.intersection(episode5)

final = episode6.difference(interserction)



print(len(final))