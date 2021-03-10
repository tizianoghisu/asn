i=1
while [ $i -gt 0 ]; do
    rm present.txt
    ./getasn.sh
    cat present.txt >> secs_ordered.txt
    cp notpresent.txt secs.txt
    i=`wc notpresent.txt | awk '{print $1}'`
    sec=`grep  '/' secs_ordered.txt | wc | awk '{print $1}'`
    echo "ESITI PUBBLICATI" $sec"/190" > README.md
    echo "" >> README.md
    cat  secs_ordered.txt >> README.md
    date=`date`
    echo "" >> README.md
    echo "UPDATED "$date >> README.md
    echo "" >> README.md
    cat spiegazione.txt >> README.md
    git add README.md
    git commit -m "update"
    git push -u https://t.ghisu%40unica.it:tuzzu070279@github.com/tizianoghisu/asn.git main
    sleep 3600
done
