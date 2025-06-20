import pygame
import sys

pygame.init()
font = pygame.font.SysFont(None, 60)

WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

BG = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
LINE_WIDTH = 15

board = [[0 for _ in range(3)] for _ in range(3)]
CurrentPlayer = 1

def MsgWinner(player):
    txt = f"Player {player} Winner"
    img = font.render(txt, True, (255, 255, 255))
    celebrateImg = pygame.image.load("celebrate.png")
    celebrateImg = pygame.transform.scale(celebrateImg, (200, 200))
    screen.blit(img, (300 - img.get_width() // 2, 300 - img.get_height() // 2 - 100))
    screen.blit(celebrateImg, (300 - 100, 270))

def RestButton():
    ButtRectangle = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 80, 200, 50)
    pygame.draw.rect(screen, (50, 50, 50), ButtRectangle, border_radius=10)
    txt = font.render("Restart", True, (255, 255, 255))
    screen.blit(txt, (WIDTH // 2 - txt.get_width() // 2, HEIGHT - 75))
    return ButtRectangle

def RestartGame():
    global board, CurrentPlayer, GameOver, winner
    board = [[0 for _ in range(3)] for _ in range(3)]
    CurrentPlayer = 1
    GameOver = False
    winner = None

def drawLines():
    pygame.draw.line(screen, LINE_COLOR, (0, 200), (600, 200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 400), (600, 400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200, 0), (200, 600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400, 0), (400, 600), LINE_WIDTH)

def getCellPos(pos):
    x, y = pos
    row = y // 200
    col = x // 200
    return row, col

def isCellEmpty(row, col):
    return board[row][col] == 0

def MarkCell(r, c, player):
    board[r][c] = player

def PrintBoard():
    for i in board:
        print(i)
    print()

def Draw():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 1:
                startX1 = (col * 200 + 40, row * 200 + 40)
                endX1 = (col * 200 + 160, row * 200 + 160)
                startX2 = (col * 200 + 40, row * 200 + 160)
                endX2 = (col * 200 + 160, row * 200 + 40)
                pygame.draw.line(screen, (66, 66, 66), startX1, endX1, 15)
                pygame.draw.line(screen, (66, 66, 66), startX2, endX2, 15)
            elif board[row][col] == 2:
                center = (col * 200 + 100, row * 200 + 100)
                pygame.draw.circle(screen, (66, 66, 66), center, 60, 15)

def CheckWinnner(player):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

running = True
winner = None
GameOver = False
restart_Button = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            if GameOver:
                if restart_Button and restart_Button.collidepoint(mousepos):
                    RestartGame()
            else:
                row, col = getCellPos(mousepos)
                if isCellEmpty(row, col):
                    MarkCell(row, col, CurrentPlayer)
                    PrintBoard()
                    if CheckWinnner(CurrentPlayer):
                        winner = CurrentPlayer
                        GameOver = True
                    else:
                        CurrentPlayer = 2 if CurrentPlayer == 1 else 1

    screen.fill(BG)
    drawLines()
    Draw()
    if GameOver and winner is not None:
        MsgWinner(winner)
        restart_Button = RestButton()
    pygame.display.flip()

pygame.quit()
sys.exit()