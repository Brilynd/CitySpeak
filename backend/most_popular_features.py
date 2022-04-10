import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import tweepy
import csv
import os
import pandas as pd

import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import spacy
from sklearn.model_selection import train_test_split
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.tokenize import RegexpTokenizer, WhitespaceTokenizer
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import string
from string import punctuation
import collections
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import en_core_web_sm

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity

# !pip3 install -U spacy
# !python3 -m spacy download en_core_web_sm

from sklearn.metrics import jaccard_score
import json

def function(file):

    tweets_bowl = pd.read_csv(filepath_or_buffer=file)
    print(tweets_bowl.head())

    def clean_text(df, text_field):
        df[text_field] = df[text_field].str.lower()
        df[text_field] = df[text_field].apply(lambda elem: re.sub(r"(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|^rt|http.+?", "", elem))  
        return df


    clean_tweets = clean_text(tweets_bowl, 'tweets')
    #print('clean:',clean_tweets.head())

    nlp = en_core_web_sm.load()
    tokenizer = RegexpTokenizer(r'\w+')
    lemmatizer = WordNetLemmatizer()
    stop = set(stopwords.words('english'))
    punctuation = list(string.punctuation) #already taken care of with the cleaning function.
    stop.update(punctuation)
    w_tokenizer = WhitespaceTokenizer()

                
    def furnished(text):
        final_text = []
        for i in w_tokenizer.tokenize(text):
    #     for i in text.split():
            if i.lower() not in stop:
                word = lemmatizer.lemmatize(i)
                final_text.append(word.lower())
        return " ".join(final_text)


                
    tweets_bowl.tweets = tweets_bowl.tweets.apply(furnished)
    user_tweet_dict={}
    for i in tweets_bowl.itertuples():
        user_tweet_dict[i[1]]=i[2]
    #print(tweets_bowl.sample(5))

    economy_related_words = '''agriculture infrastructure capitalism trading service sector technology  economical supply 
                              industrialism efficiency frugality retrenchment downsizing   credit debit value 
                             economize   save  economically
                             economies sluggish rise   rising spending conserve trend 
                             low-management  decline   industry impact poor  
                                profession    surplus   fall
                             declining  accelerating interest sectors balance stability productivity increase rates
                                pushing expanding stabilize  rate industrial borrowing struggling
                               deficit predicted    increasing  data
                              economizer analysts investment market-based economy   debt free enterprise
                             medium  exchange metric savepoint scarcity capital bank company stockholder fund business  
                             asset treasury tourism incomes contraction employment jobs upturn deflation  macroeconomics
                             bankruptcies exporters hyperinflation dollar entrepreneurship upswing marketplace commerce devaluation 
                             quicksave deindustrialization stockmarket reflation downspin dollarization withholder bankroll venture capital
                             mutual fund plan economy mortgage lender unemployment rate credit crunch central bank financial institution
                             bank rate custom duties mass-production black-market developing-countries developing economic-growth gdp trade barter 
                             distribution downturn economist'''

    social_related_words = '''sociable, gregarious societal friendly society socialization political  sociality 
                            interpersonal  ethnic socially party welfare public community socialist societies development
                                network humans socialism collective personal corporation social constructivism
                            relations volition citizenship brute   attitude rights socio 
                            socioeconomic ethics civic communal marital  sociale socialized communities     
                             policy   unions        
                            institutions values     governmental   organizations jamboree 
                             festivity    fairness  support  care  
                             sides   activism     unsocial psychosocial 
                            socializing psychological distributional  demographic  participation reunion 
                            partygoer partyism festive power network gala housewarming celebration counterparty   social-war
                            particularist interactional ideational asocial'''

    culture_related_words  = ''' ethnicity heritage modernity spirituality marxismmaterial culture 
                               ethos nationality humanism romanticism civilisation traditionalism genetics
                            kinship heredity marriage   indigenous  archeology  acculturate  
                           ontogenesis viniculture modern clothes     rooted 
                           cicero societies history roots influence geography historical folk origins 
                           phenomenon teleology ancient aspects perspective liberalism nowadays community style unique prevalent describes 
                             today  origin   modernity beliefs  genre barbarian ethnic 
                           colonization cultural universal organization western-civilization structuralism  culture 
                           heathen pagan transculturation culture peasant classicist nativism anarchy ungrown philosophic cult  
                           consciousness islamist bro-culture evolve cultic diaspora aftergrowth native cultural-relativism  
                           mongolian cosmopolitan epistemology lifestyles diversity chauvinism westernization materialism vernacular 
                           homogeneity otherness holism tusculanae disputationes primitivism superficiality hedonism discourse
                           puritanism modernism intellectualism  exclusiveness elitism  colonialism  
                           pentecostalism paganism nationwide expansion rural  auxesis kimono 
                           culturize alethophobia nettlebed japanification  dongyi clannishness insularity hybridity
                           westernisation foreignness worldview exclusionism enculturation ethnocentrism  confucianist vulgarization
                           shintoism  westernism denominationalism    deracination
                            eurocentrism  cosmologies  emotiveness bohemianism territorialism
                           philosophical-doctrine ethnic minority social-darwinism  theory cultural evolution belief systemfolk music 
                           traditional art house karl-marx   theorymedia  
                           film-theory art history museum studies cultural artifact'''

    health_related_words = '''disease obesity world health organization medicine nutrition well-being exercise welfare wellness health care public health 
                         nursing stress safety hygiene research social healthy condition aids epidemiology healthiness wellbeing
                         care illness medical dieteducation infectious disease environmental healthcare physical fitness hospitals 
                         health care provider doctors healthy community design insurance sanitation human body patient mental health
                          medicare agriculture health science fitnesshealth policy  weight loss physical therapy psychology pharmacy
                         metabolic organism human lifestyle status unhealthy upbeat vaccination sleep condom alcohol smoking water family
                         eudaimonia eudaemonia air house prevention genetics public families poor needs treatment communicable disease 
                         study protection malaria development food priority management healthful mental provide department administration
                         programs help assistance funding environment improving emergency need program affected schools private mental illness 
                         treat diseases preparedness perinatal fertility sickness veterinary sanitary pharmacists behavioral midwives
                         gerontology infertility hospitalization midwifery cholesterol childcare pediatrician pediatrics medicaid asthma 
                         pensions sicknesses push-up physical education body-mass-index eat well gymnastic apparatus tune up good morning 
                         bathing low blood-pressure heart attack health club ride-bike you feel good eczema urticaria dermatitis sunburn overwork 
                         manufacturing medical sociology need exercise run'''

    nlp = en_core_web_sm.load()
    tokenizer = RegexpTokenizer(r'\w+')
    lemmatizer = WordNetLemmatizer()
    stop = set(stopwords.words('english'))
    punctuation = list(string.punctuation)
    stop.update(punctuation)
    w_tokenizer = WhitespaceTokenizer()

    # clean the set of words
                
    def furnished(text):
        final_text = []
        for i in text.split():
            if i.lower() not in stop:
                word = lemmatizer.lemmatize(i)
                final_text.append(word.lower())
        return " ".join(final_text)

    economy = furnished(economy_related_words)
    social = furnished(social_related_words)
    culture = furnished(culture_related_words)
    health = furnished(health_related_words)
    # delete duplicates
    string1 = economy
    words = string1.split()
    economy = " ".join(sorted(set(words), key=words.index))
    #print(economy)
    string1 = social
    words = string1.split()
    social = " ".join(sorted(set(words), key=words.index))
    #print(social)
    string1 = culture
    words = string1.split()
    culture = " ".join(sorted(set(words), key=words.index))
    #print(culture)
    string1 = health
    words = string1.split()
    health = " ".join(sorted(set(words), key=words.index))
    #print(health)

    '''Vectorizing the sets of words, then standardizing them. TFIDF will be used in order to take care of the least 
    frequent words. Standardizing is cause TFIDF favors long sentences and there'll be inconsistencies between the length 
    of the tweets and the length of set of words.'''


    def get_vectors(*strs):
        text = [t for t in strs]
        #print('t',text)
        vectorizer = TfidfVectorizer()
        vectorizer.fit(text)
        return vectorizer.transform(text).toarray()

    #print(social)

    socialvector = get_vectors(social)
    economic_vector = get_vectors(economy)
    culture_vector = get_vectors(culture)
    health_vector = get_vectors(health)

    ## Vectorizing the tweets
    tv=TfidfVectorizer()
    # tweets_bowl = tweets_bowl.tweets.apply(get_vectors)
    # tweets_bowl.head()
    tfidf_tweets =tv.fit_transform(tweets_bowl.tweets)


    '''Jaccard similarity is good for cases where duplication does not matter, 
    cosine similarity is good for cases where duplication matters while analyzing text similarity. For two product descriptions, 
    it will be better to use Jaccard similarity as repetition of a word does not reduce their similarity.'''

    def jaccard_similarity(query, document):
        intersection = set(query).intersection(set(document))
        union = set(query).union(set(document))
        return len(intersection)/len(union)
    # jaccard_score(socialvector, economic_vector)

    #for similarity of 1 and 2 of column1
    # jaccard_similarity('dog lion a dog','dog is cat')


    def get_scores(group,tweets):
        scores = []
        for tweet in tweets:
            s = jaccard_similarity(group, tweet)
            scores.append(s)
        
        return scores

    # economic scores
    e_scores = get_scores(economy, tweets_bowl.tweets.to_list())
    #print(e_scores[-10:])
    # social scores
    s_scores = get_scores(social, tweets_bowl.tweets.to_list())
    #print(s_scores[-10:])
    # culture scores
    c_scores = get_scores(culture, tweets_bowl.tweets.to_list())
    #print(c_scores[-10:])
    # health scores
    h_scores = get_scores(health, tweets_bowl.tweets.to_list())
    #print(h_scores[:6])
    '''new df with names, and the jaccard scores for each group'''

    data  = {'names':tweets_bowl.screen_name.to_list(), 'economic_score':e_scores,
             'social_score': s_scores, 'culture_score':c_scores, 'health_scores':h_scores}
    scores_df = pd.DataFrame(data)
    
    #print(scores_df.head(20))

    '''Actual assigning of classes to the tweets'''

    def get_clusters(l1, l2, l3, l4):
        econ = []
        socio = []
        cul = []
        heal = []
        for i, j, k, l in zip(l1, l2, l3, l4):
            m = max(i, j, k, l)
            if m == i:
                econ.append(1)
            else:
                econ.append(0)
            if m == j:
                socio.append(1)
            else:
                socio.append(0)        
            if m == k:
                cul.append(1)
            else:
                cul.append(0)  
            if m == l:
                heal.append(1)
            else:
                heal.append(0)   
                
        return econ, socio, cul, heal

    l1 = scores_df.economic_score.to_list()
    l2 = scores_df.social_score.to_list()
    l3 = scores_df.culture_score.to_list()
    l4 = scores_df.health_scores.to_list()

    econ, socio, cul, heal = get_clusters(l1, l2, l3, l4)

    data = {'name': scores_df.names.to_list(), 'economic':econ, 'social':socio, 'culture':cul, 'health': heal}
    cluster_df = pd.DataFrame(data)
    print(cluster_df)

    e=[]
    s=[]
    c=[]
    h=[]
    u=[]
    for i in cluster_df.itertuples():
        u.append(i[1])
        e.append(i[2])
        s.append(i[3])
        c.append(i[4])
        h.append(i[5])
    

    d={}
    tweets_category={}
    count_tweets=0
    count_tweetsl=[]
    count_d=0
    for i in e:
        if i==1:
            count_tweets+=1
            count_d+=1
            
        #print(count_d,type(count_d))
        d[count_d]='economic'
    
    count_tweetsl.append(count_tweets)

    count_tweets=0   
    count=0
    for i in s:
        if i==1:
            count+=1
            count_tweets+=1
        d[count]='social'
    count_tweetsl.append(count_tweets)
        
    count_tweets=0
    count=0
    for i in c:
        if i==1:
            count+=1
            count_tweets+=1
        d[count]='cultural'
    count_tweetsl.append(count_tweets)

    count=0
    count_tweets=0
    for i in h:
        if i==1:
            count+=1
            count_tweets+=1
        d[count]='health'
    count_tweetsl.append(count_tweets)

    print(type(tweets_category))

    tweets_category['economic']=count_tweetsl[0]
    tweets_category['social']=count_tweetsl[1]
    tweets_category['culture']=count_tweetsl[2]
    tweets_category['health']=count_tweetsl[3]

    #print(tweets_category)
        
    
    popular=max(d.keys())
    #print('Most popular category:',d[popular])
    if d[popular]=='economic':
        index=e.index(max(e))
    if d[popular]=='social':
        index=s.index(max(s))
    if d[popular]=='cultural':
        index=c.index(max(c))
    if d[popular]=='health':
        index=h.index(max(h))
    user=u[index]
    #print('tweet:',user_tweet_dict[user])
    #print('user:',user)
    return([d[popular],user_tweet_dict[user],user,tweets_category])

