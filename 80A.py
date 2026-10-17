def first_n_primes(n):
    primes = []
    candidate = 2

    while len(primes) < n:
        is_prime = True

        for divisor in primes:
            if divisor * divisor > candidate:
                break
            if candidate % divisor == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(candidate)

        candidate += 1

    return primes


m,n = map(int,input().split())
b=first_n_primes(n)
c=0
for i in range(len(b)):
    if b[i]==m and b[i+1]==n:
        c+=1
if c>0:
    print("YES")
else:
    print("NO")
        
        
