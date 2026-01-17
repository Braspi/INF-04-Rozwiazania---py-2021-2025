def cezar(text, key):
    result = []

    for x in text:
        if x == "":
            result.append(" ")
        else:
            pos = ord(x) - 97
            new_pos = (pos + key) % 26
            result.append(chr(new_pos + 97))
    return "".join(result)

def main():
    text = input("Podaj text: ")
    key = int(input("Podaj key: "))
    print(cezar(text, key))

if __name__ == "__main__":
    main()