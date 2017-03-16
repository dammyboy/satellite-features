from __future__ import division
import re


def removeHTML(text):
    ''' Function adopted based on HTML cleaner used by Eliot Barril
        Link: https://www.kaggle.com/eliotbarr/transfer-learning-on-stack-exchange-tags/word-clouds
        '''
    htmlFilter = re.compile('<.*?>')
    finalText = re.sub(htmlFilter,'', text)
       
    return finalText 