class Film:
    def __init__(self):
        self._title = ""
        self._rentals = 0
        self.add_rentals()

    def setter_title(self, title):
        self._title = title

    def getter_title(self):
        return self._title

    def getter_rentals(self):
        return self._rentals

    def add_rentals(self):
        self._rentals += 1


def main():
    film = Film()
    film.setter_title("Film najlepszy23")

    title = film.getter_title()
    rentals = film.getter_rentals()

    print(title, rentals)


if __name__ == "__main__":
    main()
