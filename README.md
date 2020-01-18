# Sudoku
Python Algo for solving sudoku puzzles - Algoritimo em python para resolver sudokus

to test it out, you'll need to transcribe the sudoku into a list of ints and '.' (in place of blank squares),
initialize the "RoubaSudoku" with the list and call the "soluciona" function.

In solving the sudoku, it turns every blank into a int list and scrapes the incompatible numbers, turning any list with len 1 into a int. It also checks if the cell is the only possible placce for any number (ex: if there is no other position for a "3" in the row).

It works really well in easy and hard puzzles from sudoku.com, but struggles with expert puzzles, where you need to guess some cells in order to procede.
