i=1
while [ $i -gt 0 ]; do
    python3 getasn.sh
    i=`wc secs.txt | awk '{print $1}'`
    sleep 3600
done
