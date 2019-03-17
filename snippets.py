
def countries():
    file=open('countries.txt','r', encoding="utf-8").read().split('\n')
    country={}

    for i in range(1,len(file)):
        if len(file[i])>0:
            row=file[i].split('\t')
            if len(row[1])>0:
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
                if row[1].lower() not in city:
                    city[row[1].lower()]=[]
                
                city[row[1].lower()].append(row[0])
    return(city)

def openCity(name,s,city,total,type):
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
    
def openTotal(name,s,total,name,type):
    if type=='s':               #FIX
        variable=self.state
    if type=='c':   
        variable=self.country
    t=total
    file=open(name+s,'r').read().split('\n')
    n=name
    for f in file:
        if len(f)>0:
            row=f.split('|')
            if row[0] in variable:
                row[0]=variable[row[0]]
            n[row[0]]=int(row[1])
            t=t+int(row[1])
            
    file.close()
    return(n,t)
 
    
def loadPrior(s='small'):
    cCity={}
    cTotle=0
    sCity={}
    sTotal=0
    state={}
    totalS=0
    country={}
    totalC=0
    tempOpen=openCity('countryScore.',s,cCity,cTotal,'c')       #split acronyms
    cCity=tempOpen[0]
    cTotal=tempOpen[1]
    
    tempOpen=openCity('stateScore.',s,sCity,sTotal,'s')
    sCity=tempOpen[0]
    sTotal=tempOpen[1]
    
    tempOpen=openCity('totState.',s,totalS,state,'s')
    state=tempOpen[0]
    totalS=tempOpen[0]
    
    tempOpen=openCity('totCountry.',s,totalC,country,'c')
    country=tempOpen[0]
    totalC=tempOpen[0]
    return(cCity,cTotal,sCity,sTotal,state,totalS,country,totalC)
def isValid(L):
    flag=[0,0,0]
    if L[0]=="" and L[1]=="":
        flag=[0,0,1]
    
    if L[1]!="" and L[0] !="":
        
        if sCity[L[1]][L[0]]>0:
            flag=[1,1,0]
        else:
            flag=[0,0,1]
           
        if cCity[L[2]][L[0]]>0:
            flag=[1,flag[1],1]
        else:
            flag=[0,flag[1],1]
            
    if L[1]=="":
        if cCity[L[2][L[0]]]>0:
            flag=[1,0,1]
        else:
            flag=[0,0,1]
    for i in range(0,len(L)):
        if flag[i]==0:
            L[i]=""
    return(L)
              
        
    