'''
pivot_clusters = cluster_df.groupby(['name']).sum()
pivot_clusters['economic'] = pivot_clusters['economic'].astype(int)
pivot_clusters['social'] = pivot_clusters['social'].astype(int)
pivot_clusters['culture'] = pivot_clusters['culture'].astype(int)
pivot_clusters['health'] = pivot_clusters['health'].astype(int)
pivot_clusters['total'] = pivot_clusters['health'] + pivot_clusters['culture'] + pivot_clusters['social'] +  pivot_clusters['economic']
pivot_clusters.loc["Total"] = pivot_clusters.sum()  #add a totals row
print(pivot_clusters.shape)
pivot_clusters.tail()
fig = plt.figure(figsize =(10, 7)) 
a = pivot_clusters.drop(['total'], axis = 1)
plt.pie(a.loc['Total'], labels = a.columns)
plt.title('A pie chart showing the volumes of tweets under different categories.')
plt.show() '''

categories_d={}
#popular.to_json('output.json')
MA=function('MA.csv')
state=[]
popular_category=[]
tweet=[]
user=[]
data_frames=[]
analyticsl=[]
state.append('Massachuetts')
popular_category.append(MA[0])
tweet.append(MA[1])
user.append(MA[2])
analytics=MA[3]
analyticsl.append(analytics)
#print(x,'\n\n\n')
data_frames.append(MA[3])
categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl

