import csv
import collections
from nltk import ngrams
scoresC={}
canonC=[]
flpC=[]
pairsC={}

X=0
TotalC={}
TotalS={}

file=open('pairCity.psv','r', encoding="utf-8").read().split('\n')
for f in file:
    if len(f)>0:
        row=f.split('|')
        if len(row[1])==2:
            flpC.append(row[1])
        else:
            canonC.append(row[1])
        
        if row[1] not in pairsC:
            pairsC[row[1]]={}
        pairsC[row[1]][row[0]]=0
        
        TotalC[row[1]]=0
        


scoresS={}
canonS=[]
flpS=[]
pairsS={}
file=open('pairState.psv','r', encoding="utf-8").read().split('\n')
for f in file:
    if len(f)>0:
        row=f.split('|')
        if len(row[1])==2:
            flpS.append(row[1])
        else:
            canonS.append(row[1])
        
        if row[1] not in pairsS:
            pairsS[row[1]]={}
        pairsS[row[1]][row[0]]=0
        TotalS[row[1]]=0
        
flpS=list(set(flpS))
canonS=list(set(canonS))
flpC=list(set(flpC))
canonC=list(set(canonC))


path="pol.csv_2016-1"
text=22
def nGrammer(gram):
    
    nGram=[]
    try:
        for i in gram:
        
            nGram.append(' '.join(list(i)))
        return(nGram)
    except:
        return(nGram)
text=22

