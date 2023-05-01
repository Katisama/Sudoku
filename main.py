class Sudoku:

    def __init__(self):
       self.reset()

    def reset(self):
        rows = 9
        columns = 9
        self.board = \
            [[0 for j in range(columns)]
            for i in range(rows)]

    def print(self):
        for i in range(9):
            print(" ".join(
                [str(x) if x != 0 else "."
                for x in self.board[i]]))

def main():
    #...

if __name__ == "__main__":
    main()

