print("Start")
print('')

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

############################### end of definitions ############################

p = 45
q = 210

a = 36
b = 71

K = lcm( int(lcm(p,a)/a), int(lcm(q,b)/b) )

### predict? ###

print("Arby Predicts: ", int(K*a/p)%2, ",", int(K*b/q)%2)

### SOLVE BRUTE FORCE STYLE ###

cuepos = [0, 0]
count = 0

def step():
    cuepos[0] += a
    cuepos[1] += b
    
while count < K:
    count += 1
    step()
    if cuepos[0] % p == 0 and cuepos[1] % q == 0:
        break
    
print("Position: ", cuepos)
print("Pos Relat:", int(cuepos[0] / p), ",", int(cuepos[1] / q))
print("Modulo:   ", int(cuepos[0] / p % 2), ",", int(cuepos[1] / q % 2))
#print("Count:    ", count)
print("K:        ", K)
