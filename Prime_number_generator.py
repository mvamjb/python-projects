def is_prime(n,k=2) -> bool:
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    if k*k > n:
        return True
    if n % k == 0 and n != k:
        return False
    else:
        k += 1
        return is_prime(n,k)
def generate_primes(limit):
    primes = []
    for x in range(2,limit):
        if is_prime(x) == True:
            primes.append(x)
    return primes
 

while True:
    try:
        c = int(input("Enter upper bound for primes: "))
        if c >= 2:
            break
        else:
            print("Please enter an integer ≥ 2.")
    except:
        print("That wasnt a number--Try again.")

num = generate_primes(c)
print(num)
