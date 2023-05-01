import sys
import time
from datetime import datetime

from sudoku import Sudoku


def main():
    # takes difficulty as an argument, if not provided the program removes half of the board (level 3)
    args = [int(x) if x.isdecimal() else x for x in sys.argv[1:]]
    difficulty = args[0] if len(args) > 0 else 3

    sudoku = Sudoku()

    # trying in Total for 10 mins to find a sudoku
    timeout = 600
    start_time = time.time()
    end_time = start_time + timeout

    while time.time() < end_time:
        if sudoku.generate(difficulty) == True:
            break
        else:
            sudoku.reset()

    # printing
    sudoku.print()

    # creating the .svg-File with crrent date, time and difficulty
    svg = sudoku.toSVG()
    now = datetime.now()
    name = f'sudoku-{now:%Y%m%dT%H%M%S}-{difficulty}.svg'
    with open(name, 'w') as f:
        f.write(svg)


if __name__ == "__main__":
    main()
