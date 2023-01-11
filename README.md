ESITI PUBBLICATI 1/190 

- 22/12/2022 01 A6  Ricerca operativa	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/01%252FA6/1/4) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/01%252FA6/2/4) 

UPDATED 2023-01-11 12:14:31.230508
######################################################

Si tratta di un semplice script in python per controllare quando sono pubblicati gli esiti (ASN 2021, quarto quadrimestre).

E' sufficiente avere installato python3 e lanciare "python3 getasn.py". E' necessario che nella cartella esista il file secs.txt (contiene l'elenco dei SSC). Se presente il file tobenotified.txt, il programma manda avvisi alle e-mail presenti.

Per lanciarlo ripetutamente, si possono usare run.sh (file bash settato per ogni ora) oppure gestire un crontab.

Tiziano
