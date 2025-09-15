from math import sqrt

#### Fonction secondaire


def isprime(p):
    for b in range(2,p):
        if p%b == 0:
            return True
    return False
pass


#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
