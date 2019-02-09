from bs4 import BeautifulSoup
import requests

l = []

url = "https://en.wikipedia.org/wiki/Deep_learning"
source_code = requests.get(url)
plain_text = source_code.text
parse = BeautifulSoup(plain_text, "html.parser")
f = open("wikifile.txt", "w")

print("The title is ", parse.title.string)

for link in parse.findAll('a'):
    l.append(link.get('href'))
    for i in l:
        f.write(str(i) + "\n")



