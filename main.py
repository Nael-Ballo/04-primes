from math import sqrt

#### Fonction secondaire

def isprime(p):
    if p < 2:
        return False
    for b in range(2, int(sqrt(p)) + 1):
        if p % b == 0:
            return False
    return True

#### Fonction principale

def main():
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()

if __name__ == "__main__":
    main()
