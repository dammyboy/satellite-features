from __future__ import division
import re
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer



def removeHTML(text):
    ''' Function adopted based on HTML cleaner used by Eliot Barril
        Link: https://www.kaggle.com/eliotbarr/transfer-learning-on-stack-exchange-tags/word-clouds
        '''
    htmlFilter = re.compile('<.*?>')
    finalText = re.sub(htmlFilter,'', text)
       
    return finalText 

def estimateTFIDF(content):
    vectorizer = CountVectorizer()
    freqMatrix = vectorizer.fit_transform(content)
    
    tfidf = TfidfTransformer(norm = 'l2')
    tfidf.fit(freqMatrix)
    
    return tfidf, freqMatrix

def getTopicText(topic, textDict):
    allText = []
    tags = []
    for d in textDict:
        if d['Area'] == topic:
            allText.append(d['Title'] +' '+ d['Content'])
            tags+=d['Tags']
    return allText, tags