print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 
print(json_object)
print('......................................')
#ak=function('ak.csv')
#az=function('az.csv')
#bur=function('Burlington.csv')
#ca=function('CA.csv')
#dc=function('DC.csv')
#de=function('De.csv')
fl=function('fl.csv')
state.append('Florida')
popular_category.append(fl[0])
tweet.append(fl[1])
user.append(fl[2])
analyticsl.append(fl[3])
categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl

#print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 

#ga=function('Ga.csv')
#il=function('IL.csv')
In=function('In.csv')
state.append('Indiana')
popular_category.append(In[0])
tweet.append(In[1])
user.append(In[2])
analyticsl.append(In[3])
categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl

#print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 

#Ks=function('Ks.csv')
#ma=function('MA.csv')
Md=function('Md.csv')
state.append('Maryland')
popular_category.append(Md[0])
tweet.append(Md[1])
user.append(Md[2])
analyticsl.append(Md[3])

categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl

#print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 

Mi=function('Mi.csv')
state.append('Michigan')
popular_category.append(Mi[0])
tweet.append(Mi[1])
user.append(Mi[2])
analyticsl.append(Mi[3])

categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl

#print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 

Mn=function('Mn.csv')
state.append('Minnesota')
popular_category.append(Mn[0])
tweet.append(Mn[1])
user.append(Mn[2])
analyticsl.append(Mn[3])
categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl
#print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 

