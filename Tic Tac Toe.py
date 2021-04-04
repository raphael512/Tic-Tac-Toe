from tkinter import *
from tkinter import messagebox
def canvasInit():
    canvas.create_line(133, 0, 133, 400)
    canvas.create_line(266, 0, 266, 400)
    canvas.create_line(0, 133, 400, 133)
    canvas.create_line(0, 266, 400, 266)
    canvas.pack(fill=BOTH, expand=1)
    canvas.bind("<Button-1>", callback)

def callback(event):
    if(event.x < 133 and event.y < 133):
        ans(1)
    elif((event.x > 133 and event.x < 266) and event.y < 133):
        ans(2)
    elif(event.x > 266 and event.y < 133):
        ans(3)
    elif(event.x < 133 and (event.y > 133 and event.y < 266)):
        ans(4)
    elif((event.x > 133 and event.x < 266) and (event.y > 133 and event.y < 266)):
        ans(5)
    elif(event.x > 266 and (event.y > 133 and event.y < 266)):
        ans(6)
    elif(event.x < 133 and event.y > 266):
        ans(7)
    elif((event.x > 133 and event.x < 266) and event.y > 266):
        ans(8)
    elif(event.x > 266 and event.y > 266):
        ans(9)

def ans(x):
    global player
    if(x == 1 and ansList[0][0] == ' '):
        if(player == 1):
            drawCircle(65, 65)
            ansList[0][0] = 'o'
            player = 2
            check(0, 0)
        else:
            drawCross(65, 65)
            ansList[0][0] = 'x'
            player = 1
            check(0, 0)

    elif(x == 2 and ansList[0][1] == ' '):
        if(player == 1):
            drawCircle(200, 65)
            ansList[0][1] = 'o'
            player = 2
            check(0, 1)
        else:
            drawCross(200, 65)
            ansList[0][1] = 'x'
            player = 1
            check(0, 1)

    elif(x == 3 and ansList[0][2] == ' '):
        if(player == 1):
            drawCircle(335, 65)
            ansList[0][2] = 'o'
            player = 2
            check(0, 2)
        else:
            drawCross(335, 65)
            ansList[0][2] = 'x'
            player = 1
            check(0, 2)

    elif(x == 4 and ansList[1][0] == ' '):
        if(player == 1):
            drawCircle(65, 200)
            ansList[1][0] = 'o'
            player = 2
            check(1, 0)
        else:
            drawCross(65, 200)
            ansList[1][0] = 'x'
            player = 1
            check(1, 0)

    elif(x == 5 and ansList[1][1] == ' '):
        if(player == 1):
            drawCircle(200, 200)
            ansList[1][1] = 'o'
            player = 2
            check(1, 1)
        else:
            drawCross(200, 200)
            ansList[1][1] = 'x'
            player = 1
            check(1, 1)

    elif(x == 6 and ansList[1][2] == ' '):
        if(player == 1):
            drawCircle(335, 200)
            ansList[1][2] = 'o'
            player = 2
            check(1, 2)
        else:
            drawCross(335, 200)
            ansList[1][2] = 'x'
            player = 1
            check(1, 2)

    elif(x == 7 and ansList[2][0] == ' '):
        if(player == 1):
            drawCircle(65, 335)
            ansList[2][0] = 'o'
            player = 2
            check(2, 0)
        else:
            drawCross(65, 335)
            ansList[2][0] = 'x'
            player = 1
            check(2, 0)

    elif(x == 8 and ansList[2][1] == ' '):
        if(player == 1):
            drawCircle(200, 335)
            ansList[2][1] = 'o'
            player = 2 
            check(2, 1)
        else:
            drawCross(200, 335)
            ansList[2][1] = 'x'
            player = 1
            check(2, 1)

    elif(x == 9 and ansList[2][2] == ' '):
        if(player == 1):
            drawCircle(335, 335)
            ansList[2][2] = 'o'
            player = 2
            check(2, 2)
        else:
            drawCross(335, 335)
            ansList[2][2] = 'x'
            player = 1
            check(2, 2)
    
 
def drawCircle(x, y):
    r = 60
    x0 = x - r
    y0 = y - r
    x1 = x + r
    y1 = y + r
    return canvas.create_oval(x0, y0, x1, y1)

def drawCross(x, y):
    center = 55

    x0 = x - center
    y0 = y - center 
    x1 = x + center 
    y1 = y + center
    canvas.create_line(x0, y0, x1, y1)
    
    x0 = x - center
    y0 = y + center 
    x1 = x + center 
    y1 = y - center
    return canvas.create_line(x0, y0, x1, y1)

def check(x, y):
    ch = ansList[x][y]
    if(ch == ' '):
        return
    if(ansList[0][0] == ch):
        print("?")
        if(ansList[0][1] == ch):
            if(ansList[0][2] == ch):
                if(player == 1):
                    return messagebox.showinfo(title="Congratulations", message="Player 2 is the winner!")
                else:
                    return messagebox.showinfo(title="Congratulations", message="Player 1 is the winner!")
        if(ansList[1][0] == ch):
            if(ansList[2][0] == ch):
                if(player == 1):
                    return messagebox.showinfo(title="Congratulations", message="Player 2 is the winner!")
                else:
                    return messagebox.showinfo(title="Congratulations", message="Player 1 is the winner!")
        if(ansList[1][1] == ch):
            if(ansList[2][2] == ch):
                if(player == 1):
                    return messagebox.showinfo(title="Congratulations", message="Player 2 is the winner!")
                else:
                    return messagebox.showinfo(title="Congratulations", message="Player 1 is the winner!")

    if(ansList[0][2] == ch):
        if(ansList[1][1] == ch):
            if(ansList[2][0] == ch):
                if(player == 1):
                    return messagebox.showinfo(title="Congratulations", message="Player 2 is the winner!")
                else:
                    return messagebox.showinfo(title="Congratulations", message="Player 1 is the winner!")
        if(ansList[1][2] == ch):
            if(ansList[2][2] == ch):
                if(player == 1):
                    return messagebox.showinfo(title="Congratulations", message="Player 2 is the winner!")
                else:
                    return messagebox.showinfo(title="Congratulations", message="Player 1 is the winner!")

    if(ansList[2][0] == ch):
        if(ansList[2][1] == ch):
            if(ansList[2][2] == ch):
                if(player == 1):
                    return messagebox.showinfo(title="Congratulations", message="Player 2 is the winner!")
                else:
                    return messagebox.showinfo(title="Congratulations", message="Player 1 is the winner!")

    if(ansList[0][1] == ch):
        if(ansList[1][1] == ch):
            if(ansList[2][1] == ch):
                if(player == 1):
                    return messagebox.showinfo(title="Congratulations", message="Player 2 is the winner!")
                else:
                    return messagebox.showinfo(title="Congratulations", message="Player 1 is the winner!")

    if(ansList[1][0] == ch):
        if(ansList[1][1] == ch):
            if(ansList[1][2] == ch):
                if(player == 1):
                    return messagebox.showinfo(title="Congratulations", message="Player 2 is the winner!")
                else:
                    return messagebox.showinfo(title="Congratulations", message="Player 1 is the winner!")
        




root = Tk()
root.title("Tic-Tac-Toe")
root.geometry('400x400')
canvas = Canvas()
canvasInit()

global player
player = 1
ansList = [[' ',' ',' '], [' ',' ',' '], [' ',' ',' ']]
root.mainloop()