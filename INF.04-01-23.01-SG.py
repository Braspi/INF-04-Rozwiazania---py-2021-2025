def nwd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def main():
    wynik = nwd(int(input("podaj A: ")), int(input("podaj B: ")))
    print("NWD " + str(wynik))

if __name__ == "__main__":
    main()  