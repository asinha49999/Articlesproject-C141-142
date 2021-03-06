# -*- coding: utf-8 -*-
"""MovieRecommendationproject(C138,139,&140).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bNOfFWnhHenoMPWmMQW1uBhkLx2jnuGc
"""
import pandas as pd
shared = pd.read_csv("shared_articles.csv")
shared.head()

interaction = pd.read_csv("users_interactions.csv")
interaction.head()

interaction.columns = ["timestamp","eventType","contentId","personId","sessionId","userAgent","userRegion","userCountry"]
shared = shared.merge(interaction,on="contentId")

shared.head()

#print(shared.iloc[72679])

#print(shared["eventType_x"])

check = shared.loc[shared['eventType_x']=="CONTENT SHARED"]

#print(check["eventType_y"][1000])

from collections import Counter
total = Counter(check["title"])
#print(total)
def most_often():
  common = total.most_common(10)
  return common

total2 = []
for i in total:
  total2.append(i.lower())

# for i in total:
#    print(total[i])

# for index,i in enumerate(common):
#   x = i.lower()
#   shared["title"][index] = x
# shared.head(3)
# def convert(x):
#   return x.lower()
# common = common.apply(convert)
# shared.head(4)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(stop_words="english")
related = cv.fit_transform(total)
#print(related)

from sklearn.metrics.pairwise import cosine_similarity
cssim = cosine_similarity(related,related)
#print(cssim)

def get_titles(index):
  # print(cssim[indexnum])
  simscore = list(enumerate(cssim[index]))
  # print(simscore)
  simscore = sorted(simscore,key=lambda x:x[1],reverse=True)
  simscore.pop(0)
  #print(simscore)
  articlenames = []
  for i in simscore[0:10]:
    #print(total2[i[0]])
    articlenames.append(total2[i[0]])
  return articlenames


get_titles(3)