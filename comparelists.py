from utilities import *   

  
area1='09'
settore1='A1'
fascia1='1'
area2='09'
settore2='C1'
fascia2='1'

list1=getalllist(area1, settore1, fascia1)
list2=getalllist(area2, settore2, fascia2)

common=comparelists(list1,list2)
for item in common:
    print(item, sep='\t')


