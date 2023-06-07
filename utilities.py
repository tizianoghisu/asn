import requests
import os
import csv, smtplib, ssl
from email.mime.text import MIMEText
import shutil
from datetime import datetime, timedelta


def getlist2013(page,settore):
    tutti=[]
    response=requests.get(page)
    text=response.text
    while ' ' in text:
        text = text.replace(' ','')
    text = text.replace('<td>','')
    text = text.replace('</td>','')
    text = text.replace('</b>','')
    text = text.replace('<tdstyle="padding-left:5px;">','')

    entries=text.split()
    for i in range (len(entries)):
        if ('Dal' in entries[i]):
            if 'text-align' in entries[i-5]:
                x = { 
                    "Cognome": entries[i-9].replace('<bstyle="text-align:center;display:block">',''),
                    "Nome": entries[i-8].replace('<bstyle="text-align:center;display:block">',''),
                    "Risultato": entries[i-6].replace('<bstyle="text-align:center;display:block">',''),
                    "Data": entries[i].replace('Dal',''),
                    "Settore": settore
                    }
            else:
                x = { 
                    "Cognome": entries[i-6].replace('<bstyle="text-align:center;display:block">',''),
                    "Nome": entries[i-5].replace('<bstyle="text-align:center;display:block">',''),
                    "Risultato": entries[i-3].replace('<bstyle="text-align:center;display:block">',''),
                    "Data": entries[i].replace('Dal',''),
                    "Settore": settore
                    }
            tutti.append(x)
    return tutti


def getlist(page,settore):
    tutti=[]
    response=requests.get(page)
    text=response.text
    while ' ' in text:
        text = text.replace(' ','')
    text = text.replace('<td>','')
    text = text.replace('</td>','')
    text = text.replace('</b>','')
    text = text.replace('<tdstyle="padding-left:5px;">','')

    entries=text.split()
    for i in range (len(entries)):
        if ('Dal' in entries[i]):
            x = { 
                "Cognome": entries[i-4].replace('<bstyle="text-align:center;display:block">',''),
                "Nome": entries[i-3].replace('<bstyle="text-align:center;display:block">',''),
                "Risultato": entries[i-1].replace('<bstyle="text-align:center;display:block">',''),
                "Data": entries[i].replace('Dal',''),
                "Settore": settore
                }
            tutti.append(x)
    return tutti

def getalllist(s1,s2,f):

    pages=[]
    pages.append("https://abilitazione.cineca.it/ministero.php/public/esitoAbilitati/settore/"+s1+"%252F"+s2+"/fascia/"+f)
    pages.append("https://asn.cineca.it/ministero.php/public/esitoAbilitati/settore/"+s1+"%252F"+s2+"/fascia/"+f)
    pages.append("https://asn16.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/1")
    pages.append("https://asn16.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/2")
    pages.append("https://asn16.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/3")
    pages.append("https://asn16.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/4")
    pages.append("https://asn16.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/5")
    pages.append("https://asn18.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/1")
    pages.append("https://asn18.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/2")
    pages.append("https://asn18.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/3")
    pages.append("https://asn18.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/4")
    pages.append("https://asn18.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/5")
    pages.append("https://asn18.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/6")
    pages.append("https://asn21.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/1")
    pages.append("https://asn21.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/2")
    pages.append("https://asn21.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/3")
    pages.append("https://asn21.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/4")
    pages.append("https://asn21.cineca.it/pubblico/miur/esito-abilitato/"+s1+"%252F"+s2+"/"+f+"/5")

    ab=[]
	
    for i in range(len(pages)):
        page=pages[i]
        if (i==1):
            ab=ab+(getlist2013(page,s1+s2))
        else:
            ab=ab+(getlist(page,s1+s2))

    ab.sort(key=lambda x: (x["Cognome"], x["Nome"]))
	
    return ab

def comparelists(list1,list2):

    commonlist=[]
    for item1 in list1:
        for item2 in list2:
            if item1["Cognome"]==item2["Cognome"] and item1["Nome"]==item2["Nome"]:
                x = { 
                    "Cognome": item1["Cognome"],
                    "Nome": item1["Nome"],
                    "Settore1": item1["Settore"], 
                    "Data1": item1["Data"], 
                    "Settore2": item2["Settore"], 
                    "Data2": item2["Data"], 
                    }
                commonlist.append(x)

    return commonlist


list1=getalllist('09','A1','1')
list2=getalllist('09','C1','1')
common=comparelists(list1,list2)
for item in common:
    print(item, sep='\t')


list1=getalllist('09','A1','2')
list2=getalllist('09','C1','2')
common=comparelists(list1,list2)
for item in common:
    print(item, sep='\t')
	
