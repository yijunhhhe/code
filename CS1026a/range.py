    try:
        if sentimentValues != 0 and 24.660845 < float(tweetsWordList[0][0]) < 49.189787 and -125.242264 < float(tweetsWordList[0][1]) < -67.444574:
            scoreOfTheTweet = sentimentValues/numOfKeywords

            if -125.242264 < float(tweetsWordList[0][1]) < -115.236428:
                pacific.append(scoreOfTheTweet)
    except ValueError:
        pass
    line = tweetFile.readline()

scoreOfTimeZone = sum(pacific)/len(pacific)
print(scoreOfTimeZone)

