class Notes:
    __counter_notes = 0
    def __init__(self, title, content):
        Notes.__counter_notes += 1
        self.__id = Notes.__counter_notes

        self._title = title
        self._content = content

    def print_notes(self):
        print("Tytuł: " + self._title)
        print("Treść: " + self._content)


    def diagnostic(self):
        print(self._title , ";" , self._content , ";", self.__id , ";" , Notes.__counter_notes )

def main():
    notes = Notes("Notetka 1", "Lorem ipsum dolor sit amet")
    notes2 = Notes("Notetka 2", "Lorem ipsum dolor sit amet niggaer")

    notes.print_notes()
    notes2.print_notes()

    notes.diagnostic()

if __name__ == "__main__":
    main()
