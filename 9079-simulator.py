print("동전 모양 (3x3):")

board = [input().split() for i in range(3)]

print("""연산 목록:
1 x : x행의 동전을 모두 뒤집습니다.
2 y : y열의 동전을 모두 뒤집습니다.
3 : -> 방향의 대각선으로 동전을 모두 뒤집습니다.
4 : <- 방향의 대각선으로 동전을 모두 뒤집습니다.
5: 끝내기
""")

while True:
    rop = input()

    match rop[0]:
        case "1":
            x = int(rop[2])
            for i in range(3):
                board[x][i] = "H" if board[x][i] == "T" else "T"
        case "2":
            y = int(rop[2])
            for i in range(3):
                board[i][y] = "H" if board[i][y] == "T" else "T"
        case "3":
            for i in range(3):
                board[i][i] = "H" if board[i][i] == "T" else "T"
        case "4":
            for i in range(3):
                board[2-i][i] = "H" if board[2-i][i] == "T" else "T"
        case "5":
            break
    for i in range(3):
        print(board[i])
