# Strategy Pattern: permite trocar algoritmos de forma flexível

class SortStrategy:
    def sort(self, data):
        raise NotImplementedError

class BubbleSortStrategy(SortStrategy):
    def sort(self, data):
        print("Usando BubbleSort")
        return sorted(data)  # Simulação

class QuickSortStrategy(SortStrategy):
    def sort(self, data):
        print("Usando QuickSort")
        return sorted(data)  # Simulação

class Sorter:
    def __init__(self, strategy: SortStrategy):
        self.strategy = strategy

    def set_strategy(self, strategy: SortStrategy):
        self.strategy = strategy

    def sort(self, data):
        return self.strategy.sort(data)

if __name__ == "__main__":
    data = [5, 3, 8, 1]
    sorter = Sorter(BubbleSortStrategy())
    print(sorter.sort(data))
    sorter.set_strategy(QuickSortStrategy())
    print(sorter.sort(data))
