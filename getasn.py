import requests
import csv, smtplib, ssl
from email.mime.text import MIMEText
import shutil
from datetime import datetime

f=open('secs.txt','r')
lines=f.readlines()
f.close()


trues=[]
falses=[]
sectors=[]

for line in lines:
    check=False
    s1=line.split()[0]
    s2=line.split()[1]
    page="https://asn18.cineca.it/pubblico/miur/esito/"+s1+"%252F"+s2+"/2/6"
    response=requests.get(page)
    text=response.text
    if not ('Non risultano' in text):
        check=True
        v=text[text.find("Dal"):]
        date=v.split()[1]
    if not check:
        page="https://asn18.cineca.it/pubblico/miur/esito/"+s1+"%252F"+s2+"/1/6"
        response=requests.get(page)
        text=response.text
        if not ('Non risultano' in text):
            check=True
            v=text[text.find("Dal"):]
            date=v.split()[1]
    if check:
        trues.append(line)
        sectors.append(line.split()[0]+'/'+line.split()[1])
    else:
        falses.append(line)
    print(line+str(check))
 
from_address = "asnrisultati@gmail.com"
password = "provaprova"

msg = MIMEText('This is test mail')
msg['Subject'] = 'Test mail'

context = ssl.create_default_context()
f=open("tobenotified.txt")
lines=f.readlines()
f.close()
no=open('notifications.out','a')
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    for line in lines:
        s=line.split()[0]
        if any(s in sector for sector in sectors):
            p="I have notified "+str(line.split()[1])+" for sector "+str(line.split()[0])+" \n"
            no.write(p)
            msg=MIMEText("Sono stati pubblicati i risultati del SSC "+s)
            msg['Subject']="NUOVI RISULTATI ASN"
            server.sendmail(
                from_address,
                line.split()[1], msg.as_string())

no.close()
f1=open('present.txt','w')
f2=open('notpresent.txt','w')
f3=open('secs_ordered.txt','a')

for line in falses:
    f2.write(line)
for line in trues:
    f1.write('- '+date+' '+line)
    f3.write('')
    f3.write('- '+date+' '+line)

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
f.write('ESITI PUBBLICATI '+str(count)+'/190 \n')
for sec in secs:
    s1=sec.split()[2]
    s2=sec.split()[3]
    p1="https://asn18.cineca.it/pubblico/miur/esito/"+s1+"%252F"+s2+"/1/6"
    p2="https://asn18.cineca.it/pubblico/miur/esito/"+s1+"%252F"+s2+"/2/6"
    f.write('\n')
    f.write(sec.rstrip("\n")+" [I fascia]("+p1+") [II fascia]("+p2+") \n")

f.write('\n')
now = datetime.now()
f.write('UPDATED '+str(now))
f.close()
