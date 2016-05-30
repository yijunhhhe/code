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
    return timeZone

def computeRegionSentiment(region):
    scoreOfRegion = sum(region)/len(region)
    return scoreOfRegion

def computeScoreOfTheTweet(tweetsWordList,keywordList):
    keyWordYes = False
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
        keywordYes = True
        return scoreOfTheTweet



import sys
# Name: Yijun He Student Number:

# Receive the input of keyword file's name
#keywordFileName = input("Please enter the name of keyword file: ")

# Make sure keywords file exists
try:
    keywordFile = open("keywords.txt", "r")
except IOError as fileNameError:
    print(fileNameError)
    sys.exit(0)

# Read lines from Keywords file and store it in list
line = keywordFile.readline()
keywordList = []
while line != "":
    wordList = line.split(",")
    for word in wordList:
        word = word.rstrip()
        keywordList.append(word)
    line = keywordFile.readline()

# Obtain the name of the tweets file
#tweetFileName = input("Please enter the name of the tweets file: ")

# Make sure tweets file exists
try:
    tweetFile = open("2.txt","r")
except IOError as fileNameError:
    print(fileNameError)
    sys.exit(0)

# Define different time zone as lists
pacific = []
mountain = []
central = []
eastern = []

# Read line from tweets file
line = tweetFile.readline()
while line != "":
    tweetsWordList = line.split(" ")
    scoreOfTheTweet = computeScoreOfTheTweet(tweetsWordList,keywordList)
    timeZone = determineTimeZone(line,tweetsWordList)
    if scoreOfTheTweet != None:
        if timeZone == "Pacific":
            pacific.append(scoreOfTheTweet)
        elif timeZone == "Mountain":
            mountain.append(scoreOfTheTweet)
        elif timeZone == "Central":
            central.append(scoreOfTheTweet)
        else:
            eastern.append(scoreOfTheTweet)
    line = tweetFile.readline()



scoreOfPacific = computeRegionSentiment(pacific)
scoreOfMountain = computeRegionSentiment(mountain)
scoreOfCentral = computeRegionSentiment(central)
scoreOfEastern = computeRegionSentiment(eastern)
print(scoreOfPacific,scoreOfMountain,scoreOfCentral,scoreOfEastern)



