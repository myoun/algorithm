nsudoku = []
for i in range(9):
    nsudoku.append(list(map(int, input().split())))

blanks = []
numbers = set(range(1, 10))

# Find Blank
for line in range(9):
    for idx in range(9):
        e = nsudoku[line][idx]
        if e == 0:
            blanks.append((line, idx))

def solve(blank):
    if len(blanks) == blank:
        return
    line, idx = blanks[blank]

    found = set()

    # search row
    for i in range(9):
        e = nsudoku[line][i]
        if e != 0:
            found.add(e)
    
    # search column
    for i in range(9):
        e = nsudoku[i][idx]
        if e != 0:
            found.add(e)

    box_line = (line // 3) * 3
    box_idx = (idx // 3) * 3

    for i in range(3):
        for j in range(3):
            e = nsudoku[box_line+i][box_idx+j]
            if e != 0:
                found.add(e)

    possible_numbers = numbers - found

    for i in possible_numbers:
        nsudoku[line][idx] = i
        solve(blank+1)
    
    for i in nsudoku:
        print(" ".join(map(str, i)))

for i in range(len(blanks)):
    solve(i)
