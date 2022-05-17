ESITI PUBBLICATI 10/190 

- 16/05/2022 12 C2  Diritto ecclesiastico e canonico	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/12%252FC2/1/2) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/12%252FC2/2/2) 

- 16/05/2022 10 L1  Lingue, letterature e culture inglese e anglo-americane	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/10%252FL1/1/2) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/10%252FL1/2/2) 

- 13/05/2022 10 M1  Lingue, letterature e culture germaniche	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/10%252FM1/1/2) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/10%252FM1/2/2) 

- 13/05/2022 06 L1  Anestesiologia	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/06%252FL1/1/2) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/06%252FL1/2/2) 

- 11/05/2022 14 A1  Filosofia politica	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/14%252FA1/1/2) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/14%252FA1/2/2) 

- 11/05/2022 11 D1  Pedagogia e storia della pedagogia	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/11%252FD1/1/2) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/11%252FD1/2/2) 

- 10/05/2022 06 H1  Ginecologia e ostetricia	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/06%252FH1/1/2) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/06%252FH1/2/2) 

- 10/05/2022 03 D1  Chimica e tecnologie farmaceutiche, tossicologiche e nutraceutico-alimentari	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/03%252FD1/1/2) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/03%252FD1/2/2) 

- 06/05/2022 11 A4  Scienze del libro e del documento e scienze storico religiose	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/11%252FA4/1/2) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/11%252FA4/2/2) 

- 04/05/2022 10 C1  Musica, teatro, cinema, televisione e media audiovisivi	 [I fascia](https://asn21.cineca.it/pubblico/miur/esito/10%252FC1/1/2) [II fascia](https://asn21.cineca.it/pubblico/miur/esito/10%252FC1/2/2) 

UPDATED 2022-05-17 15:15:09.312455
######################################################

Si tratta di un semplice script in python per controllare quando sono pubblicati gli esiti (ASN 2021, secondo quadrimestre).

E' sufficiente avere installato python3 e lanciare "python3 getasn.py". E' necessario che nella cartella esista il file secs.txt (contiene l'elenco dei SSC). Se presente il file tobenotified.txt, il programma manda avvisi alle e-mail presenti.

Per lanciarlo ripetutamente, si possono usare run.sh (file bash settato per ogni ora) oppure gestire un crontab.

Tiziano
