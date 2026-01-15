import math

def sieve(A, n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if A[i] == True:
            j = 2 *i
            while j <= n:
                A[j] = False
                j += i

def main():
    n = 100

    A = [True] * (n + 1)

    A[0] = False
    A[1] = False

    sieve(A, n)

    print("Liczby pierwsze od 2 do 100: ")
    for i in range(2, n + 1):
        if A[i] == True:
            print(str(i) + ", ")


if __name__ == "__main__":
    main()
