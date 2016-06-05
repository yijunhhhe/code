def latandlong(lat,long):
    if 49.189787 >= lat >= 24.660845:
        if long <=-87.518395:
            return ("Eastern")
        elif long >= -87.518395 and long <= -101.998892:
            return ("Central")
        elif long >= -101.998892 and long <= -115.236428:
            return ("Mountain")
        elif long >= -115.236428 and long <=-125.242264:
            return ("Pacific")

def tweetHappinessScore(value1,keyword,parts2):
    numKeywords = 0
    tweetHappinessScore = 0
    for word in parts2:
        if word in keyword:
            numKeywords = numKeywords + 1
            wordIndex = keyword.index(word)  # find the index of this word in keyword list
            tweetHappinessScore = tweetHappinessScore + value1[wordIndex]
    if numKeywords > 0 :   # only when there is word in tweet in keyword list then you calculate the sentiment value
        sentimentalValue= tweetHappinessScore/numKeywords
    return sentimentalValue

keywordsFile= open(fileKeywords, "r")
keywords = keywordsFile.readline()
keyword = []
value1 = []
    for line in keywordsFile:
        if "," in line:
            parts1 = line.split(",")
            keyword.append(parts1[0])
            value1.append(int(parts1[1]))
tweetsFile = open(fileTweets, "r")
for line in tweetsFile:
    parts2 = line.split()
    lat = float(parts2[0].strip("[,"))
    long = float(parts2[1].strip("]"))
    timeZone= latandlong(lat, long)
    score = tweetHappinessScore(value1,keyword,parts2)

    if timeZone == "Eastern":
        easternNumberOfTweets = easternNumberOfTweets + 1
        easternHappinessScore = easternHappinessScore + score
    elif timeZone == "Central":
        centralNumberOfTweets = centralNumberOfTweets + 1
        centralHappinessScore = centralHappinessScore + score
    elif timeZone == "Mountain":
        mountainNumberOfTweets = mountainNumberOfTweets + 1
        mountainHappinessScore = mountainHappinessScore + score
    elif timeZone == "Pacific":
        pacificNumberOfTweets = pacificNumberOfTweets + 1
        pacificHappinessScore = pacificHappinessScore + score