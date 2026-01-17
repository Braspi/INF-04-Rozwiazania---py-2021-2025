class Tools:
    def licz_samogloski(self, text):

        if not text:
            return 0

        samogloski = "aąeęiouóAĄEĘIOUÓY"
        ilosc_samoglosek = 0


        for samogloska in samogloski:
            if samogloska in text:
                ilosc_samoglosek += 1

        return ilosc_samoglosek

    def usun_powtorzenia(self, text):

        if not text:
            return 0

        wynik = text[0]

        for i in range(1, len(text)):
            if text[i] != text[i-1]:
                wynik += text[i]

        return wynik


def main():
    text = input("Podaj tekst: ")

    tools = Tools()
    print(tools.licz_samogloski(text))

    print(tools.usun_powtorzenia(text))

if __name__ == "__main__":
    main()