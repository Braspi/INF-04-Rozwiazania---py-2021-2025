class Sort:
    def __init__(self):
        self.table = []

    def read(self):
        print("Podaj 10 liczb (całkwitych)")
        for i in range(10):
            number = int(input())
            self.table.append(number)

    def find_max(self, start):
        maxIndex = start
        for i in range(len(self.table)):
            if self.table[i] < self.table[maxIndex]:
                maxIndex = i
        return maxIndex


    def selection_sort(self):
        for i in range(len(self.table)):
            maxIndex = self.find_max(i)

            temp = self.table[i]
            self.table[i] = self.table[maxIndex]
            self.table[maxIndex] = temp

    def print(self):
        print("Posortowana tablica: ")
        for i in range(len(self.table)):
            print(self.table[i])

def main():
    sort = Sort()
    sort.read()
    sort.selection_sort()
    sort.print()

if __name__ == "__main__":
    main()
