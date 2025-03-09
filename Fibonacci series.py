
#Fibonacci series using Memonization

def fib(m,d ={0:0,1:1}):
    if m in d:
        return d[m]
    else:
        d[m] = fib(m-1,d) + fib(m-2,d)
        return d[m]

print(fib(50))