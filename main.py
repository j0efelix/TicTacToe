board = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]

class Tictactoe:
    def __init__(self, board):
        print("""
    TYPE THE NUMBER TO INSERT 'X' AND 'O'
                (1)|(2)|(3)
                ---+---+---
                (4)|(5)|(6) 
                ---+---+---
                (7)|(8)|(9)
                         """)
        self.display_board(board)

    def display_board(self, board):
        print("\n")
        print(f"{board[0]}|{board[1]}|{board[2]}")
        print("---+---+---")
        print(f"{board[3]}|{board[4]}|{board[5]}")
        print("---+---+---")
        print(f"{board[6]}|{board[7]}|{board[8]}")
        print("\n")

    def user_choice(self):
        self.x_choice = int(input("Enter the position of 'X': "))
        board[self.x_choice - 1] = " X "
        self.display_board(board)
        self.o_choice = int(input("Enter the position of 'O': "))
        board[self.o_choice - 1] = " O "
        self.display_board(board)

    def check_winner(self, is_play):
        if board[0] and board[1] and board[2] == "X":
            is_play = False
            print("X is the winner")

game = Tictactoe(board)
is_play = True
while is_play:
    game.user_choice()
    game.check_winner(is_play)

