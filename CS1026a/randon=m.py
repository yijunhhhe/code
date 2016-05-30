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
    numOfKeywords = 0
    sentimentValues = 0
    # Obtain every word in the tweets word list
    for word in tweetsWordList:
        print(word)
        word = word.rstrip()
        print(word)
        # find out if there are any words from tweets line in keywords list
        if word in keywordList:
            # Avoid Value Error
            try:
                indexOfSentimentWord = keywordList.index(word)
                sentimentValues = sentimentValues + int(keywordList[indexOfSentimentWord + 1])
                numOfKeywords = numOfKeywords + 1
            except ValueError:
                pass
    # Define latitude and longitude and pass value into it
    latitude = float(tweetsWordList[0].strip("[,"))
    longitude = float(tweetsWordList[1].strip("]"))
    print(tweetsWordList)
    print(sentimentValues)


    line = tweetFile.readline()

