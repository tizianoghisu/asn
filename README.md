ESITI PUBBLICATI 2/190 

- 01/09/2022 07 H3  Malattie infettive e parassitarie degli animali	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/07%252FH3/1/3) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/07%252FH3/2/3) 

- 30/08/2022 12 E4  Diritto dell'Unione europea	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/12%252FE4/1/3) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/12%252FE4/2/3) 

UPDATED 2022-09-06 11:19:16.307676
######################################################

Si tratta di un semplice script in python per controllare quando sono pubblicati gli esiti (ASN 2021, secondo quadrimestre).

E' sufficiente avere installato python3 e lanciare "python3 getasn.py". E' necessario che nella cartella esista il file secs.txt (contiene l'elenco dei SSC). Se presente il file tobenotified.txt, il programma manda avvisi alle e-mail presenti.

Per lanciarlo ripetutamente, si possono usare run.sh (file bash settato per ogni ora) oppure gestire un crontab.

Tiziano
