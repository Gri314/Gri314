print("Start")
print("")

def gcf2(n, m): ## SECOND GCF FUNCTION ##
    
    outbox = 1
    
    for i in range(2, n + 1):
        
        if n % i == 0 and m % i == 0:
            outbox = i
            
    return outbox

def gcf(a,b): ## ACTUAL GCF WHEN CALLED BELOW ##
    if a < b:
        return gcf2(a,b)
    else:
        return gcf2(b,a)

def lcm(a,b):
    K = gcf(a,b)
    if K == 1:
        return a * b
    else:
        return int((a*b)/K)

print(gcf(13, 26))
print(lcm(4,5))
