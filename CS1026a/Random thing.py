if sentimentValues != 0 and 24.660845 < latitude < 49.189787 and -125.242264 < longitude < -67.444574:
        scoreOfTheTweet = sentimentValues/numOfKeywords
        if -125.242264 < longitude <= -115.236428:
            pacific.append(scoreOfTheTweet)
        elif -115.236428 < longitude <= -101.998892:
                mountain.append(scoreOfTheTweet)
        elif -101.998892 < longitude <= -87.518395:
                central.append(scoreOfTheTweet)
        else:
                eastern.append(scoreOfTheTweet)