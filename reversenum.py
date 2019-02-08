n = int(input())    
R = 0    
while(n > 0):    
    i = n %10    
    R = (R *10) + i  
    n = n //10    
print(R)   
