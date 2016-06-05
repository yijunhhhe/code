# Name: Yijun He
# Student Number: 250892341
# Class: CS1026A
# This program intends to calculate sentiment value of each tweet based on keywords and its corresponding value
# Then compute the happiness score of each region which is the total score of all tweets divided by the number of tweets

# import sys module
import sys

## This function determine which time zone the twitter was in
# @param tweetsWordList a list consisting of each word from a line
# @return the time zone
def determineTimeZone(tweetsWordList):
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

## This function compute the sentiment value for each region
# @param region a list consisting of tweets from each region
# @return the total "happiness score" of each region
def computeRegionSentiment(region):
    scoreOfRegion = sum(region)/len(region)
    return scoreOfRegion

## This function compute the sentiment value for each tweet
# @Param tweetsWordList indicating a list consisting of each word from a line
# @Param keywordList indicating a list consisting of all keywords
# @return the happiness score of each tweet
def computeScoreOfTheTweet(tweetsWordList,keywordList):
    numOfKeywords = 0
    sentimentValues = 0
    # Obtain every word in the tweets word list
    for word in tweetsWordList:
        word = word.rstrip(".?',@[]!/")
        # find out if there are any words from tweets line in keywords list
        if word in keywordList:
            # Avoid Value Error
            try:
                indexOfSentimentWord = keywordList.index(word)
                sentimentValues = sentimentValues + int(keywordList[indexOfSentimentWord + 1])
                numOfKeywords = numOfKeywords + 1
            except ValueError:
                pass
    # ignore the line without keywords
    if numOfKeywords > 0:
        scoreOfTheTweet = sentimentValues/numOfKeywords
        return scoreOfTheTweet

def main():
    # Receive the input of keyword file's name
    keywordFileName = input("Please enter the name of keyword file: ")

    # Make sure keywords file exists
    try:
        keywordFile = open(keywordFileName, "r")
    except IOError as fileNameError:
        print(fileNameError)
        sys.exit(0)

    # Read lines from Keywords file and store it in keyword list
    line = keywordFile.readline()
    keywordList = []
    while line != "":
        wordList = line.split(",")
        for word in wordList:
            word = word.rstrip()
            keywordList.append(word)
        line = keywordFile.readline()

    # Obtain the name of the tweets file
    tweetFileName = input("Please enter the name of the tweets file: ")

    # Make sure tweets file exists
    try:
        tweetFile = open(tweetFileName,"r",encoding="utf-8", errors='ignore')
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
        tweetsWordList = line.split()
        # Compute the score of each tweet
        scoreOfTheTweet = computeScoreOfTheTweet(tweetsWordList,keywordList)
        # find the time zone the tweet was in
        timeZone = determineTimeZone(tweetsWordList)
        # Ignore the tweet without keywords and outside time zone
        # add the score of the tweet to corresponding time zone
        if scoreOfTheTweet != None and timeZone != "":
            if timeZone == "Pacific":
                pacific.append(scoreOfTheTweet)
            elif timeZone == "Mountain":
                mountain.append(scoreOfTheTweet)
            elif timeZone == "Central":
                central.append(scoreOfTheTweet)
            else:
                eastern.append(scoreOfTheTweet)
        # Read next line
        line = tweetFile.readline()

    # Calculate the score of each region
    scoreOfPacific = computeRegionSentiment(pacific)
    scoreOfMountain = computeRegionSentiment(mountain)
    scoreOfCentral = computeRegionSentiment(central)
    scoreOfEastern = computeRegionSentiment(eastern)

    # print the results
    print("The happiness score in pacific is: {}, and the number of tweets is: {}\n"
          "The happiness score in Mountain is: {}, and the numebr of tweets is: {}\n"
          "The happiness score in Central is: {}, and the numebr of tweets is: {}\n"
          "The happiness score in Eastern is: {}, and the numebr of tweets is: {}\n"
          .format(scoreOfPacific, len(pacific), scoreOfMountain, len(mountain),
                  scoreOfCentral, len(central), scoreOfEastern, len(eastern)))

    keywordFile.close()
    tweetFile.close()

main()

