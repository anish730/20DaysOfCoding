#print fibonacci series using recursive function.

def recur_fibo(n):
    if n==0 or n==1:
        return n 
    else:
        return recur_fibo(n-1) + recur_fibo(n-2)
nth_terms = 8

for i in range(nth_terms):
    print(recur_fibo(i))