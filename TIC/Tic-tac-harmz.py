# -*- coding: utf-8 -*-
"""
Created on Fri Apr  5 09:45:33 2024

@author: Harmony
"""
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import font , ttk , messagebox
import random
root = tk.Tk()

# from main import *
# import pygame , sys
# pygame.quit()
# sys.exit()
# pygame.init()

root.title("TIC-TAC-TOE")
# print("*****************************")
# print("*        *         *        *")
# print("*    1   *   2     *   3    *")
# print("*****************************")
# print("*        *         *        *")
# print("*    4   *    5    *    6   *")
# print("*****************************")
# print("*        *         *        *")
# print("*    7   *    8    *   9    *")
# print("*****************************\n")

def computer(row , col):
    global current_player, computer_user
    computer_user = 'o'
    if game[row][col] == '' :
       game[row][col] = current_player
    k = random.randint(0, 2)
    l = random.randint(0, 2)
      # buttons[row][col].configure(text=current_player)
    if  game[k][l] == '' and game[row][col] == 'x':
        buttons[k][l].configure(text=computer_user)
        game[k][l] = computer_user
        if game[k][l] != None:
            buttons[row][col].configure(text=current_player)
            #check_winner()
    check_winner()

def make_your_move(row, col):
    global current_player
    if game[row][col] == '':
        #curr_player = ''
        #curr_player = tk.
        game[row][col] = current_player
        buttons[row][col].\
            configure(text=current_player)
        check_winner()
        current_player  = "o"\
            if current_player == "x"\
            else "x"
        messagebox.showinfo( "PLAYER",message= f"{current_player} is next")

def check_winner():
    #game = [['', '', ''] for _ in range(3)]
    wining_comb = (game[0] , game[1] , game[2] ,

                   [game[i][0] for i in range(3)],
                   [game[i][1] for i in range(3)],
                   [game[i][2] for i in range(3)],
                   [game[i][i]for i  in range(3)],
                   [game[i][2 - i] for i in range(3)])
    global combination
    for combination in wining_comb:
        if combination[0] == combination[1] == combination[2] != '':
            announce_winner(combination[0])
            print(combination[0])
    if all(game[i][j] != ''for i in range(3) for j in  range(3)):
        #print()
        announce_winner("Draw")
other_player = ''

"""
def announce_winner(player):#shows the scoreboard too
    count = 0
    count_2 = 0
    #name = (f"x: {count} - {count_2} o")
    if player == "x" or announce_winner("") :
            message = "It is a draw!"
            count += 0
            count_2 += 0
            messagebox.showinfo("scoreboard" , name)
    else:
            message = f"Player {player} wins!"
            #count += 1
            #count_2 += 1
           # messagebox.showinfo("scoreboard" , (count ,"-", count_2 ))
            #messagebox.showinfo("Scoreboard" , name)

    #messagebox.showinfo("Game over", message)
    reset_game()
"""

def announce_winner(player):
        if player == "Draw":
            message = "It is a draw!"
        else:
            message = f"Player {player} wins!"
        messagebox.showinfo("Game over", message)
        reset_game()

def reset_game():
    global game , current_player
    game = [['' , '' , '']for _ in range(3)]
    #current_player = "x"
    for row in buttons:
        for button in row:
            button.configure(text= '')
    k = random.randint(0, 2)
    l = random.randint(0, 2)
    #buttons[k][l].configure(text=computer_user)

def newWindow():
    master = tk.Tk()
    global buttons
    global row
    buttons = []
    for i in range(3):
        row = []
        for j in range(3):

             #messagebox.showinfo("PLAYER", message="TIC-TAC-TOE")
             tkinter.Label(text="TIC-TAC-TOE")
             button = ttk.Button(master, text='', width=10
                                 ,command= lambda i = i, j = j: make_your_move
                                 (i , j))
             button.grid(row=i, column=j, padx=15, pady=18)
             row.append(button)
        buttons.append(row)
    root.withdraw()


def comp():
    master = tk.Tk()
    global buttons
    global row ,  col
    buttons = []
    for i in range(3):
        row = []
        for j in range(3):
             root.title("TIC-TAC-TOE")
             button = ttk.Button(master, text='', width=10
                                 ,command= lambda i = i, j = j: computer(i , j))
             button.grid(row=i, column=j, padx=15, pady=18)
             row.append(button)
        buttons.append(row)
    k = random.randint(0, 2)
    l = random.randint(0, 2)
    buttons[k][l].configure(text=computer_user)
    root.withdraw()

game = [['' , '' , '']for _ in range(3)]
current_player = 'x'
computer_user = 'o' if current_player == 'x' else 'x'

label = Label(root,text = "WELCOME TO HARMONY'S WORLD!" ,
              height= 5 , width= 37 , fg= "red").grid(pady =  3 , padx= 5)
tk.Button(root ,  text="Player vs player 2", background="grey",foreground="black",
          height=3, width=15 , command= newWindow).grid(pady= 5 , padx= 5)
tk.Button(root , text= "Player vs computer" , background= "grey" ,foreground="black" ,
           height= 3 , width=15 , command= comp).grid(pady= 5 , padx= 5)
v = Scale(root, fg= "red",bg= "black",from_= 0 , to= 10 , orient= HORIZONTAL)
v.grid()#homeboard for the start game option
root.mainloop()

def newButton\
                ( root,command,  width=5):
    return tk.Button(parent, text="start game",background= "red",
                          foreground= "black",  width=10, command= command).pack()   # prints the interface to play

import sys
sys.exit(0)
# players = ["xo"]
# computer, human = "",""
# human = str(input("Do you want to be X or O? ")).lower()
# print(f"{human} plays first")

