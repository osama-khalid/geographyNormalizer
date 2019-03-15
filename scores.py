import csv

from nltk import ngrams
scores={}
canon=[]
flp=[]
pairs={}
file=open('pairCity.psv','r').read().split('\n')
for f in file:
    if len(f)>0:
        row=f.split('|')
        if len(row[1])==2:
            flp.append(row[1])
        else:
            canon.append(row[1])
        
        if row[1] not in pairs:
            pairs[row[1]]={}
        pairs[row[1]][row[0]]=0

flp=list(set(flp))
canon=list(set(canon))
path="pol.csv_2016-1"
text=22
def nGrammer(gram):
    nGram=[]
    for i in gram:
            nGram.append(' '.join(list(i)))
    return(nGram)


with open(path,'r', encoding="utf-8") as csvfile:   
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:    
        #print(datetime.fromtimestamp(int(row[dateStamp])))
        
        #if c <100:
        content=row[text].replace(',',' ').replace('.',' ').lower()
        
        contentSpace=content.split(' ')
        contentComma=content.split(',')
        
        contentBiSpace=nGrammer(ngrams(contentSpace, 2))
        contentBiComma=nGrammer(ngrams(contentComma, 2))
        
        contentTriSpace=nGrammer(ngrams(contentSpace, 3))
        contentTriComma=nGrammer(ngrams(contentComma, 3))


        updatedCanon=list(set(list(set(canon).intersection(set(content)))+list(set(canon).intersection(set(contentSpace)))+list(set(canon).intersection(set(contentComma)))+list(set(canon).intersection(set(contentBiSpace)))+list(set(canon).intersection(set(contentBiComma)))+list(set(canon).intersection(set(contentTriSpace)))+list(set(canon).intersection(set(contentTriComma)))))
        
        for c in updatedCanon:
            if len(c)>0:
                newCanon=list(pairs[c].keys())
                cityCanon=list(set(list(set(newCanon).intersection(set(content)))+list(set(newCanon).intersection(set(contentSpace)))+list(set(newCanon).intersection(set(contentComma)))+list(set(newCanon).intersection(set(contentBiSpace)))+list(set(newCanon).intersection(set(contentBiComma)))+list(set(newCanon).intersection(set(contentTriSpace)))+list(set(newCanon).intersection(set(contentTriComma)))))
                for k in cityCanon:
                    if len(k)>0:
                        pairs[c][k]=pairs[c][k]+1
        
        content1=row[text].replace(',',' ').replace('.',' ')
        
        contentSpace1=content.split(' ')
        contentComma1=content.split(',')
        
        contentBiSpace1=nGrammer(ngrams(contentSpace, 2))
        contentBiComma1=nGrammer(ngrams(contentComma, 2))
        
        contentTriSpace1=nGrammer(ngrams(contentSpace, 3))
        contentTriComma1=nGrammer(ngrams(contentComma, 3))
        
        updatedflp=list(set(list(set(flp).intersection(set(content1)))+list(set(flp).intersection(set(contentSpace1)))+list(set(flp).intersection(set(contentComma1)))+list(set(flp).intersection(set(contentBiSpace1)))+list(set(flp).intersection(set(contentBiComma1)))+list(set(flp).intersection(set(contentTriSpace1)))+list(set(flp).intersection(set(contentTriComma1)))))
        for c in updatedflp:
            if len(c)>0:
                newCanon=list(pairs[c].keys())
                cityCanon=list(set(list(set(newCanon).intersection(set(content)))+list(set(newCanon).intersection(set(contentSpace)))+list(set(newCanon).intersection(set(contentComma)))+list(set(newCanon).intersection(set(contentBiSpace)))+list(set(newCanon).intersection(set(contentBiComma)))+list(set(newCanon).intersection(set(contentTriSpace)))+list(set(newCanon).intersection(set(contentTriComma)))))
                for k in cityCanon:
                    if len(k)>0:
                        pairs[c][k]=pairs[c][k]+1
                        
            
