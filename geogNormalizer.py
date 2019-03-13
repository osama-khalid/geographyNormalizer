import os
import csv   

from nltk import ngrams
def ISO3166():
    iso={}
    file=open('iso3166.csv','r', encoding="utf-8").read().split('\n')
    for i in range(1,len(file)):
        if len(file[i])>0:
            row=file[i].split(',')
            iso[row[2]]=row[0].lower()
            iso[row[1]]=row[0].lower()
    return(iso)

def countries():
    file=open('countries.txt','r', encoding="utf-8").read().split('\n')
    country={}

    for i in range(1,len(file)):
        if len(file[i])>0:
            row=file[i].split('\t')
            if len(row[1])>0:
                if row[0]!='-':
                    country[row[0]]=row[3].lower()
                if row[1]!='-':
                    country[row[1]]=row[3].lower()
    return(country)
def cities():
    city={}
    file=open('cities.txt','r', encoding="utf-8").read().split('\n')
    
    
    

    for i in range(1,len(file)):
        if len(file[i])>0:
            row=file[i].split('\t')
            if len(row[1])>0:
                city[row[1].lower()]=row[0]
    return(city)
def multiLingualCountry():
    mLCountry={}
    subdir=os.listdir('./data/')
    for s in subdir:
        path='./data/'+s+'/country.csv'
        with open(path,'r', encoding="utf-8") as csvfile:   
            readCSV = csv.reader(csvfile, delimiter=',')
            x=0
            for row in readCSV:    
                if x>0:
                    mLCountry[row[1].lower()]=row[0]
                
                x=x+1
        
     
    
    return(mLCountry)
    
def multiLingualCities():      #row[1]     #row[19]
    mLCity={}
    cCountry={}
    with open('allCities.csv','r',encoding='utf-8') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        x=0
        
        for row in readCSV:    
            if x>0:
                cCountry[row[1].lower()]=row[19].lower()
                variants=row[3].split(',')
                if len(variants)>0:
                    for v in variants:
                        mLCity[v.lower()]=row[1].lower()
                    
                
            x=x+1
    return([mLCity,cCountry])
isoCode=ISO3166() 

isoCountry=countries()   
isoCity=cities()
mLCountry=multiLingualCountry()
mLCity=multiLingualCities()     #List of 2 dics

country=[]
for c in isoCountry:
    country.append(isoCountry[c])

#States USA

text=open('xx.txt','r',encoding='utf-8').read().split('\n')

for f in text:
    if len(f)>0:
        row=f.split('\t | \t')
        if len(row)>4:
            location=row[4]
            text=location.strip(' ').lower()
            #print(text.split(' '))
            t=text.split(' ')
            flag=0
            for byte in t:
                    
                    
                if byte in country:
                    print(text,mLCountry[byte],byte)
                    flag=1
                
                if byte in mLCity[0] and flag==0:
                    print(text,mLCity[0][byte],byte)
                    flag=1
                
            
            t=text.split(',')
            
            for byte in t:
            
            
                if byte in country and flag==0:
                    print(text,mLCountry[byte],byte)
                    flag=1
            
                if byte in mLCity[0] and flag==0:
                    print(text,mLCity[0][byte],byte)
                    flag=1
            if flag==0:
                print('-------------'+text)
            '''
            if flag==0:
                print('------'+text)
            bigrams = ngrams(text.split(), 2)
            b=[]
            for i in bigrams:
                b.append(' '.join(list(i)))
                if ' '.join(list(i)) in countries:
                    print('-------')
            print(b)
            print(location.replace(' ','').lower())
            if location.replace(' ','').lower() in countries:
                print('-------')
            '''