from sudoku_class import *

ntrials = 50
asudoku = sudoku()
for n in range(30, 70, 5):
    completed = 0
    for i in range(ntrials):
        asudoku.makepuzzle(n)
        asudoku.solve()

        if asudoku.solved():
            completed += 1
print(n, (asudoku.solved()/ntrials))