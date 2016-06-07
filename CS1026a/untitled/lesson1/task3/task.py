sentence ="I had such a horrible day. It was awful so bad sigh. It could not have been worse but actually though "\
          +"such a terrible horrible awful bad day."

makeItHappy ={"horrible":"amazing","bad":"good","awful":"awesome","worse":"better","terrible":"great"}

sentenceList = sentence.split()
newString = ""
for key in makeItHappy:
    for i in range(len(sentenceList)):
        if sentenceList[i] == key:
            sentenceList[i] = makeItHappy[key]

for i in range(len(sentenceList)):
    newString = newString + sentenceList[i] + " "


print(newString)


