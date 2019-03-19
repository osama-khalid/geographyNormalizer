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

        self.stateCity=self.states()
        self.country=[]
        for c in self.isoCountry:
            self.country.append(self.isoCountry[c])
    
        self.revCountry={}
        for n in self.isoCountry:
            self.revCountry[self.isoCountry[n]]=n
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
                    if row[0]!='-':
                        country[row[0]]=row[3].lower()
                    if row[1]!='-':
                        country[row[1]]=row[3].lower()
        return(country)
    def cities(self):
        city={}
        file=open('cities.txt','r', encoding="utf-8").read().split('\n')

        for i in range(1,len(file)):
            if len(file[i])>0:
                row=file[i].split('\t')
                if len(row[1])>0:
                    city[row[1].lower()]=row[0]
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
            
        if candidateCity !="" and candidateState !="" and candidateCity not in self.stateCity[0][candidateState.upper()]:
            candidateState=""            
        
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
                if item.lower() in self.mLCountry and self.mLCountry[item.lower()].upper() in self.isoCode:
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
                
                if item.lower() in self.mLCity[1]:
                    city.append([item.lower(),3])
                    country.append([self.mLCity[1][item.lower()],1])
                '''   
                
                
        return([city,state,country])
                    
#States USA

path='xx.txt'
csv_file=open('xx_updated1','w')
writer=csv.writer(csv_file,delimiter='|', lineterminator='\n')
G=geoExtract()
P=[]
x=0
with open(path,'r', encoding="utf-8") as csvfile:   
    readCSV = csv.reader(csvfile, delimiter='|')
    for row in readCSV: 
        x=x+1
        if len(row)>4:
            city=""
            state=""
            country=""
                
            location=row[4].replace('\t',' ')
            output=G.extract(location)
            city=output[0]
            state=output[1]
            country=output[2]
            row.append(city)
            row.append(state)
            row.append(country)
            writer.writerow(row)
       