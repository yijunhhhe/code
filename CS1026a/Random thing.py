#Name: Eun Seo Pak
#Course: CS1026- Assignment 2
#Program Description: A program that analyzes Twitter information. This is a sentiment analysis where it determines key words and phrases in tweets and show their happiness score. It will determine the happiness score for each of the four timezones and the number of tweets found in that timezone.
#storing variables
def latandlong(lat,long):
    timeZone = ""
    if 49.189787 >= lat >= 24.660845:
        if long <= -67.444574 and long >= -87.518395:
            timeZone = "Eastern"
        elif long <= -87.518395 and long >= -101.998892:
            timeZone = "Central"
        elif long <= -101.998892 and long >= -115.236428:
            timeZone = "Mountain"
        elif long <= -115.236428 and long >=-125.242264:
            timeZone = "Pacific"
    return timeZone

def tweetHappinessScore(value1,keyword,parts2):
    numKeywords = 0
    tweetHappinessScore = 0
    sentimentalValue = 0
    for eachWord in parts2:
        eachWord = eachWord.rstrip(",?!.[]@")
        if eachWord in keyword:
            numKeywords = numKeywords + 1
            wordIndex = keyword.index(eachWord)  # find the index of this word in keyword list
            tweetHappinessScore = tweetHappinessScore + value1[wordIndex]
    if numKeywords > 0 :   # only when there is word in tweet in keyword list then you calculate the sentiment value
        sentimentalValue = tweetHappinessScore/numKeywords
    return sentimentalValue


timeZone= 0
score= 0

#prompting user for the name of the file containing the keywords and tweets
fileTweets = input("Input file name:")
fileKeywords = input("Input file name:")
#reading the file with the keywords
keywordsFile= open(fileKeywords, "r")
keywords = keywordsFile.readline()    #reading the lines of the keywords file
keyword = []         #storing a list of all the keywords
value1 = []          #storing a list of all the values
listOfEastern = []
listOfCentral = []
listOfMountain = []
listOfPacific = []
for line in keywordsFile:
    if "," in line:
        parts1 = line.split(",")         #split
        keyword.append(parts1[0])        #before the comma, it is a keyword
        value1.append(int(parts1[1]))    #after the comma, it is the value of the keyword
tweetsFile = open(fileTweets, "r",encoding="utf-8", errors='ignore')
for line in tweetsFile:
    parts2 = line.split()
    lat = float(parts2[0].strip("[,"))
    long = float(parts2[1].strip("]"))
    print(lat,long)
    timeZone= latandlong(lat, long)
    score = tweetHappinessScore(value1,keyword,parts2)
    print(timeZone)
    print(score)

    if timeZone!= "" and score!= 0:
        if timeZone == "Eastern":
            listOfEastern.append(score)
        elif timeZone == "Central":
            listOfCentral.append(score)
        elif timeZone == "Mountain":
            listOfMountain.append(score)
        elif timeZone == "Pacific":
            listOfPacific.append(score)


print ("The happiness score of the Eastern Time Zone is", sum(listOfEastern)/len(listOfEastern) , "and the number of tweets found is", len(listOfEastern))
print ("The happiness score of the Central Time Zone is", sum(listOfCentral)/len(listOfCentral), "and the number of tweets found is", len(listOfCentral))
print ("The happiness score of the Mountain Time Zone is", sum(listOfMountain)/len(listOfMountain), "and the number of tweets found is", len(listOfMountain))
print ("The happiness score of the Pacific Time Zone is", sum(listOfPacific)/len(listOfPacific), "and the number of tweets found is", len(listOfPacific))