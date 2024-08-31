height, width = map(int, input().split())

board = []

for h in range(height):
    line = list(input())
    board.append(line)

counts = []
opposite = { 'B' : 'W', 'W' : 'B' }

for a in range(height-7):
    for b in range(width-7):
        count = 0
        last_line_color = 'W'
        last_color = last_line_color
        for h in range(8):
            for w in range(8):
                color = opposite[last_color]
                now = board[a+h][b+w]
                if color != now:
                    count += 1
                last_color = color
            last_line_color = opposite[last_line_color]
            last_color = last_line_color

        counts.append(count)
        counts.append(64 - count)

print(min(counts))

    