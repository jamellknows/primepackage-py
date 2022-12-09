def primefactors(num):
    import math
    from random import random
    
    theta = math.pi /3 
    arr = []
    length = num
    
    if(length == 0):
        rand = random()
        start = math.floor(length * rand)
        end  = start + length
        
     
    for i in range(0, length):
        y = theta * (1 + 6*i)
        y = math.sqrt((y/theta)**2 - 0.25)
        arr.append(y)
        # y = theta* 5 *(1 + (6/5)*i)
        # y = math.sqrt((y/theta)-0.25)
        # arr.append(y)
        
    arr.sort()

    prime = []
    for i in range(0, len(arr)-1):
        arr[i] = math.floor(arr[i])
        if(math.floor(arr[i]) % 2 != 0):
            arr[i] = arr[i] + 1
        prime.append(arr[i]+1)
        # prime.append(arr[i]-1)
       
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
    #bascally I need to subract primes from the number
    for i in range()
    
    
      