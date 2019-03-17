#57527235
text=open('xx.txt','r',encoding='utf-8').read().split('\n')
file2=open('tweet.psv','w',encoding='utf-8')
x=0
for f in text:
    if len(f)>0:
        row=f.split('\t | \t')
        if len(row)>4:
            location=row[4]
            #print(location)
            file2.write(location+'\n')
            if x>1000:
                break
                
                
            x=x+1
file2.close()            