i=1
while [ $i -gt 0 ]; do
    ./getasn.sh
    i=`wc notpresent.txt | awk '{print $1}'`
    sleep 3600
done
