import os
import csv   
import operator
import math
from wordfreq import word_frequency as wf 
import csv 

from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="textExtract_Uiowa")

#from geotext import GeoText
#https://simplemaps.com/data/us-cities

from nltk import ngrams
class geoExtract(object):
    def __init__(self):
        loadState=self.stateLoad()                    #
        self.stateDeAbbr=loadState[0]                    #FL-Florida
        self.stateAbbr=loadState[1]                        #Florida=FL
        self.cityInState=loadState[2]                      #Miami->Florida,Ohio
        self.stateHasCity=loadState[3]                    #Florida->Miami,Tellehesse
    
        loadCountry=self.iso3166()
        self.iso3DeAbbr=loadCountry[0]                   #AF->Afghanistan
        self.iso2DeAbbr=loadCountry[1]                   #AF->Afghanistan
        self.isoAbbr=loadCountry[2]                        #Afghanistan ->AF
        
        loadCountry=self.fipCountry()
        self.fipDeAbbr=loadCountry[1]                   #AF->Afghanistan
        self.fipAbbr=loadCountry[0]                        #Afghanistan ->AF
        
        loadCity=self.countryLoad()
        self.cityInFIP=loadCity[0]                          #Lahore->PK
        self.FIPhasCity=loadCity[1]                         #PK->Lahore
        
        self.MLCountry=self.multiLingualCountry()               #Afghani - >AF
        self.priors=self.loadPrior()								#PriorLoad	
    
        open=self.loadPrior()
        self.cityNCountry=open[0]
        self.totalCityNCountry=open[1]
        self.cityNState=open[2]
        self.totalCityNState=open[3]
        self.aggState=open[4]
        self.aggCountry=open[5]
        self.totalState=open[6]
        self.totalCountry=open[7]
        
        
    def fipCountry(self):
        file=open('countries.txt','r', encoding="utf-8").read().split('\n')
        flpAbbr={}              #United Kingdom ->UK
        flpDeAbbr={}          #UK->United Kingdom
        for i in range(1,len(file)):
            if len(file[i])>0:
                row=file[i].split('\t')
                if len(row[1])>0:
                   if row[1]!='-':
                        
                        flpAbbr[row[3].lower()]=row[1]
                        
                        
                        flpDeAbbr[row[1]]=row[3].lower()
                            
                            
        return(flpAbbr,flpDeAbbr)
        
    def countryLoad(self):
        cityInFIP={}
        FIPhasCity={}
        
        file=open('cities.txt','r',encoding='utf-8').read().split('\n')
        
        for i in range(1,len(file)):
            if len(file[i])>0:
                row=file[i].split('\t')
                if row[1].lower() not in cityInFIP:
                    cityInFIP[row[1].lower()]=[]
                cityInFIP[row[1].lower()].append(row[0])
                
                if row[0] not in FIPhasCity:
                    FIPhasCity[row[0]]=[]
                FIPhasCity[row[0]].append(row[1].lower())
                
        return(cityInFIP,FIPhasCity)
                
                        
    


    def iso3166(self):
        iso2DeAbbr={}             #AF -> Afghanistan,AFG->Afghanistan
        
        
        iso3DeAbbr={}             #AF -> Afghanistan,AFG->Afghanistan
        isoAbbr={}             #Afghanistan ->AF,AFG
        
        file=open('iso3166.csv','r', encoding="utf-8").read().split('\n')
        iso3to2={}
        for i in range(1,len(file)):
            if len(file[i])>0:
                row=file[i].split(',')
                
                
                iso2DeAbbr[row[2]]=row[0].lower()
                iso3DeAbbr[row[1]]=row[0].lower()
                
                
                    
                
                isoAbbr[row[0].lower()]=row[1]
            
        return(iso2DeAbbr,iso3DeAbbr,isoAbbr)
        
        
    def multiLingualCountry(self):
        isoCountry={}
        subdir=os.listdir('./data/')
        for s in subdir:
            path='./data/'+s+'/country.csv'
            with open(path,'r', encoding="utf-8") as csvfile:   
                readCSV = csv.reader(csvfile, delimiter=',')
                x=0
                for row in readCSV:    
                    if x>0:
                        isoCountry[row[1].lower()]=row[0]
                    
                    x=x+1
        
        return(isoCountry)    
    
    def stateLoad(self):
        stateDeAbbr={}                    #FL-Florida
        stateAbbr={}                        #Florida=FL
        cityInState={}                      #Miami->Florida,Ohio
        stateHasCity={}                    #Florida->Miami,Tellehesse
        
        with open('states.csv','r',encoding='utf-8') as csvfile:            #row[0]=cityName, 2=Abbr 3=DeAbbr
            readCSV=csv.reader(csvfile,delimiter=',')
            ctr=0
            for row in readCSV:
                if ctr>0:
                    if row[2] not in stateDeAbbr:
                        stateDeAbbr[row[2]]=row[3].lower()
                        
                    if row[2] not in stateHasCity:
                        stateHasCity[row[2]]=[]
                    stateHasCity[row[2]].append(row[0])
                    
                    if row[0].lower() not in cityInState:
                        cityInState[row[0].lower()]=[]
                    cityInState[row[0].lower()].append(row[2])
                    
                    if row[3].lower() not in stateAbbr:
                        stateAbbr[row[3].lower()]=row[2]
                        
                ctr=ctr+1

        return(stateDeAbbr,stateAbbr,cityInState,stateHasCity)
        
        
    def loadPrior(self,s='big'):
        cityNCountry={}
        totalCityNCountry=0
        cityNState={}
        totalCityNState=0
        
        aggState={}
        aggCountry={}
        totalState=0
        totalCountry=0
        
        open=self.openCity('countryScore.',s,'c')
        cityNCountry=open[0]
        totalCityNCountry=open[1]
        
        open=self.openCity('stateScore.',s,'c')
        cityNState=open[0]
        totalCityNState=open[1]
        
        open=self.openTotal('totCountry.',s,'c')
        aggCountry=open[0]
        totalCountry=open[1]
        
        open=self.openTotal('totState.',s,'s')
        aggState=open[0]
        totalState=open[1]
        
        return(cityNCountry,totalCityNCountry,cityNState,totalCityNState,aggState,aggCountry,totalState,totalCountry)
        
        
    def openCity(self,name,s,type):
        if type=='s':               #FIX
            variable=self.stateDeAbbr#Fip
        if type=='c':   
            variable=self.fipAbbr                   #AF->Afghanistan

        c={}
        t=0
        file=open(name+s,'r').read().split('\n')
        for f in file:
            if len(f)>0:
                row=f.split('|')
                if row[0] in variable:
                    row[0]=variable[row[0]]
                #print(row[0])
                if row[0] not in c:
                    c[row[0]]={}
                if row[1] not in c[row[0]]:
                    c[row[0]][row[1]]=1
                if int(row[2])>-1:    
                    c[row[0]][row[1]]=c[row[0]][row[1]]+int(row[2])
                    t=t+int(row[2])
     
        
        return(c,t)
        
    def openTotal(self,name,s,type):
        if type=='s':
            variable=self.stateDeAbbr
        if type=='c':
            variable=self.fipAbbr
            
        t=0
        n={}
        
        file=open(name+s,'r').read().split('\n')
        for f in file:
            if len(f)>0:
                row=f.split('|')
                if row[0] in variable:
                    row[0]=variable[row[0]]
                if row[0] not in n:
                    n[row[0]]=1
                if int(row[1])>-1:
                    n[row[0]]=n[row[0]]+int(row[1])
                    t=t+int(row[1])
        
        return(n,t)
        
        
        
