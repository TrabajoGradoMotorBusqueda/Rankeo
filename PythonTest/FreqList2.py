from collections import Counter 
from itertools import repeat, chain 
  
ini_list = [1, 2, 3, 4, 4, 5, 5, 5, 5, 7, 
            1, 1, 2, 4, 7, 8, 9, 6, 6, 6] 
  
# printing initial ini_list 
print ("initial list", str(ini_list)) 
  
# sorting on bais of frequency of elements 
result = list(chain(i for i, c in Counter(ini_list).most_common())) 
  
# printing final result 
print("final list", str(result)) 
