#include <iostream>
#include <ctime>		// time
#include <string>

using std::string;


enum Move { ROCK = 0, PAPER = 1, SCISSORS = 2 };
enum Result { PLAYER1, PLAYER2, TIE };

string moveToString(Move move) {
	switch (move) {
		case Move::ROCK:
			return "rock";
		case Move::PAPER:
			return "paper";
		case Move::SCISSORS:
			return "scissors";
	}
	return "";
}

Move getChoice() {
	std::cout << "Enter your move (rock, paper, or scissors): ";

	string choice;
	std::getline(std::cin, choice);

	// string[string.length()] = '\0' - will go to default case
	switch (choice[0]) {
		case 'r':
		case 'R':
			return Move::ROCK;
		case 'p':
		case 'P':
			return Move::PAPER;
		case 's':
		case 'S':
			return Move::SCISSORS;
		default:
			std::cout << "Invalid choice." << std::endl;
			return getChoice();
	}
}


Result calculateWinner(Move p1, Move p2) {
	Move winList[3] = { ROCK, PAPER, SCISSORS };
	Move loseList[3] = { SCISSORS, ROCK, PAPER };

	for (size_t i = 0; i < 3; i++) {
		if (p1 == winList[i] && p2 == loseList[i]) {
			return Result::PLAYER1;
		} else if (p1 == loseList[i] && p2 == winList[i]) {
			return Result::PLAYER2;
		}
	}
	return Result::TIE;
}

void printScores(string name, int playerWins, int computerWins) {
	std::cout << "---------------------------------" << std::endl;
	std::cout << name << ": " << playerWins << "\tComputer: " <<  computerWins << std::endl;
	std::cout << "---------------------------------" << std::endl;
}


int main() {

	srand(time(NULL));

	int playerWins = 0;
	int computerWins = 0;

	int games = 0;

	std::cout << "What is your name? ";
	string name;
	std::getline(std::cin, name);

	std::cout << "How many wins should we play until? ";
	int numWins;
	std::cin >> numWins;

	// FLUSH CIN BUFFER???
	string _;
	std::getline(std::cin, _);

	std::cout << "Let’s see who can win " << numWins << " games first! Good luck." << std::endl;

	while (playerWins < numWins && computerWins < numWins) {

		std::cout << std::endl;

		Move playerMove = getChoice();
		Move computerMove = Move(rand() % 3);

		std::cout << name << " picks " << moveToString(playerMove) << " and computer picks " << moveToString(computerMove) << std::endl;

		Result winner = calculateWinner(playerMove, computerMove);

		games++;

		switch (winner) {
			case Result::PLAYER1:
				std::cout << "... " << name << " wins!" << std::endl;
				playerWins++;
				break;
			case Result::PLAYER2:
				std::cout << "... Computer wins!" << std::endl;
				computerWins++;
				break;
			case Result::TIE:
				std::cout << "... A tie." << std::endl;
				break;
		}

		printScores(name, playerWins, computerWins);

		games++;
	}

	if (playerWins > computerWins) {
		std::cout << "\n" << name << " beat the computer:\n... won " << playerWins << " games in " << games << " rounds of rock-paper-scissors." << std::endl;
	} else {
		std::cout << "\nThe computer beat " << name << ":\n... won " << computerWins << " games in " << games << " rounds of rock-paper-scissors." << std::endl;
	}



	return 0;
}