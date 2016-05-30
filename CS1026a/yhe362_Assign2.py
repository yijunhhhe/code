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

# Read lines from Keywords file
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
    tweetFile = open("tweetss.txt","r")
except IOError as fileNameError:
    print(fileNameError)
    sys.exit(0)

pacific = []
line = tweetFile.readline()
while line != "":
    tweetsWordList = line.split(" ")
    numOfKeywords = 0
    sentimentValues = 0
    for word in tweetsWordList:
        if word in keywordList:
            try:
                indexOfSentimentWord = keywordList.index(word)
                sentimentValues = sentimentValues + int(keywordList[indexOfSentimentWord + 1])
                numOfKeywords = numOfKeywords + 1
            except ValueError:
                pass


