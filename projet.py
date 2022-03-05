import random


class projet:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_joueur(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, joueur):
        self.board[row][col] = joueur

    def is_player_win(self, joueur):
        gagner = None

        n = len(self.board)

        for i in range(n):
            gagner = True
            for j in range(n):
                if self.board[i][j] != joueur:
                    gagner = False
                    break
            if gagner:
                return gagner

        '''les colonnes'''
        for i in range(n):
            gagner = True
            for j in range(n):
                if self.board[j][i] != joueur:
                    gagner = False
                    break
            if gagner:
                return gagner

        '''les diagonales'''
        gagner = True
        for i in range(n):
            if self.board[i][i] != joueur:
                gagner = False
                break
        if gagner:
            return gagner

        gagner = True
        for i in range(n):
            if self.board[i][n - 1 - i] != joueur:
                win = False
                break
        if gagner:
            return gagner
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_joueur_turn(self, joueur):
        return 'X' if joueur == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item)
            print()

    def start(self):
        self.create_board()

        joueur = 'X' \
            if self.get_random_first() == 1 else 'O'
        while True:
            print(f" joueur {joueur} tourne")

            self.show_board()

            row, col = list(
                map(int, input("Entrez les numéros de ligne et de colonne :").split()))
            print()

            self.fix_spot(row - 1, col - 1, joueur)

            """Voir si il a gagné ou a perdu"""
            if self.is_player_win(joueur):
                print(f"joueur {joueur} tu as gagné!")
                break

            """jeux nul ou non"""
            if self.is_board_filled():
                print("Egalité")
                break

            player = self.swap_joueur_turn(joueur)

        """le tableau final"""
        print()
        self.show_board()

    def get_random_first (self):
        pass

    def get_random_first (self):
        pass
