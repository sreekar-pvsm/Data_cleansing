#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 13:24:54 2020

@author: psreekar
"""
from __future__ import print_function
import pandas as pd

import re
import sys
from optparse import OptionParser
from langdetect import detect

def dataframe(file):
    df = pd.DataFrame(columns = ['subject','Description','ticket_id','agent_id'])
    f = []
    fileHandle = open(file, 'r')
    try:
        for line in fileHandle:
            fields = line.split('|')
            f.append(fields)
           
        fileHandle.close()
    except:
        pass
    i=0
    for field in f:
        df.loc[i] = [field[0],field[1],field[-2],field[-1]]
        i=i+1
    df =df.dropna(axis=0, how='any')
    return df

def verify_args(options, parser):
    if not all([options.input, options.field, options.output]):
        parser.print_help()
        sys.exit(10)


def fetch_options():
    """Fetch the script options from the command line"""
    parser = OptionParser()
    parser.add_option("-f", "--field", dest="field", type="string",
                      help="Column to anonymize")
    parser.add_option("-i", "--input", dest="input", type="string",
                      help="Input CSV file")
    parser.add_option("-o", "--output", dest="output", type="string",
                      help="Output CSV file")
    (options, args) = parser.parse_args()
    if not options.output:
        options.output = options.input
    verify_args(options, parser)
    return (options, args)


def valid_str_data(data):
    if isinstance(data, str) and len(data) > 0:
        return True
    return False


def anonymized(data):
    if not valid_str_data(data):
        return data

    number_patterns = re.findall(r'\d\d+', data)
    for p in number_patterns:
        data = data.replace(p, 'X' * len(p))

    email_patterns = re.findall(r'[\w\.-]+@[\w\.-]+', data)
    for p in email_patterns:
        data = data.replace(p, 'X' * len(p))
        
    return data


def anonymize_data(df, field):
    for index, row in df.iterrows():
        df.loc[index, field] = anonymized(row[field])
    return df



 



def lang_detect(data):
    lis = []
    for desc in data['Description']:
        if desc is not None:
            l = detect(desc)
            lis.append(l)
        else:
            lis.append('none')
    data['language'] = lis
    
    li = []
    i= 0
    for da in data['language']:
        if da != 'en':
            li.append(i)
        i = i+1
    data = data.drop(li)
    return data

data = dataframe('/Users/psreekar/Desktop/sentiment data /2020-06-15+16_21_09+-+email_source.csv12')
fields = ['subject','Description']

for field in fields:
    field = field.strip()
    df = anonymize_data(data, field)
#df = lang_detect(df)
    
df.to_csv('/Users/psreekar/Desktop/sentiment data /Data_8.csv', index=False)


















from textblob import TextBlob

d = pd.read_csv('/Users/psreekar/Desktop/sentiment data /Data_2.csv')
Blob = []
list1 = data['Description'].tolist()
for text in list1:
    blob = TextBlob(str(text))
    temp = blob.noun_phrases
    print(temp)
#    if type(temp).__name__ == 'float':
#        pass
#    else:
#        Blob.extend(text)
    try:
        Blob.extend(temp)
    except:
        pass
    
def dta(data):
    from langdetect import detect
    list1 = data['Description'].tolist()
    L = []
    for text in list1:
        try:
            lang = detect(str(text))
            L.append(lang)
        except:
            L.append('na')
            pass
    data['Language']= L
    
    data_f = data[data['subject'] != 'Transaction Response']
    data_f1 =  data_f[data_f['Language'] == 'en']
    d = data_f1.sample(n=20000)
    d.to_csv('/Users/psreekar/Desktop/sentiment data /Data.csv', index=False)

d = d.replace(Blob,'X'*7)
d = d.sample(n=20000)





import pandas as pd


data1 = pd.read_csv('/Users/psreekar/Desktop/sentiment data /Data_1.csv')
data2 = pd.read_csv('/Users/psreekar/Desktop/sentiment data /Data_2.csv')
data3 = pd.read_csv('/Users/psreekar/Desktop/sentiment data /Data_3.csv')
data4 = pd.read_csv('/Users/psreekar/Desktop/sentiment data /Data_4.csv')
data5 = pd.read_csv('/Users/psreekar/Desktop/sentiment data /Data_5.csv')
data6 = pd.read_csv('/Users/psreekar/Desktop/sentiment data /Data_6.csv')
data7 = pd.read_csv('/Users/psreekar/Desktop/sentiment data /Data_7.csv')
data8 = pd.read_csv('/Users/psreekar/Desktop/sentiment data /Data_8.csv')

frames = [data1,data2,data3,data4,data5,data6,data7,data8]
Data = pd.concat(frames)


D = pd.read_csv('/Users/psreekar/Desktop/sentiment data /Data.csv')
