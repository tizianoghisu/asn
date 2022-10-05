mailaddr='dumm'
if [ $# -lt 2 ]
then   
	s=1
	e=`wc secs.txt | awk '{print $1}'`
else
	s=$1
	e=$2   
fi  
echo $s $e
if [ -f "present.txt" ]; then   
    rm present.txt   
fi
if [ -f "notpresent.txt" ]; then
    rm notpresent.txt 
fi 
i=$s
while [ $i -le $e ]; do 
   i1=`head -n$i secs.txt | tail -n1 | awk '{print $1}'`
   i2=`head -n$i secs.txt | tail -n1 | awk '{print $2}'`
   i3=`head -n$i secs.txt | tail -n1 | awk '{print $3}'`
   i0=`head -n$i secs.txt | tail -n1 | awk '{print $0}'`
   i=`expr $i + 1`
   check='False'
   curl https://asn18.cineca.it/pubblico/miur/esito/${i1}%252F${i2}/2/6 >& page.html 
   page=`cat page.html` 
   if [[ $page != *'Non risultano'* ]]; then
      check='True'
      date=`grep Dal page.html | head -n1 | awk '{print $2}'`
   fi
   curl https://asn18.cineca.it/pubblico/miur/esito/${i1}%252F${i2}/1/6 >& page.html
   page=`cat page.html` 
   if [[ $page != *'Non risultano'* ]]; then
      check='True'
      date=`grep Dal page.html | head -n1 | awk '{print $2}'`
   fi
   if [[ $check == 'False' ]]; then
      echo $i0 >> notpresent.txt
   else
      echo "" >> present.txt
      echo - $date $i0 >> present.txt
      new="$i0 USCITO $date"
      if [[ 'dummy' =~ $mailaddr ]]; then   
        echo "Not sending"
      else
        echo $new | mail -s "$new" $mailaddr
      fi
   fi
   echo $i0 $check
done

if [ -f "present.txt" ]; then
    cat present.txt >> secs_ordered.txt
    grep '/'  present.txt > newsecs.txt 
fi
cp notpresent.txt secs.txt
i=`wc notpresent.txt | awk '{print $1}'`
sec=`grep  '/' secs_ordered.txt | wc | awk '{print $1}'`
echo "ESITI PUBBLICATI" $sec"/190" > README.md
echo "" >> README.md
grep '/'  secs_ordered.txt > tmp.txt
cat tmp.txt | awk '{print $0, "[I fascia](https://asn18.cineca.it/pubblico/miur/esito/"$3"%252F"$4"/1/6) [I    I fascia](https://asn18.cineca.it/pubblico/miur/esito/"$3"%252F"$4"/2/6)"}' >> README.md
date=`date`
echo "" >> README.md
echo "UPDATED "$date >> README.md
echo "" >> README.md
cat spiegazione.txt >> README.md
if [ -f "newsecs.txt" ]; then
    python3 sendmail.py >> notifications.out
fi
