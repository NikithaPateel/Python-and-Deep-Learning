import nltk
#nltk.download()
from bs4 import BeautifulSoup
import requests
from nltk.stem import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk import wordpunct_tokenize,pos_tag,ne_chunk

url = "https://en.wikipedia.org/wiki/Google"
source_code = requests.get(url)
plain_text = source_code.text
parse = BeautifulSoup(plain_text, "html.parser")
p = parse.findAll('p')

f = open("input.txt", "w")

#s = open("stokens.txt","w")

for item in p:
    f.write(str(item.text))

lemmatizer = WordNetLemmatizer()
pstemmer = PorterStemmer()
f = open('input.txt','r')

with open("stokens.txt","w") as s:
    for statement in f:
        stokens = nltk.sent_tokenize(statement)
        for stk in stokens:
            s.write(str("Stentense token//"))
            s.write(str(stk))
            s.write(str("TRIGRAM//"))
            tri = nltk.trigrams(stk.split())
            for t in tri:
                s.write(str(t))
            s.write(str("Name Entity//"))
            s.write(str((ne_chunk(pos_tag(wordpunct_tokenize(stk))))))
        #print("stokens",stokens)

        wtokens = nltk.word_tokenize(statement)
        for wtk in wtokens:
            s.write(str("Word token//"))
            s.write(str(wtk))
            #print(pstemmer.stem(wtk))
            s.write(str("Stemming//"))
            s.write(str(pstemmer.stem(wtk)))
            #print(pstemmer.stem(wtk))
        #print("wtokens", wtokens)

        for w in wtokens:
            #print("Lemmatizer",lemmatizer.lemmatize(w))
            s.write("Lemmatization//")
            s.write(str(lemmatizer.lemmatize(w)))
            print(lemmatizer.lemmatize(w))
        pos = nltk.pos_tag(stokens)
        #print("pos",pos)
        s.write(str("Parts of speech//"))
        s.write(str(pos))