with open(path,'r', encoding="utf-8") as csvfile:   
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:    
        X=X+1
        if X%5000==0:
            print(X)
        if X>900000:
            break
            
        #print(datetime.fromtimestamp(int(row[dateStamp])))
        
        #if c <100:
        content=row[text].replace(',',' ').replace('.',' ').lower()
        
        contentSpace=content.split(' ')
        contentComma=content.split(',')
        
        contentBiSpace=nGrammer(ngrams(contentSpace, 2))
        contentBiComma=nGrammer(ngrams(contentComma, 2))
        
        contentTriSpace=nGrammer(ngrams(contentSpace, 3))
        
        contentTriComma=nGrammer(ngrams(contentComma, 3))


        updatedCanon=list(set(list(set(canonC).intersection(set(content)))+list(set(canonC).intersection(set(contentSpace)))+list(set(canonC).intersection(set(contentComma)))+list(set(canonC).intersection(set(contentBiSpace)))+list(set(canonC).intersection(set(contentBiComma)))+list(set(canonC).intersection(set(contentTriSpace)))+list(set(canonC).intersection(set(contentTriComma)))))
        
        for c in updatedCanon:
            if len(c)>0:
                TotalC[c]=TotalC[c]+1
                newCanon=list(pairsC[c].keys())
                cityCanon=list(set(list(set(newCanon).intersection(set(content)))+list(set(newCanon).intersection(set(contentSpace)))+list(set(newCanon).intersection(set(contentComma)))+list(set(newCanon).intersection(set(contentBiSpace)))+list(set(newCanon).intersection(set(contentBiComma)))+list(set(newCanon).intersection(set(contentTriSpace)))+list(set(newCanon).intersection(set(contentTriComma)))))
                for k in cityCanon:
                    if len(k)>0:
                        pairsC[c][k]=pairsC[c][k]+1
                        
        
        content1=row[text].replace(',',' ').replace('.',' ')
        
        contentSpace1=content.split(' ')
        contentComma1=content.split(',')
        
        contentBiSpace1=nGrammer(ngrams(contentSpace, 2))
        contentBiComma1=nGrammer(ngrams(contentComma, 2))
        
        contentTriSpace1=nGrammer(ngrams(contentSpace, 3))
        contentTriComma1=nGrammer(ngrams(contentComma, 3))
        
        updatedflp=list(set(list(set(flpC).intersection(set(content1)))+list(set(flpC).intersection(set(contentSpace1)))+list(set(flpC).intersection(set(contentComma1)))+list(set(flpC).intersection(set(contentBiSpace1)))+list(set(flpC).intersection(set(contentBiComma1)))+list(set(flpC).intersection(set(contentTriSpace1)))+list(set(flpC).intersection(set(contentTriComma1)))))
        for c in updatedflp:
            if len(c)>0:
                TotalC[c]=TotalC[c]+1
                newCanon=list(pairsC[c].keys())
                cityCanon=list(set(list(set(newCanon).intersection(set(content)))+list(set(newCanon).intersection(set(contentSpace)))+list(set(newCanon).intersection(set(contentComma)))+list(set(newCanon).intersection(set(contentBiSpace)))+list(set(newCanon).intersection(set(contentBiComma)))+list(set(newCanon).intersection(set(contentTriSpace)))+list(set(newCanon).intersection(set(contentTriComma)))))
                for k in cityCanon:
                    if len(k)>0:
                        pairsC[c][k]=pairsC[c][k]+1
                        
        content=row[text].replace(',',' ').replace('.',' ').lower()
        
        contentSpace=content.split(' ')
        contentComma=content.split(',')
        
        contentBiSpace=nGrammer(ngrams(contentSpace, 2))
        contentBiComma=nGrammer(ngrams(contentComma, 2))
        
        contentTriSpace=nGrammer(ngrams(contentSpace, 3))
        contentTriComma=nGrammer(ngrams(contentComma, 3))


        updatedCanon=list(set(list(set(canonS).intersection(set(content)))+list(set(canonS).intersection(set(contentSpace)))+list(set(canonS).intersection(set(contentComma)))+list(set(canonS).intersection(set(contentBiSpace)))+list(set(canonS).intersection(set(contentBiComma)))+list(set(canonS).intersection(set(contentTriSpace)))+list(set(canonS).intersection(set(contentTriComma)))))
        
        for c in updatedCanon:
            if len(c)>0:
                TotalS[c]=TotalS[c]+1
                newCanon=list(pairsS[c].keys())
                cityCanon=list(set(list(set(newCanon).intersection(set(content)))+list(set(newCanon).intersection(set(contentSpace)))+list(set(newCanon).intersection(set(contentComma)))+list(set(newCanon).intersection(set(contentBiSpace)))+list(set(newCanon).intersection(set(contentBiComma)))+list(set(newCanon).intersection(set(contentTriSpace)))+list(set(newCanon).intersection(set(contentTriComma)))))
                for k in cityCanon:
                    if len(k)>0:
                        pairsS[c][k]=pairsS[c][k]+1
        
        content1=row[text].replace(',',' ').replace('.',' ')
        
        contentSpace1=content.split(' ')
        contentComma1=content.split(',')
        
        contentBiSpace1=nGrammer(ngrams(contentSpace, 2))
        contentBiComma1=nGrammer(ngrams(contentComma, 2))
        
        contentTriSpace1=nGrammer(ngrams(contentSpace, 3))
        contentTriComma1=nGrammer(ngrams(contentComma, 3))
        
        updatedflp=list(set(list(set(flpS).intersection(set(content1)))+list(set(flpS).intersection(set(contentSpace1)))+list(set(flpS).intersection(set(contentComma1)))+list(set(flpS).intersection(set(contentBiSpace1)))+list(set(flpS).intersection(set(contentBiComma1)))+list(set(flpS).intersection(set(contentTriSpace1)))+list(set(flpS).intersection(set(contentTriComma1)))))
        for c in updatedflp:
            TotalS[c]=TotalS[c]+1
            if len(c)>0:
                newCanon=list(pairsS[c].keys())
                cityCanon=list(set(list(set(newCanon).intersection(set(content)))+list(set(newCanon).intersection(set(contentSpace)))+list(set(newCanon).intersection(set(contentComma)))+list(set(newCanon).intersection(set(contentBiSpace)))+list(set(newCanon).intersection(set(contentBiComma)))+list(set(newCanon).intersection(set(contentTriSpace)))+list(set(newCanon).intersection(set(contentTriComma)))))
                for k in cityCanon:
                    if len(k)>0:
                        pairsS[c][k]=pairsS[c][k]+1
                                    
            
file=open('countryScore.psv1','w', encoding="utf-8")
for c in pairsC:
    for k in pairsC[c]:
        file.write(c+'|'+k+'|'+str(pairsC[c][k])+'\n')
file.close()


file=open('stateScore.psv1','w', encoding="utf-8")
for c in pairsS:
    for k in pairsS[c]:
        file.write(c+'|'+k+'|'+str(pairsS[c][k])+'\n')
file.close()

file=open('totCountry.psv1','w', encoding="utf-8")
for c in TotalC:
    file.write(c+'|'+str(TotalC[c])+'\n')
    
file.close()

file=open('totState.psv1','w', encoding="utf-8")
for c in TotalS:
    file.write(c+'|'+str(TotalS[c])+'\n')    
    
file.close()    