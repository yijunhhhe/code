def determineTimeZone(line, tweetsWordList):

    latitude = float(tweetsWordList[0].strip("[,"))
    longitude = float(tweetsWordList[1].strip("]"))
    if -125.242264 < longitude <= -115.236428:
        timeZone = "Pacific"
    elif -115.236428 < longitude <= -101.998892:
        timeZone = "Mountain"
    elif -101.998892 < longitude <= -87.518395:
        timeZone = "Central"
    else:
        timeZone = "Eastern"

def computeRegionSentiment(timeZone,):
    if timeZone = "Pacific":
        pacific.append()
def computeRegionSentiment(timeZone, pacific, mountain, central, eastern, scoreOfTheTweet):
    if timeZone == "Pacific":
        pacific.append(scoreOfTheTweet)
    elif timeZone == "Mountain":
        mountain.append(scoreOfTheTweet)
    elif timeZone == "Central":
        central.append(scoreOfTheTweet)
    elif timeZone == "Eastern":
        eastern.append(scoreOfTheTweet)
def computeScoreOfTheTweet(tweetsWordList,keywordList):
    numOfKeywords = 0
    sentimentValues = 0
    # Obtain every word in the tweets word list
    for word in tweetsWordList:
        # find out if there are any words from tweets line in keywords list
        if word in keywordList:
            # Avoid Value Error
            try:
                indexOfSentimentWord = keywordList.index(word)
                sentimentValues = sentimentValues + int(keywordList[indexOfSentimentWord + 1])
                numOfKeywords = numOfKeywords + 1
            except ValueError:
                pass
    if numOfKeywords > 0:
        scoreOfTheTweet = sentimentValues/numOfKeywords
        return scoreOfTheTweet
    else:
        return