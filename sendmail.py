import csv, smtplib, ssl
from email.mime.text import MIMEText

from_address = "asnrisultati@gmail.com"
password = "provaprova"

f=open("present.txt", 'r')
lines=f.readlines();
f.close()
sectors=[]
for line in lines:
    if len(line.split())>3:
        s1=line.split()[2]
        s2=line.split()[3]
        s=s1+'/'+s2
        sectors.append(s)

msg = MIMEText('This is test mail')
msg['Subject'] = 'Test mail'

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_address, password)
    f=open("tobenotified.txt")
    lines=f.readlines()
    for line in lines:
        s=line.split()[0]
        if any(s in sector for sector in sectors):
            print("I have notified %s for sector %s\n" % (line.split()[1], line.split()[0]) )
            msg=MIMEText("Sono stati pubblicati i risultati del SSC "+s)
            msg['Subject']="NUOVI RISULTATI ASN"
            server.sendmail(
                from_address,
                line.split()[1], msg.as_string())
