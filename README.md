ESITI PUBBLICATI 2/190 

- 06/05/2022 11 A4  Scienze del libro e del documento e scienze storico religiose	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/11%252FA4/1/2) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/11%252FA4/2/2) 

- 04/05/2022 10 C1  Musica, teatro, cinema, televisione e media audiovisivi	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/10%252FC1/1/2) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/10%252FC1/2/2) 

UPDATED 2022-05-08 21:18:33.514762
######################################################

Si tratta di un semplice script in python per controllare quando sono pubblicati gli esiti (ASN 2021, secondo quadrimestre).

E' sufficiente avere installato python3 e lanciare "python3 getasn.py". E' necessario che nella cartella esista il file secs.txt (contiene l'elenco dei SSC). Se presente il file tobenotified.txt, il programma manda avvisi alle e-mail presenti.

Per lanciarlo ripetutamente, si possono usare run.sh (file bash settato per ogni ora) oppure gestire un crontab.

Tiziano
