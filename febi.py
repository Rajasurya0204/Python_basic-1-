nterms = int(input())
n1 = 0
n2 = 1
count = 0
if nterms == 1:
   print(nterms)
else:
   while count < nterms:
       print(n2,end=" ")
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1
