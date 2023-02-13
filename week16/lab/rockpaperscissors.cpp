/*
	Description: Play rock, paper, scissors against the computer.
    Author: Millan Kumar
    Date: Febuary 17, 2023
*/

#include <iostream>
#include <ctime>		// time
#include <string>

using namespace std;


 // explicit values for easy conversion from int to Move
enum Move : int { ROCK = 0, PAPER = 1, SCISSORS = 2 };
enum Result { PLAYER1, PLAYER2, TIE };

string moveToString(Move move) {
	// convert Move enum to string

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
	// gets valid user input

	cout << "Enter your move (rock, paper, or scissors): ";

	string choice;
	getline(cin, choice);

	// string[string.length()] = '\0' (will go to default case)
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
			cout << "Invalid choice." << endl;
			return getChoice();
	}
}


Result calculateWinner(Move p1, Move p2) {
	// returns the winner of the round

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
	// prints the current scores

	cout << "---------------------------------" << endl;
	cout << name << ": " << playerWins << "\tComputer: " <<  computerWins << endl;
	cout << "---------------------------------" << endl;
}

void round(int& playerWins, int& computerWins, string name) {
	/*
		plays a round of rock-paper-scissors (gets user input, generates computer move, calculates winner)
		Note: updates playerWins and computerWins
	*/


	Move playerMove = getChoice();
	Move computerMove = Move(rand() % 3);

	cout << name << " picks " << moveToString(playerMove) << " and computer picks " << moveToString(computerMove) << endl;

	Result winner = calculateWinner(playerMove, computerMove);

	switch (winner) {
		case Result::PLAYER1:
			cout << "... " << name << " wins!" << endl;
			playerWins++;
			break;
		case Result::PLAYER2:
			cout << "... Computer wins!" << endl;
			computerWins++;
			break;
		case Result::TIE:
			cout << "... A tie." << endl;
			break;
	}
}

void printWinner(string winner, string loser, int wins, int games) {
	// prints the winner of the game
	cout << endl << winner << " beat " << loser << ":\n... won " << wins << " games in " << games << " rounds of rock-paper-scissors." << endl;
}


int main() {

	srand(time(NULL));

	int playerWins = 0;
	int computerWins = 0;

	int games = 0;

	cout << "What is your name? ";
	string name;
	getline(cin, name);

	cout << "How many wins should we play until? ";
	int numWins;
	cin >> numWins;

	// FLUSH CIN BUFFER???
	string _;
	getline(cin, _);

	cout << "Let’s see who can win " << numWins << " games first! Good luck." << endl;

	while (playerWins < numWins && computerWins < numWins) {

		cout << endl;

		round(playerWins, computerWins, name);
		printScores(name, playerWins, computerWins);

		games++;
	}

	if (playerWins > computerWins) {
		printWinner(name, "the computer", playerWins, games);
	} else {
		printWinner("the computer", name, computerWins, games);
	}



	return 0;
}