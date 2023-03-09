
from __future__ import annotations

import sys # for sys.maxsize


class Move:

	def __init__(self, row: int, col: int):
		self.row = row
		self.col = col

	def __str__(self):
		return f"Move({self.row}, {self.col})"
	
	def __repr__(self):
		return f"Move({self.row}, {self.col})"

class Board:

	def __init__(self):

		self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
		self.player = 'X'

	def __str__(self):
		return self.board, self.player
	
	def getNextPlayer(self) -> str:
		if self.player == 'X':
			return 'O'
		else:
			return 'X'

	def printBoard(self):
		print("\n")
		for row, i in zip(self.board, range(3)):
			for col, j in zip(row, range(3)):
				print(col, end='')
				if j != 2:
					print("|", end='')
			if i != 2:
				print("\n-----")
		print("\n")


	def validMoves(self) -> list[Move]:
		validMoves = []
		for row in range(3):
			for col in range(3):
				if self.board[row][col] == ' ':
					validMoves.append(Move(row, col))
		return validMoves
	
	def makeMove(self, move: Move, player: str):
		self.board[move.row][move.col] = player
		# self.printBoard()


	def gameWinner(self) -> str | None:
		for row in range(3):
			if self.board[row][0] == self.board[row][1] == self.board[row][2] and self.board[row][0] != ' ':
				return self.board[row][0]
		for col in range(3):
			if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
				return self.board[0][col]
		if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
			return self.board[0][0]
		if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
			return self.board[0][2]
		return None
	
	def isBoardFilled(self) -> bool:
		for row in range(3):
			for col in range(3):
				if self.board[row][col] == ' ':
					return False
		return True
	
	def makeHumanMove(self):
		while True:
			row = int(input("Enter row: "))
			col = int(input("Enter col: "))
			if self.board[row][col] == ' ':
				self.board[row][col] = self.player
				break
			else:
				print("Invalid move, try again")
	
	def makeBestMove(self):
		bestScore = -sys.maxsize
		bestMove = None

		for move in self.validMoves():
			
			self.makeMove(move, 'X')

			# isMaximizing = False
			# if self.player == 'X':
			# 	isMaximizing = True
			score = self.minimax(0, False)

			# undo move
			self.board[move.row][move.col] = ' '

			if score > bestScore:
				print("score: ", score)
				bestScore = score
				bestMove = move

		self.makeMove(bestMove, 'X')

	def minimax(self, depth, isMaximizing):
		scores = {
			'X': 10,
			'O': -10,
			'TIE': 0
		}
		result = self.gameWinner()
		# print("result: ", result)

		if result is not None:
			return scores[result]
		elif self.isBoardFilled():
			return scores['TIE']
				
		if isMaximizing:
			bestScore = -sys.maxsize
			for move in self.validMoves():

				# self.player = self.getNextPlayer()
				self.makeMove(move, 'X')
				
				score = self.minimax(depth + 1, False)
				
				self.board[move.row][move.col] = ' '
				# self.player = self.getNextPlayer()

				bestScore = max(score, bestScore)

			return bestScore
		else:
			bestScore = sys.maxsize
			for move in self.validMoves():

				self.makeMove(move, 'O')
				# self.player = self.getNextPlayer()
				
				score = self.minimax(depth + 1, True)

				bestScore = min(score, bestScore)

				self.board[move.row][move.col] = ' '
				# self.player = self.getNextPlayer()
			return bestScore






def main():

	board = Board()


	while True:
		board.printBoard()


		if board.player == 'X':
			print("Player X's turn")			
			board.makeBestMove()
		else:
			print("Player O's turn")
			board.makeHumanMove()


		board.player = board.getNextPlayer()
		
		winner = board.gameWinner()
		if winner != None:
			print("Winner is ", winner)
			break
		elif board.isBoardFilled():
			print("Tie")
			break

	board.printBoard()

	



if __name__ == '__main__':
	main()