file=open('countryScore.psv1','w')
for c in pairs:
    for k in pairs[c]:
        file.write(c+'|'+k+'|'+str(pairs[c][k])+'\n')
file.close()


import csv
scores={}
canon=[]
flp=[]
pairs={}
file=open('pairState.psv','r').read().split('\n')
for f in file:
    if len(f)>0:
        row=f.split('|')
        if len(row[1])==2:
            flp.append(row[1])
        else:
            canon.append(row[1])
        
        if row[1] not in pairs:
            pairs[row[1]]={}
        pairs[row[1]][row[0]]=0

flp=list(set(flp))
canon=list(set(canon))
path="pol.csv_2016-1"
text=22



with open(path,'r', encoding="utf-8") as csvfile:   
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:    
        #print(datetime.fromtimestamp(int(row[dateStamp])))
        content=row[text].replace(',',' ').replace('.',' ').lower()
        
        contentSpace=content.split(' ')
        contentComma=content.split(',')
        
        contentBiSpace=nGrammer(ngrams(contentSpace, 2))
        contentBiComma=nGrammer(ngrams(contentComma, 2))
        
        contentTriSpace=nGrammer(ngrams(contentSpace, 3))
        contentTriComma=nGrammer(ngrams(contentComma, 3))


        updatedCanon=list(set(list(set(canon).intersection(set(content)))+list(set(canon).intersection(set(contentSpace)))+list(set(canon).intersection(set(contentComma)))+list(set(canon).intersection(set(contentBiSpace)))+list(set(canon).intersection(set(contentBiComma)))+list(set(canon).intersection(set(contentTriSpace)))+list(set(canon).intersection(set(contentTriComma)))))
        
        for c in updatedCanon:
            if len(c)>0:
                newCanon=list(pairs[c].keys())
                cityCanon=list(set(list(set(newCanon).intersection(set(content)))+list(set(newCanon).intersection(set(contentSpace)))+list(set(newCanon).intersection(set(contentComma)))+list(set(newCanon).intersection(set(contentBiSpace)))+list(set(newCanon).intersection(set(contentBiComma)))+list(set(newCanon).intersection(set(contentTriSpace)))+list(set(newCanon).intersection(set(contentTriComma)))))
                for k in cityCanon:
                    if len(k)>0:
                        pairs[c][k]=pairs[c][k]+1
        
        content1=row[text].replace(',',' ').replace('.',' ')
        
        contentSpace1=content.split(' ')
        contentComma1=content.split(',')
        
        contentBiSpace1=nGrammer(ngrams(contentSpace, 2))
        contentBiComma1=nGrammer(ngrams(contentComma, 2))
        
        contentTriSpace1=nGrammer(ngrams(contentSpace, 3))
        contentTriComma1=nGrammer(ngrams(contentComma, 3))
        
        updatedflp=list(set(list(set(flp).intersection(set(content1)))+list(set(flp).intersection(set(contentSpace1)))+list(set(flp).intersection(set(contentComma1)))+list(set(flp).intersection(set(contentBiSpace1)))+list(set(flp).intersection(set(contentBiComma1)))+list(set(flp).intersection(set(contentTriSpace1)))+list(set(flp).intersection(set(contentTriComma1)))))
        for c in updatedflp:
            if len(c)>0:
                newCanon=list(pairs[c].keys())
                cityCanon=list(set(list(set(newCanon).intersection(set(content)))+list(set(newCanon).intersection(set(contentSpace)))+list(set(newCanon).intersection(set(contentComma)))+list(set(newCanon).intersection(set(contentBiSpace)))+list(set(newCanon).intersection(set(contentBiComma)))+list(set(newCanon).intersection(set(contentTriSpace)))+list(set(newCanon).intersection(set(contentTriComma)))))
                for k in cityCanon:
                    if len(k)>0:
                        pairs[c][k]=pairs[c][k]+1
            
file=open('countryScore.psv2','w')
for c in pairs:
    for k in pairs[c]:
        file.write(c+'|'+k+'|'+str(pairs[c][k])+'\n')
file.close()