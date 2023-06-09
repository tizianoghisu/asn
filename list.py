from utilities import * 

area='09' 
settore='C1' 
fascia='1'
 
list1=getalllist(area, settore, fascia)  
for item in list1:
    print(item, sep='\t')

