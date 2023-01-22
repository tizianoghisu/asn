ESITI PUBBLICATI 5/190 

- 19/01/2023 07 H3  Malattie infettive e parassitarie degli animali	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/07%252FH3/1/4) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/07%252FH3/2/4) 

- 19/01/2023 07 H2  Patologia veterinaria e ispezione degli alimenti di origine animale	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/07%252FH2/1/4) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/07%252FH2/2/4) 

- 18/01/2023 10 D1  Storia antica	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/10%252FD1/1/4) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/10%252FD1/2/4) 

- 11/01/2023 02 D1  Fisica applicata, didattica e storia della fisica	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/02%252FD1/1/4) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/02%252FD1/2/4) 

- 22/12/2022 01 A6  Ricerca operativa	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/01%252FA6/1/4) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/01%252FA6/2/4) 

UPDATED 2023-01-22 16:15:52.487408
######################################################

Si tratta di un semplice script in python per controllare quando sono pubblicati gli esiti (ASN 2021, quarto quadrimestre).

E' sufficiente avere installato python3 e lanciare "python3 getasn.py". E' necessario che nella cartella esista il file secs.txt (contiene l'elenco dei SSC). Se presente il file tobenotified.txt, il programma manda avvisi alle e-mail presenti.

Per lanciarlo ripetutamente, si possono usare run.sh (file bash settato per ogni ora) oppure gestire un crontab.

Tiziano
