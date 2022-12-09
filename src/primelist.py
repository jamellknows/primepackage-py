import math
from random import random, randint
def primelist(start, end):
    theta = math.pi /3 
    arr = []
    length = end - start
    
    if(length == 0):
        rand = random()
        start = math.floor(length * rand)
        end  = start + length
        
     
    for i in range(start, length):
        y = theta * (1 + 6*i)
        y = math.sqrt((y/theta)**2 - 0.25)
        arr.append(y)
        y = theta* 5 *(1 + (6/5)*i)
        y = math.sqrt((y/theta)-0.25)
        arr.append(y)
        
    arr.sort()

    prime = []
    for i in range(0, len(arr)-1):
        arr[i] = math.floor(arr[i])
        if(math.floor(arr[i]) % 2 != 0):
            arr[i] = arr[i] + 1
        prime.append(arr[i]+1)
        prime.append(arr[i]-1)
       
    prime.sort()
    
    primeh = []
    for i in range(0, len(prime)-1):
        if prime[i] not in primeh:
            primeh.append(prime[i])
    begin = 0
    fini = len(primeh)-1
    
    for i in range(0, len(primeh)-1):
        if primeh[i] <= start:
                begin = i
        if primeh[i] <= end:
                fini = i
        
    
    prime = primeh
    prime = prime[begin:fini]
    
    #set prime[0] = start
    #prime[len(prime)-1] = end
    #slice function copy into riemann list 
    return prime
      
        
    