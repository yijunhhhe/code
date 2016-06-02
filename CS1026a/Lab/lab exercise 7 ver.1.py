
keywordFile = open("keywords.txt","r")
keywordList = []
positive = []
neutral = []
negative = []
sentiment = 0
string = "I really am very happy for you I love the weather I am also sad and have some regrets about being so tired"
for line in keywordFile:
    line = line.strip()
    line = line.split(",")
    for word in line:
        word.strip(" ")
        keywordList.append(word)
    for i in range (1,len(keywordList),2):
        if int(keywordList[i]) == 20:
            if keywordList[i - 1] not in positive:
                positive.append(keywordList[i - 1])
        elif int(keywordList[i]) == 0:
            if keywordList[i - 1] not in neutral:
                neutral.append(keywordList[i - 1])
        elif int(keywordList[i]) == -10:
            if keywordList[i - 1] not in negative:
                negative.append(keywordList[i - 1])
string = string.split(" ")
for word in string:
    if word in keywordList:
        index = keywordList.index(word)
        sentiment = sentiment + int(keywordList[index + 1])

print("The positive keywords are {}\n"
      "The negative keywords are {}\n"
      "The neutral keywords are {}\n"
      "The sentiment of the tweet is {}".format(positive,negative,neutral,sentiment)      )