Nc=function('Nc.csv')
state.append('North Carolina')
popular_category.append(Nc[0])
tweet.append(Nc[1])
user.append(Nc[2])
analyticsl.append(Nc[3])
categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl
#print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 

Nj=function('Nj.csv')
state.append('New Jersey')
popular_category.append(Nj[0])
tweet.append(Nj[1])
user.append(Nj[2])
analyticsl.append(Nj[3])
categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl
#print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 

Ny=function('Ny.csv')
state.append('New Yorl')
popular_category.append(Ny[0])
tweet.append(Ny[1])
user.append(Ny[2])
analyticsl.append(Ny[3])
categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl
#print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 

oh=function('Oh.csv')
state.append('Ohio')
popular_category.append(oh[0])
tweet.append(oh[1])
user.append(oh[2])
analyticsl.append(oh[3])
categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl
#print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 

ok=function('OK.csv')
state.append('Oklahoma')
popular_category.append(ok[0])
tweet.append(ok[1])
user.append(ok[2])
analyticsl.append(ok[3])
categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl
#print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 

pa=function('Pa.csv')
state.append('Pennsylvania')
popular_category.append(pa[0])
tweet.append(pa[1])
user.append(pa[2])
analyticsl.append(pa[3])
categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl
#print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 

sc=function('Sc.csv')
state.append('South Carolina')
popular_category.append(sc[0])
tweet.append(sc[1])
user.append(sc[2])
analyticsl.append(sc[3])
categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl
#print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 

tn=function('Tn.csv')
state.append('Tennessee')
popular_category.append(tn[0])
tweet.append(tn[1])
user.append(tn[2])
analyticsl.append(tn[3])
categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl
#print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 

tx=function('TX.csv')
state.append('Texas')
popular_category.append(tx[0])
tweet.append(tx[1])
user.append(tx[2])
analyticsl.append(tx[3])
categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl
#print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 

va=function('VA.csv')
state.append('Virginia')
popular_category.append(va[0])
tweet.append(va[1])
user.append(va[2])
analyticsl.append(va[3])
categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl
#print(categories_d)
json_object = json.dumps(categories_d, indent = 4) 

vt=function('Vt.csv')
state.append('Vermont')
popular_category.append(vt[0])
tweet.append(vt[1])
user.append(vt[2])
analyticsl.append(vt[3])
categories_d['state']=state
categories_d['popular_category']=popular_category
categories_d['tweet']=tweet
categories_d['user']=user
categories_d['Analytics']=analyticsl
print(categories_d)
print('...........................................')
json_object = json.dumps(categories_d, indent = 4) 
pd.DataFrame.from_dict(categories_d).to_json('output.json')


print(json_object)
with open('json_data.json', 'w') as outfile:
    outfile.write(json_object)

