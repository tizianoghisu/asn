mailaddr='dummy'
if [ $# -lt 2 ]
then
	s=1
	e=`wc secs.txt | awk '{print $1}'`
else
	s=$1
	e=$2
fi
echo $s $e
rm present.txt notpresent.txt
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
      echo $date $i0 >> present.txt
      echo "" >> present.txt
      new="$i0 USCITO $date"
      if [[ 'dummy' =~ $mailaddr ]]; then   
        echo "Not sending"
      else
        echo $new | mail -s "$new" $mailaddr
      fi
   fi
   echo $i0 $check
done


