import pycrfsuite
import unicodedata
#import streamlit as st
from PIL import Image
def checkdigit(char):
    digits = [u'۱',u'۲',u'۳',u'۴',u'۵',u'۶',u'۷',u'۸',u'۹',u'۰']
    if char in digits:
        return "true"
    return "false"
    
def isnonjoiner(char):
    non_joiners = [u'ا', u'د', u'ڈ', u'ز', u'ذ', u'ر', u'ڑ', u'ژ', u'و', u'ے']
    if char in non_joiners:
        return "true"
    return "false"
    
def create_char_features(sentence, i):
    features = [
        'bias',
        'char=' + sentence[i][0],
        'char.isdigit=' + checkdigit(sentence[i][0]),
        'char.isnonjoiner=' + isnonjoiner(sentence[i][0]),
        'char.category=' + unicodedata.category(sentence[i][0]),
        'char.direction=' + unicodedata.bidirectional(sentence[i][0]),
    ]
    
    if i >= 1:
        features.extend([
            'char-1=' + sentence[i-1][0],
            'char-1:0=' + sentence[i-1][0] + sentence[i][0],
        ])
    else:
        features.append("BOS")
        
    if i >= 2:
        features.extend([
            'char-2=' + sentence[i-2][0],
            'char-2:0=' + sentence[i-2][0] + sentence[i-1][0] + sentence[i][0],
            'char-2:-1=' + sentence[i-2][0] + sentence[i-1][0],
        ])
        
    if i >= 3:
        features.extend([
            'char-3:0=' + sentence[i-3][0] + sentence[i-2][0] + sentence[i-1][0] + sentence[i][0],
            'char-3:-1=' + sentence[i-3][0] + sentence[i-2][0] + sentence[i-1][0],
        ])
        
        
    if i + 1 < len(sentence):
        features.extend([
            'char+1=' + sentence[i+1][0],
            'char:+1=' + sentence[i][0] + sentence[i+1][0],
        ])
    else:
        features.append("EOS")
        
    if i + 2 < len(sentence):
        features.extend([
            'char+2=' + sentence[i+2][0],
            'char:+2=' + sentence[i][0] + sentence[i+1][0] + sentence[i+2][0],
            'char+1:+2=' + sentence[i+1][0] + sentence[i+2][0],
        ])
        
    if i + 3 < len(sentence):
        features.extend([
            'char:+3=' + sentence[i][0] + sentence[i+1][0] + sentence[i+2][0]+ sentence[i+3][0],
            'char+1:+3=' + sentence[i+1][0] + sentence[i+2][0] + sentence[i+3][0],
        ])
    
    return features

def create_sentence_features(prepared_sentence):
    return [create_char_features(prepared_sentence, i) for i in range(len(prepared_sentence))]

def create_sentence_labels(prepared_sentence):
    return [str(part[1]) for part in prepared_sentence]
tagger = pycrfsuite.Tagger()
tagger.open('./Model/urdu-word-segmentation.crfsuite')

def segment_sentence(sentence):
    sentence = sentence.replace(" ", "")
    sentence = sentence.replace(u"\u200C", "") 
    prediction = tagger.tag(create_sentence_features(sentence))
    print (prediction)
    complete = ""
    for i, p in enumerate(prediction):
        if p == "1":
            complete += " " + sentence[i]
        elif p == "2":
            complete += u"\u200C" + sentence[i]
        else:
            complete += sentence[i]
    return complete
Input_File=open("./no_space_v2.ur",'r')
output_File=open("./text_output/_v2_old_model.txt",'x')
content=Input_File.readlines()
for lines in content:
	output=segment_sentence(lines)
	output_File.write(output)
Input_File.close()
output_File.close()
	


	