class textExtract:
    def __init__(self):
        self.geo=geoExtract()
        
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
        candidate=self.candidateGen(textList)
        
        
        return(candidate)
        
    def candidateGen(self,textList):
        city=[]
        state=[]
        country=[]
        geo=self.geo
        for textItem in textList:
            for item in textItem:
                if item in geo.stateDeAbbr:
                    
                    state.append([item,float(1)])
                    country.append(['united states',float(0.5)])
                if item.lower() in geo.stateAbbr:
                    
                    state.append([geo.stateAbbr[item.lower()],float(0.5)])
                    country.append(['united states',float(0.5)])
                
                if item in geo.iso2DeAbbr:
                    cand=geo.iso2DeAbbr[item]
                      
                    country.append([cand,float(1)])
                    
                if item in geo.iso3DeAbbr:
                    cand=geo.iso3DeAbbr[item]
                      
                    country.append([cand,float(1)])
              #              
                if item in geo.fipDeAbbr:
                    country.append([geo.fipDeAbbr[item],float(1)])
                            
                if item.lower() in geo.fipAbbr:
                    
                    c = geo.fipAbbr[item.lower()]
                    country.append([geo.fipDeAbbr[c],float(1)])
                
                        
                if item.lower() in geo.MLCountry and geo.MLCountry[item.lower()] in geo.fipDeAbbr:
                
                    c=geo.fipDeAbbr[geo.MLCountry[item.lower()]]
                    country.append([c,float(1)])
                    
            
                if item.lower() in geo.cityInState:
                    city.append([item.lower(),float(1)])
                    s={}
                    t=0
                    for i in geo.cityInState[item.lower()]:
                        s[i]=float(geo.cityNState[i][item.lower()])
                        t=t+float(geo.cityNState[i][item.lower()])
                    for i in geo.cityInState[item.lower()]:
                        state.append([i,s[i]/t])
                    
                    country.append(['united states',float(0.5)])    
                        
                    #state.append([i,/float(geo.totalCityNState)])                        
                        
                        
                if item.lower() in geo.cityInFIP:
                    if wf(item.lower(),'en')>0:
                        city.append([item.lower(),float(1)])
                        c={}
                        t=0
                        for i in geo.cityInFIP[item.lower()]:
                            
                            if i in geo.fipDeAbbr and i in geo.cityNCountry and item.lower() in geo.cityNCountry[i]:
                                c[i]=math.log(1/wf(item.lower(),'en'))*float(geo.cityNCountry[i][item.lower()])
                                t=t+math.log(1/wf(item.lower(),'en'))*float(geo.cityNCountry[i][item.lower()])
                        
                        for i in geo.cityInFIP[item.lower()]:
                           if i in geo.fipDeAbbr and i in c:                            
                                country.append([geo.fipDeAbbr[i],c[i]/t])
        
        candidateCity={}
        candidateState={}
        candidateCountry={}
        
        for c in city:
            if c[0] not in candidateCity:
                candidateCity[c[0]]=0
            candidateCity[c[0]]=candidateCity[c[0]]+c[1]
            
        for s in state:    
            if s[0] not in candidateState:
                candidateState[s[0]]=0
            candidateState[s[0]]=candidateState[s[0]]+s[1]
        for c in country:
            if c[0] not in candidateCountry:
                candidateCountry[c[0]]=0
            candidateCountry[c[0]]=candidateCountry[c[0]]+c[1]
        #print(candidateCity,candidateState,candidateCountry)    
        return(self.candidateResolution(candidateCity,candidateState,candidateCountry))
        
    
    def candidateResolution(self,city,state,country):
        
        candidateCity=""
        candidateState=""
        candidateCountry=""
        if len(country)>0:
            countrySort=sorted(country.items(),key=operator.itemgetter(1),reverse=True)    
            candidateCountry=countrySort[0][0]
        if len(city)>0:
            for c in city:
                if  candidateCountry in self.geo.fipAbbr and self.geo.fipAbbr[candidateCountry] in self.geo.cityNCountry and c in self.geo.cityNCountry[self.geo.fipAbbr[candidateCountry]]:
                    
                    city[c]=city[c]*self.geo.cityNCountry[self.geo.fipAbbr[candidateCountry]][c]
                    
                else:
                    city[c]=0
            
            citySort=sorted(city.items(),key=operator.itemgetter(1),reverse=True)
            candidateCity=citySort[0][0]
        #self.cityInFIP=loadCity[0]                          #Lahore->PK
        #self.FIPhasCity=loadCity[1]                         #PK->Lahore
        
        
        if candidateCountry != 'united states':
            candidateState=""    
        if candidateCountry=='united states' and candidateCity =="":
            if len(state)>0:
                stateSort=sorted(state.items(),key=operator.itemgetter(1),reverse=True)
                candidateState=stateSort[0][0]
            
        if candidateCountry =="united states" and candidateCity !="":
            for s in state:
                if candidateCity in self.geo.cityInState:
                    if s in self.geo.cityInState[candidateCity]:
                        state[s]=state[s]*self.geo.cityNState[s][candidateCity]
                    else:
                        state[s]=0
                else:
                    candidateCity=""
            if len(state)>0:        
                stateSort=sorted(state.items(),key=operator.itemgetter(1),reverse=True)
                candidateState=stateSort[0][0]
            else:
                candidateState=""
        if candidateCity == candidateCountry:
            candidateCity=""
        if candidateState=="" and candidateCountry =="united states":
            candidateCity=""
        return(candidateCity,candidateState,candidateCountry)


path='xx.txt'
csv_file=open('xx_updated3','w')
writer=csv.writer(csv_file,delimiter='|', lineterminator='\n')
G=textExtract()
P=[]
x=0
with open(path,'r', encoding="utf-8") as csvfile:   
    readCSV = csv.reader(csvfile, delimiter='|')
    for row in readCSV: 
        x=x+1
        if x>50:
            break
        city=""
        state=""
        country=""

        if len(row)>4:
            location=row[4].replace('\t',' ')
            output=G.extract(location)
            city=output[0]
            state=output[1]
            country=output[2]
            P.append([output,location])
        '''
        row.append(city)
        row.append(state)
        row.append(country)
        writer.writerow(row)
        '''
    