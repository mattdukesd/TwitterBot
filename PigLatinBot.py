
# coding: utf-8

# In[ ]:

from itertools import takewhile
import random
import tweepy
import json
import numpy as np
import time

#infinite loop
while(True):

    # Twitter API Keys
    consumer_key = "XJooc84KrySr8PYm52t7PgMQ9"
    consumer_secret = "EJdLnorVol2yhQgrj8rRQUCUB4Ytymb46TPDCLCGVFdUW9nGnL"
    access_token = "937016298659180544-M45OhNqdS5y5UPwrRJL5XpBnEYU1FOX"
    access_token_secret = "sFVR1upTLGrF3Xvx1If7MxHjBTAzGwBLkEVjTG5EJbqOq"

    # Setup Tweepy API Authentication
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    #list of interesting accounts
    user_list = ['@realDonaldTrump','@SteveMartinToGo','@badbanana','@OfficialKat','@Pundamentalism',
                 '@AlYankovic','@pourmecoffee','@KenJennings','@chuck_facts','@Lord_Voldemort7','@big_ben_clock',
                 '@BronxZooCobra','@SeinfeldToday','@EveryWord','@factsandtrivia','@Preschoolgems',
                 '@NYTOnIt','@TweetsOfOld','@elonmusk','@Wendys','@kanyewest','@SheNegotiates']
   
    #pick random account
    target_user = user_list[random.randint(0,21)]

    #Get the latest tweet
    public_tweets = api.user_timeline(target_user, page=1, tweet_mode='extended')
    target_tweet = public_tweets[0]['full_text']
    
    #set lists
    random_addon_list = ['way','hay','yay']
    punctuation_list = ['.',',',':',';','!','?','-','*','%','&','"',"'",'(',')','+','/']
    vowel_list = ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']
    split_tweet = target_tweet.split()
    new_split = []
    new_split.append('RT '+ target_user + ':')

    for word in split_tweet: 
        #don't touch certain words, particularly for twitter
        if word[0] == '$' or word[0] == '@' or word[0] == '#' or word in punctuation_list:
            new_split.append(word)
        
        #remove links and images    
        elif 'http' in word or word[0:3] == '<img' or word[0:3] == 'div.' or '.jpg' in word:
            word = ""
      
        #convert everything else to pig latin
        else:            
            #create empty lists and strings    
            punct_begin = []
            punct_b = ''
            punct_end = []
            punct_e = ''
            new_string = ''

            #remove and preserve beginning punctuation
            while word[0] in punctuation_list:
                punct_begin.append(word[0])
                word = word[1:]
             
            #create string with stripped punctuation
            for punct in punct_begin:
                punct_b += str(punct)
                
            #convert Mr. and Mrs. to longform
            if word == 'Mr.':
                word = 'Mister'
            
            if word == 'Mrs.':
                word = 'Miss'

            #remove and preserve ending punctuation       
            while word[-1] in punctuation_list:
                punct_end.insert(0,word[-1])
                word = word[:-1]
            
            #create string with stripped punctuation
            for punct in punct_end:
                punct_e += str(punct)

            #if word starts with a vowel and upper - modify word then add back upper   
            if word[0] in vowel_list and word.isupper() and len(word) != 1:                                       
                random_addon = random_addon_list[random.randint(0,2)]
                word = (word + random_addon).upper()

            #modify word starting with vowel
            elif word[0] in vowel_list and word[-1].islower() and len(word) != 1:
                random_addon = random_addon_list[random.randint(0,2)]
                word = word + random_addon

            #modify word starting with a vowel and only one character long
            elif word[0] in vowel_list and len(word) == 1:
                random_addon = random_addon_list[random.randint(0,2)]
                word = word + random_addon

          #if word starts with a consonant and upper - modify word then upper  
            elif word[0] not in vowel_list and word.isupper() and len(word) != 1:
                word = word[len(list(takewhile(lambda x: x not in "AEIOU", word))):] + word[:len(list(takewhile(lambda x: x not in "AEIOU", word)))] + 'ay'
                word = word.upper()

            #if word starts with a consonant and and title - modify word then add back title  
            elif word[0] not in vowel_list and word[0].isupper() and word[-1].islower() or word[0] not in vowel_list and word.isupper() and len(word) == 1:
                word = word[len(list(takewhile(lambda x: x not in "aeiou", word))):] + word[:len(list(takewhile(lambda x: x not in "aeiou", word)))] + 'ay'
                word = word.title()

            #modify word starting with consonant not title or upper
            else:
                word = word[len(list(takewhile(lambda x: x not in "aeiou", word))):] + word[:len(list(takewhile(lambda x: x not in "aeiou", word)))] + 'ay' 

            #Concatenate preserved punctuation with modified text and append to list    
            new_string = punct_b + word + punct_e
            new_split.append(new_string)
                
    #join list to string
    pig_latin_string = ' '.join(new_split)
    
    #make sure we don't go over character limit with additional characters
    eettway = pig_latin_string[:279]
    
    #post new tweet
    api.update_status(eettway)     

    #create random time
    time_list1 = np.random.randint(low=25000,high=50000,size=15)
    time_list2 = np.random.randint(low=2500,high=50000,size=15)
    time_value = time_list1[(np.random.randint(low=0,high=14,size=1))] + time_list2[(np.random.randint(low=0,high=14,size=1))]

    #sleep
    time.sleep(time_value)  


# In[ ]:



