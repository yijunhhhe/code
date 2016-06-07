# TODO: type solution here
name = ["Stirling","Lana","Cyril","Pam","Ray","Cheryl"]
alias =["Duchess","Truckasaurus","Chet","Cookie Monster","Gilles de Rais","Cherlene"]
dic = {}
for i in range(len(name)):
    dic[name[i]] = alias[i]
for key in sorted(dic):
    print(key,":",dic[key])
