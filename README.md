ESITI PUBBLICATI 0/190 

UPDATED 2021-12-15 20:26:47.308107
######################################################

Si tratta di un semplice script in python per controllare quando sono pubblicati gli esiti (ASN 2018, sesto quadrimestre).

E' sufficiente avere installato python3 e lanciare "python3 getasn.py". E' necessario che nella cartella esista il file secs.txt (contiene l'elenco dei SSC). Se presente il file tobenotified.txt, il programma manda avvisi alle e-mail presenti.

Per lanciarlo ripetutamente, si possono usare run.sh (file bash settato per ogni ora) oppure gestire un crontab.

Tiziano
