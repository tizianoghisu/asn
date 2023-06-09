import requests
import os
import csv, smtplib, ssl
from email.mime.text import MIMEText 
import shutil 
from datetime import datetime, timedelta   
from utilities import * 

notify=True    

f=open('secs.txt','r')
lines=f.readlines()
f.close() 


trues=[]
falses=[]
sectors=[]
dates=[]
r1=[]
r2=[]
for line in lines:
    check=False
    s1=line.split()[0]
    s2=line.split()[1]
    page="https://asn21.cineca.it/pubblico/miur/esito/"+s1+"%252F"+s2+"/2/5"
    l=getfulllist(page,s1+s2)
    #print(text)
    if len(l)>0:
        check=True
        res2=evstats(l)
        date=None
        for item in l:
            if item["Esito"]=="Si":
                date=item["Data"]
                break

    page="https://asn21.cineca.it/pubblico/miur/esito/"+s1+"%252F"+s2+"/1/5"
    l=getfulllist(page,s1+s2)
    if len(l)>0:
        check=True
        res1=evstats(l)
        if date!=None:
            for item in l:
                if item["Esito"]=="Si":
                    date=item["Data"]
                    break

    if check:
        dates.append(date)
        trues.append(line)
        sectors.append(line.split()[0]+'/'+line.split()[1])
        r1.append(res1)
        r2.append(res2)
    else:
        falses.append(line)
    print(line.split()[0]+'/'+line.split()[1]+' '+str(check))

if ((notify==True) and (len(trues)>0)):   
    from_address = "asnrisultati@gmail.com"
    password = "kshrmwjnslgjyamw"


    msg = MIMEText('This is test mail')
    msg['Subject'] = 'Test mail'

    if os.path.exists("tobenotified.txt"):
        f=open("tobenotified.txt")
        lines=f.readlines()
        f.close()
        context = ssl.create_default_context()
        no=open('notifications.out','a')
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(from_address, password)
            for line in lines:
                s=line.split()[0]
                if any(s in sector for sector in sectors):
                    for i in range(1,len(line.split())):
                        email=line.split()[i]
                        p="I have notified "+str(email)+" for sector "+str(line.split()[0])+" \n"
                        no.write(p)
                        msg=MIMEText("Sono stati pubblicati i risultati del SSC "+s)
                        msg['Subject']="NUOVI RISULTATI ASN"
                        server.sendmail(
                            from_address,
                            email, msg.as_string())
        no.close()
    
f1=open('present.txt','w')
f2=open('notpresent.txt','w')
f3=open('secs_ordered.txt','a')

for line in falses:
    f2.write(line)
i=-1
for line in trues:
    i+=1
    f1.write('- '+dates[i]+' '+line)
    f3.write('')
    #f3.write('- '+dates[i]+' '+line)
    f3.write('- '+dates[i]+' '+line.rstrip('\n')+' PERCENTUALI: '+str(round(r1[i]*1000)/10)+' (I) '+str(round(r2[i]*1000)/10)+" (II)\n")

f1.close()
f2.close()
f3.close()


shutil.copyfile('notpresent.txt','secs.txt')

f=open('secs_ordered.txt')
lines=f.readlines()
count=0
secs=[]
for line in lines:
    if len(line.split())>1:
        secs.append(line)
        count+=1
f.close()

f=open('README.md','w')
#f.write('visita il sito [https://www.risultatiasn.it](https://www.risultatiasn.it) (aggiornato in tempo reale)\n')
f.write('ESITI PUBBLICATI '+str(count)+'/190 \n')
secs.sort(key=lambda date: (datetime.strptime(date.split()[1], '%d/%m/%Y'), date.split()[2], date.split()[3]))
for sec in secs[::-1]:
    s1=sec.split()[2]
    s2=sec.split()[3]
    p1="https://asn21.cineca.it/pubblico/miur/esito/"+s1+"%252F"+s2+"/1/5"
    p2="https://asn21.cineca.it/pubblico/miur/esito/"+s1+"%252F"+s2+"/2/5"
    f.write('\n')
    f.write(sec.partition("PERCENTUALI")[0]+" [I fascia]("+p1+") [II fascia]("+p2+") \n")

secs.sort(key=lambda date: (date.split()[2], date.split()[3]))
f.write("\n")
f.write("PERCENTUALI DI PASSAGGIO PER SETTORE:\n")
for sec in secs:
    s1=sec.split()[2]
    s2=sec.split()[3]
    f.write('\n')
    f.write(s1+'/'+s2+': '+sec.partition("PERCENTUALI")[2])



f.write('\n')
now = datetime.now()
hours=1
hoursToAdd = timedelta(hours = hours)
timeToPrint=now+hoursToAdd

f.write('UPDATED '+str(timeToPrint))
        
fs=open('spiegazione.txt','r')        
lines=fs.readlines()
fs.close()
for line in lines:
        f.write(line)
        
        
f.close()
        
        
