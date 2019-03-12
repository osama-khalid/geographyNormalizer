text=open('xx.txt','r').read().split('\n')
from nltk import ngrams
for f in text:
    if len(f)>0:
        row=f.split('\t | \t')
        if len(row)>4:
            location=row[4]
            text=location.strip(' ').lower()
            print(text.split(' '))
            bigrams = ngrams(text.split(), 2)
            b=[]
            for i in bigrams:
                b.append(' '.join(list(i)))
            print(b)
            print(location.replace(' ','').lower())
            
            
cities=open('cities.txt','r').read().split('\n')
cityCount={}

for c in cities:
    if len(c)>0:
        row=c.split('\t')
        if len(row[1])>0:
            cityCount[row[1].lower()]=row[0]