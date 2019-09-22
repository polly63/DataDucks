import nltk
import pandas as pd
df = pd.read_csv('Rogers.csv')

# Data Cleaning
comments = []
i = 0
while i < len(df['Avatar']):
    if df['Avatar'][i].isdigit():
        comments.append(df['Avatar'][i-1])
    elif df['Avatar'][i] == '•Reply•Share ›' and df['Avatar'][i-1].isdigit() is False:
        comments.append(df['Avatar'][i-1])
    i += 1

# Word tokenize and POS tag on each comment
word_list = []
for item in comments:
    token_list = nltk.word_tokenize(item)
    word_list.append(nltk.pos_tag(token_list))

# choose all the adjectives, nouns and verbs
verb_list = []
noun_list = []
adjective_list = []
for item in word_list:
    for word in item:
        if word[1] == 'NN' or word[1] == 'NNS' or word[1] == 'NNP' or word[1] == 'NNPS':
            noun_list.append(word[0])
        elif word[1] == 'JJ' or word[1] == 'JJR' or word[1] =='JJS':
            adjective_list.append(word[0])
        elif word[1] == 'VB' or word[1] == 'VBD' or word[1] == 'VBG' or word[1] == 'VBN' or word[1] == 'VBP'\
                or word[1] == 'VBZ':
            verb_list.append(word[0])

# Count the frequency of each adjective, nouns and verbs
verb = {}
noun = {}
adj = {}
for item in noun_list:
    noun[item] = noun_list.count(item)
for item in verb_list:
    verb[item] = verb_list.count(item)
for item in adjective_list:
    adj[item] = adjective_list.count(item)

# Convert data frame to csv
df1 = pd.DataFrame.from_dict(verb, orient='index')
df1.to_csv("verb.csv")
df1 = pd.read_csv("verb.csv")

df2 = pd.DataFrame.from_dict(noun, orient='index')
df2.to_csv("noun.csv")
df2 = pd.read_csv("noun.csv")

df3 = pd.DataFrame.from_dict(adj, orient='index')
df3.to_csv("adj.csv")
df3 = pd.read_csv("adj.csv")