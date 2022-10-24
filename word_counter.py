import requests, nltk
from bs4 import BeautifulSoup
from collections import Counter
r = requests.get('https://www.gutenberg.org/files/16/16-h/16-h.htm')
r.encoding = ('utf-8')
html = r.text
soup = BeautifulSoup(html)
text = soup.get_text()
tokenizer = nltk.tokenize.RegexpTokenizer('\w+')
tokens = tokenizer.tokenize(text)
words = []
for word in tokens:
    words.append(word.lower())
stopwords = nltk.corpus.stopwords.words('english')
words_ns = [word for word in words if word not in stopwords]
count = Counter(words_ns)
top_ten = count.most_common(10)
print(top_ten)
