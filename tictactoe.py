# Creating board
board = ["   " for x in range(9)]

class TicTacToe:
    def __init__(self, board):
        self.is_play = True
        self.display_board(board)
        self.choice()

    def display_board(self, board):
        print(f"{board[0]}|{board[1]}|{board[2]}")
        print("---+---+---")
        print(f"{board[3]}|{board[4]}|{board[5]}")
        print("---+---+---")
        print(f"{board[6]}|{board[7]}|{board[8]}")
        print("\n")

    def choice(self):
        while self.is_play:
            self.x_choice = int(input("Enter the position of 'X': "))
            board[self.x_choice - 1] = " X "
            self.display_board(board)

            self.o_choice = int(input("Enter the position of 'O': "))
            board[self.o_choice - 1] = " O "
            self.display_board(board)

            if self.winner() == False:
                print("Draw")
                self.is_play = False

    def winner(self):
        #Horizontal Line for X
        if board[0] == " X " and board[1] == " X " and board[2] == " X ":
            print("X win")
            self.is_play = False
        elif board[3] == " X " and board[4] == " X " and board[5] == " X ":
            print("X win")
            self.is_play = False

        elif board[6] == " X " and board[7] == " X " and board[8] == " X ":
            print("X win")
            self.is_play = False

        # Horizontal Line for O
        if board[0] == " O " and board[1] == " O " and board[2] == " O ":
            print("O win")
            self.is_play = False
        elif board[3] == " O " and board[4] == " O " and board[5] == " O ":
            print("O win")
            self.is_play = False
        elif board[6] == " O " and board[7] == " O " and board[8] == " O ":
            print("O win")
            self.is_play = False

        # Vertical Line for X
        if board[0] == " X " and board[3] == " X " and board[6] == " X ":
            self.is_play = False
            print("X win")
        elif board[1] == " X " and board[4] == " X " and board[7] == " X ":
            self.is_play = False
            print("X win")
        elif board[2] == " X " and board[5] == " X " and board[8] == " X ":
            self.is_play = False
            print("X win")

        #Veritcal line for 0
        if board[0] == " O " and board[3] == " O " and board[6] == " O ":
            self.is_play = False
            print("O win")
        elif board[1] == " O " and board[4] == " O " and board[7] == " O ":
            self.is_play = False
            print("O win")
        elif board[2] == " O " and board[5] == " O " and board[8] == " O ":
            self.is_play = False
            print("O win")

        #Diagonally for X
        if board[0] == " X " and board[4] == " X " and board[8] == " X ":
            self.is_play = False
            print("X win")
        elif board[2] == " X " and board[4] == " X " and board[6] == " X ":
            self.is_play = False
            print("X win")

        # Diagonally for O
        if board[0] == " O " and board[4] == " O " and board[8] == " O ":
            self.is_play = False
            print("O win")
        elif board[2] == " O " and board[4] == " O " and board[6] == " O ":
            self.is_play = False
            print("O win")


print("""
TYPE THE NUMBER TO INSERT 'X' AND 'O'\n
(1)|(2)|(3)
---+---+---
(4)|(5)|(6) 
---+---+---
(7)|(8)|(9)
                """)
game = TicTacToe(board)

