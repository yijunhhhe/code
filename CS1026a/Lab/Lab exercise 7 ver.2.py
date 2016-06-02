
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
    if int(line[1]) == 20:
        if line[0] not in positive:
            positive.append(line[0])
    elif int(line[1]) == 0:
        if line[0] not in neutral:
            neutral.append(line[0])
    elif int(line[1]) == -10:
        if line[0] not in negative:
            negative.append(line[0])
    for word in line:
        word.strip(" ")
        keywordList.append(word)

string = string.split(" ")
for word in string:
    if word in keywordList:
        index = keywordList.index(word)
        sentiment = sentiment + int(keywordList[index + 1])

print("The positive keywords are {}\n"
      "The negative keywords are {}\n"
      "The neutral keywords are {}\n"
      "The sentiment of the tweet is {}".format(positive,negative,neutral,sentiment)      )


