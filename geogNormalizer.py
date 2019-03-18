import os
import csv   
import operator
#from geotext import GeoText
#https://simplemaps.com/data/us-cities

from nltk import ngrams
class geoExtract(object):
    def __init__(self):
    
        
        self.isoCode=self.ISO3166() 
        self.isoCountry=self.countries()   
        self.isoCity=self.cities()
        self.mLCountry=self.multiLingualCountry()
        self.mLCity=self.multiLingualCities()     #List of 2 dics
        self.stateCity=self.states()
        self.country=[]
        for c in self.isoCountry:
            self.country.append(self.isoCountry[c])
    
        priors=self.loadPrior()
        self.cCity=priors[0]
        self.cTotal=priors[1]
        self.sCity=priors[2]
        self.sTotal=priors[3]
        self.State=priors[4]
        self.totalS=priors[5]
        self.Country=priors[6]
        self.totalC=priors[7]
        
    
    def ISO3166(self):
        iso={}
        file=open('iso3166.csv','r', encoding="utf-8").read().split('\n')
        for i in range(1,len(file)):
            if len(file[i])>0:
                row=file[i].split(',')
                iso[row[2]]=row[0].lower()
                iso[row[1]]=row[0].lower()
        return(iso)
    def countries(self):
        file=open('countries.txt','r', encoding="utf-8").read().split('\n')
        country={}

        for i in range(1,len(file)):
            if len(file[i])>0:
                row=file[i].split('\t')
                if len(row[1])>0:
                   if row[1]!='-':
                        country[row[1]]=row[3].lower()
        return(country)
    
    def openCity(self,name,s,city,total,type):
        if type=='s':               #FIX
            variable=self.state
        if type=='c':   
            variable=self.country
        c=city
        t=total
        file=open(name+s,'r').read().split('\n')
        for f in file:
            if len(f)>0:
                row=f.split('|')
                if row[0] in variable:
                    row[0]=variable[row[0]]
                if row[0] not in c:
                    c[row[0]]={}
                c[row[0]][row[1]]=int(row[2])
                t=t+int(row[2])
     
        file.close()
        return(c,t)
        
    def openTotal(self,name,s,total,C,type):
        if type=='s':               #FIX
            variable=self.state
        if type=='c':   
            variable=self.country
        t=total
        file=open(name+s,'r').read().split('\n')
        n=C
        for f in file:
            if len(f)>0:
                row=f.split('|')
                if row[0] in variable:
                    row[0]=variable[row[0]]
                n[row[0]]=int(row[1])
                t=t+int(row[1])
                
        file.close()
        return(n,t)
     
        
    def loadPrior(self,s='small'):
        cCity={}
        cTotal=0
        sCity={}
        sTotal=0
        state={}
        totalS=0
        country={}
        totalC=0
        tempOpen=self.openCity('countryScore.',s,cCity,cTotal,'c')       #split acronyms
        cCity=tempOpen[0]
        cTotal=tempOpen[1]
        
        tempOpen=self.openCity('stateScore.',s,sCity,sTotal,'s')
        sCity=tempOpen[0]
        sTotal=tempOpen[1]
        
        tempOpen=self.openTotal('totState.',s,totalS,state,'s')
        state=tempOpen[0]
        totalS=tempOpen[0]
        
        tempOpen=self.openTotal('totCountry.',s,totalC,country,'c')
        country=tempOpen[0]
        totalC=tempOpen[0]
        return(cCity,cTotal,sCity,sTotal,state,totalS,country,totalC)


    '''
    def countries(self):
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
    '''
    
    '''
    def cities(self):
        city={}
        file=open('cities.txt','r', encoding="utf-8").read().split('\n')

        for i in range(1,len(file)):
            if len(file[i])>0:
                row=file[i].split('\t')
                if len(row[1])>0:
                    city[row[1].lower()]=row[0]
        return(city)
    '''   
    
    def cities(self):
        city={}
        file=open('cities.txt','r', encoding="utf-8").read().split('\n')
        
        for i in range(1,len(file)):
            if len(file[i])>0:
                row=file[i].split('\t')
                if len(row[1])>0:
                    if row[1].lower() not in city:
                        city[row[1].lower()]=[]
                    
                    city[row[1].lower()].append(row[0])
        return(city)  
        
        
    def multiLingualCountry(self):
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
    def states(self):
        stateCity={}
        stateName={}
        nameState={}
        cityState={}
        with open('states.csv','r',encoding='utf-8') as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            x=0
            
            for row in readCSV:    
                if x>0:
                    if row[2] not in stateCity:
                        stateCity[row[2]]=[]
                    stateCity[row[2]].append(row[0].lower())
                    
                    if row[0].lower() not in cityState:
                        cityState[row[0].lower()]=[]
                    cityState[row[0].lower()].append(row[2])
                    
                    if row[2] not in stateName:
                        stateName[row[2]]=row[3].lower()
                    if row[3].lower() not in nameState:
                        nameState[row[3].lower()]=row[2]
                    
                x=x+1
        return([stateCity,cityState,stateName,nameState])
        
    def multiLingualCities(self):      #row[1]     #row[19]
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

    def nGrammer(self,gram):
        nGram=[]
        for i in gram:
                nGram.append(' '.join(list(i)))
                
        return(nGram)

    def extract(self,text):
        text=text.strip(' ').strip(',')
        textSpace=text.split(' ')
        textComma=text.split(',')
        
        textBiSpace=self.nGrammer(ngrams(textSpace, 2))
        textBiComma=self.nGrammer(ngrams(textComma, 2))
        
        textTriSpace=self.nGrammer(ngrams(textSpace, 3))
        textTriComma=self.nGrammer(ngrams(textComma, 3))
        
        #textNoSpace=text.replace(' ','')
        #textNoComma=text.replace(',','')
        textList=[textSpace,textComma,textBiSpace,textBiComma,textTriSpace,textTriComma]
        CSC=self.cityStateCountry(textList)
        
        return(self.voting(CSC))
        '''self.isoCode=self.ISO3166() 
        self.isoCountry=self.countries()   
        self.isoCity=self.cities()
        self.mLCountry=self.multiLingualCountry()
        self.mLCity=self.multiLingualCities()     #List of 2 dics
        self.stateCity=self.states()
        self.country=[]
        for c in self.isoCountry:
            self.country.append(self.isoCountry[c])
        '''
    def voting(self,csc):
        cityList=csc[0]
        
        stateList=csc[1]
        
        countryList=csc[2]
        #correction USA=US
                
        city={}
        country={}
        state={}
    
        for c in countryList:
            if c[0].lower()=='united states':
                c[0]='united states of america'
            if c[0].lower() not in country:
                country[c[0].lower()]=0
            country[c[0].lower()]=country[c[0].lower()]+c[1]
            
        for s in stateList:
            if s[0].lower() not in state:
                state[s[0].lower()]=0
            state[s[0].lower()]=state[s[0].lower()]+s[1]
            
        for c in cityList:
            if c[0].lower() not in city:
                city[c[0].lower()]=0
            city[c[0].lower()]=city[c[0].lower()]+c[1]
        
        citySort=sorted(city.items(),key=operator.itemgetter(1),reverse=True)
        candidateCity=""
        candidateState=""
        candidateCountry=""
        if len(citySort)>0:
            if len(citySort)>1:
                if citySort[0][1]!=citySort[1][1]:
                    
                    candidateCity=citySort[0][0]
            else:
                candidateCity=citySort[0][0]
            
            
        stateSort=sorted(state.items(),key=operator.itemgetter(1),reverse=True)    
        if len(stateSort)>0:
            if len(stateSort)>1:
                if stateSort[0][1]!=stateSort[1][1]:
                    
                    candidateState=stateSort[0][0]
            else:
                candidateState=stateSort[0][0]
                
        countrySort=sorted(country.items(),key=operator.itemgetter(1),reverse=True)    
        
        if len(countrySort)>0:
            candidateCountry=countrySort[0][0]
            
        #if candidateCity != "" and self.isoCountry[self.isoCity[candidateCity]] !=  candidateCountry:
        #   candidateCity=""
            
        if candidateCity != "" and candidateState !="" and  candidateCity not in self.stateCity[0][candidateState.upper()]:
            candidateCity=""        

        if candidateCity not in sCity[candidateState]:
            candidateState=""
        if candidateCity not in cCity[candidateCountry]:
            candidateCity=""
        return([candidateCity,candidateState,candidateCountry])
        
        
        
    def cityStateCountry(self,textList):
        city=[]
        state=[]
        country=[]
        for textItem in textList:
            for item in textItem:
                if item in self.isoCode:
                    country.append([self.isoCode[item],3])
                if item in self.country:
                    country.append([item,3])
                if item in self.isoCountry:
                    country.append([self.isoCountry[item],3])    
                if item.lower() in self.mLCountry:
                    #print(item)
                    #print(self.mLCountry[item.lower()])
                    country.append([self.isoCode[self.mLCountry[item.lower()].upper()],3])
                
                
                if item.lower() in self.stateCity[1]:
                    country.append([self.isoCode['USA'],1])
                    for s in self.stateCity[1][item.lower()]:
                        state.append([s,2])
                    city.append([item,3])
                if item.lower() in self.stateCity[3]:
                    country.append([self.isoCode['USA'],2])
                    state.append([self.stateCity[3][item.lower()],3])
                if item in self.stateCity[2]:
                    country.append([self.isoCode['USA'],2])
                    state.append([item,3])
                '''
                if item in self.mLCity[0]:
                    city.append([self.mLCity[0][item],0])
                    country.append([self.mLCity[1][self.mLCity[0][item]],2])
                '''   
                if item.lower() in self.mLCity[1]:
                    city.append([item.lower(),3])
                    country.append([self.mLCity[1][item.lower()],1])
        return([city,state,country])
                    
#States USA

text=open('xx.txt','r',encoding='utf-8').read().split('\n')
G=geoExtract()
P=[]
x=0
for f in text:
    x=x+1
    if len(f)>0:
        row=f.split('\t | \t')
        if len(row)>4:
            location=row[4]
            P.append([G.extract(location),location])
            if x >50:
                break