def determineTimeZone(line, tweetsWordList):
    latitude = float(tweetsWordList[0].strip("[,"))
    longitude = float(tweetsWordList[1].strip("]"))
    if  24.660845 < latitude < 49.189787:
        if -125.242264 < longitude <= -115.236428:
            timeZone = "Pacific"
        elif -115.236428 < longitude <= -101.998892:
            timeZone = "Mountain"
        elif -101.998892 < longitude <= -87.518395:
            timeZone = "Central"
        elif -87.518395 < longitude <= -67.444574:
            timeZone = "Eastern"
        else:
            timeZone = ""
    else:
        timeZone = ""
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
        word = word.rstrip(".?',!/")
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
    tweetFile = open("1.txt","r")
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
count = 1
while line != "":
    tweetsWordList = line.split(" ")
    scoreOfTheTweet = computeScoreOfTheTweet(tweetsWordList,keywordList)
    timeZone = determineTimeZone(line,tweetsWordList)

    print(count, scoreOfTheTweet)
    print(timeZone)
    if scoreOfTheTweet != None and timeZone != "":
        if timeZone == "Pacific":
            pacific.append(scoreOfTheTweet)
        elif timeZone == "Mountain":
            mountain.append(scoreOfTheTweet)
        elif timeZone == "Central":
            central.append(scoreOfTheTweet)
        else:
            eastern.append(scoreOfTheTweet)
    line = tweetFile.readline()
    count = count + 1


try:
    scoreOfPacific = computeRegionSentiment(pacific)
    scoreOfMountain = computeRegionSentiment(mountain)
    scoreOfCentral = computeRegionSentiment(central)
    scoreOfEastern = computeRegionSentiment(eastern)
except ZeroDivisionError:
    pass
print(scoreOfPacific,scoreOfMountain,scoreOfCentral,scoreOfEastern)



