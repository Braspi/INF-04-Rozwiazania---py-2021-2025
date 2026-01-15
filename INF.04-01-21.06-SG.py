class Sort:
    def __init__(self):
        self.tablica = []

    def read(self):
        print("Podaj 10 liczb całkowitcyh: ")
        for i in range(10):
            liczb = int(input())
            self.tablica.append(liczb)

    def __find_max(self, start):
        maxIndex = start
        for i in range(start+1, len(self.tablica)):
            if self.tablica[i] > self.tablica[maxIndex]:
                maxIndex = i
        return maxIndex

    def selection_sort(self):
        for i in range(len(self.tablica)):
            maxIndex = self.__find_max(i)

            temp = self.tablica[i]
            self.tablica[i] = self.tablica[maxIndex]
            self.tablica[maxIndex] = temp

    def print(self):
        print("Tablica: ")
        for liczb in self.tablica:
            print(liczb)

        find_max = self.__find_max(2)
        print(find_max, "max index")

def main():
    sort = Sort()
    sort.read()
    sort.selection_sort()
    sort.print()

if __name__ == "__main__":
    main()