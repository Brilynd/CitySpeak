import os
import tweepy as tw
import pandas as pd
import threading


# convert to a DataFrame and keep only relevant columns
#df = pd.DataFrame(sliced_scraped_tweets)[['date', 'content']]
consumer_key = "1k6AdpDFORmdIMtUF53RzPDb9"
consumer_secret = "03wn9Q9Zan0He2M8lLF8gvBa2Qq1DY0q6PymZIEVIfe6lqOmEY"
access_key= "1512860430343061508-N86rMhNI3J9gbQS7VcYBDrmYlLJDvi"
access_secret = "PIleHq0btFTsbTy2aoDjDaQC6627EB4ld5Su4oAtW9OB9"
auth=tw.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_key,access_secret)
api = tw.API(auth,wait_on_rate_limit=True)
# Collect tweets: @user  tweet
l=[]
def tweets():
    search_words = "Joe Biden -filter:retweets"
    tweets = tw.Cursor(api.search_tweets,
                  q=search_words,
                  lang="en").items(1000)
    #print(tweets)
    # Iterate and print tweets
    
    
    for tweet in tweets:
        l.append(tweet.text)
    return l
    print(l)
# Collect tweets
#tweets = tw.Cursor(api.search_tweets,
#                       q=search_words,
#                       lang="en",
#                       since=date_since).items(5)


# Collect a list of tweets :table of users and locations
users_locs=[]
def loc():
    new_search = "Donald Trump" + " -filter:retweets"
    date_since = "2018-11-16"
    tweets = tw.Cursor(api.search_tweets, 
                               q=new_search,
                               lang="en").items(1000)

    users_locs = [[tweet.user.screen_name, tweet.user.location] for tweet in tweets]
    print('a',users_locs)
    ##locs=[]
    ##for i in users_locs:
    ##    #put regex here
    ##    if len(i[1])>0:
    ##        #print(i)
    ##        if len(i[1].split()[1])==2:
    ##            locs.append(i)
    ##
        
    [tweet.text for tweet in tweets]

    tweet_text = pd.DataFrame(data=users_locs, 
                        columns=['user', "location"])

    return tweet_text
    print(tweet_text)
print('............................................')
##
##
##print("ID of process running main program: {}".format(os.getpid()))
##  
##    # print name of main thread
##print("Main thread name: {}".format(threading.current_thread().name))
##
##  
##t1 = threading.Thread(target=tweets(), name='t1')
###t1.start()
##
##t2 = threading.Thread(target=tweets(),  name='t2')
##
##t1.start()
##t2.start()
##
##t1.join()
##    # wait until thread 2 is completely executed
##t2.join()
##print(l)
##
##
##t3 = threading.Thread(target=loc(), name='t3')
###t1.start()
##
##t4 = threading.Thread(target=loc(),  name='t4')
##
##t3.start()
##t4.start()
##
##t3.join()
##    # wait until thread 2 is completely executed
##t4.join()
##print(users_locs.append(users_locs))
##print(len(users_locs))
d={}
c=0
users_locs=loc()
l=tweets()
for i in users_locs:
    d[i[0]]=[i[1],l[c]]
    c+=1
print(d)



##
##userl={}
##for i in l:
##    if i.split()[0][0]=="@":
##        userl[i.split()[0]]=i
##
##lst_dir={}
##for i in userl.keys():
##    x=userl[i].split()
##    string=''
##    for j in x:
##        
##        if j[0]!="@":
##            #print(j)
##            string=string+j+" "
##    lst_dir[i]=string
###print(lst_dir)
##
##final_dir={}
##for i in users_locs:
##    
##    if i[0] in lst_dir.keys():
##        
##        for j in lst_dir.keys():
##            l=[]
##            
##            if i[0]==j:
##                
##                l.append(i[1])
##                
##                l.append(lst_dir[j])
##                final_dir[j]=l
##
##print('final directory:',final_dir)
##
