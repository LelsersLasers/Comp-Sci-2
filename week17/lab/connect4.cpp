/*
  Description: Play connect 4! Now with AI!
  Author: Millan & Jerry
  Date: March 9, 2023
*/

//----------------------------------------------------------------------------//
#include <iostream> // terminal input/output

#include <climits>  // INT_MIN, INT_MAX for minimax
#include <fstream>  // file reading and writing
#include <tuple>    // return more than 2 things from function
#include <utility>  // pair - return 2 things from function
#include <vector>   // python like lists for minimax

using namespace std;
//----------------------------------------------------------------------------//


//----------------------------------------------------------------------------//
#define MAX(a, b) ((a) > (b) ? (a) : (b))
#define MIN(a, b) ((a) < (b) ? (a) : (b))

const int BOARD_WIDTH = 7;
const int BOARD_HEIGHT = 6;

const int MAX_DEPTH = 8;

// Use these numbers to score an unfinished board (used in minimax)
const int COL_SCORES[7] = {1, 2, 3, 4, 3, 2, 1};
//----------------------------------------------------------------------------//


//----------------------------------------------------------------------------//
// Empty first so it is the default
enum Spot { Empty, X, O };

// explicit int values used when reading/writing to file
enum ControlOptions : int { Person = 0, Easy = 1, Hard = 2 };

// Game info
struct Board {
  Spot grid[BOARD_WIDTH][BOARD_HEIGHT];
  bool notFilledColumn[BOARD_WIDTH];
  Spot turn;
};
//----------------------------------------------------------------------------//


//----------------------------------------------------------------------------//
void clearScreen();

char spotToChar(Spot spot, bool writingToFile = false);
Spot charToSpot(char c);
Spot nextTurn(Spot spot);

int bestMove(Board *board);
int minimax(Board *board, int depth, int a, int b, bool isMaximizing);

void dropSpot(Board *board, int col);
void undoMove(Board *board, int col);
void updateFilledColumns(Board *board); 
int getMove(Board *board, ControlOptions player);
void move(Board *board, ControlOptions player);
bool boardFilled(Board *board);
bool checkWin(Board *board);
void printGame(Board *board);

ControlOptions setUpPlayer(int playerNum);
pair<ControlOptions, ControlOptions> setUpPlayers();

void saveGameData(Board *board, ControlOptions player1, ControlOptions player2);
tuple<Board, ControlOptions, ControlOptions> readSaveGameData();

vector<int> openMoves(Board *board);
int simpleScoreBoard(Board *board);
int bestMove(Board *board);
int minimax(Board *board, int depth, int a, int b, bool isMaximizing);
//----------------------------------------------------------------------------//

void clearScreen() {
  // "clear" is specific to linux/mac
  system("clear");
}

char spotToChar(Spot spot, bool writingToFile) {
  switch (spot) {
  case Spot::X:
    return 'X';
  case Spot::O:
    return 'O';
  default:
    if (writingToFile) {
      // spaces in file (at the end of lines) get trimmed
      return '+';
    } else {
      return ' ';
    }
  }
}

Spot charToSpot(char c) {
  // for reading from file
  switch (c) {
  case 'X':
    return Spot::X;
  case 'O':
    return Spot::O;
  default:
    return Spot::Empty;
  }
}

Spot nextTurn(Spot spot) {
  // toggles between X and 0
  switch (spot) {
  case Spot::X:
    return Spot::O;
  case Spot::O:
    return Spot::X;
  default:
    return spot;
  }
}

void dropSpot(Board *board, int col) {
  // assumes row is not full
  for (int y = 0; y < BOARD_HEIGHT; y++) {
    if (board->grid[col][y] == Spot::Empty) {
      board->grid[col][y] = board->turn;
      break;
    }
  }
}

void undoMove(Board *board, int col) {
  // replace top of a column with empty
  for (int y = BOARD_HEIGHT - 1; y >= 0; y--) {
    if (board->grid[col][y] != Spot::Empty) {
      board->grid[col][y] = Spot::Empty;
      break;
    }
  }
}

void updateFilledColumns(Board *board) {
  // if the top of a column is empty, you can place a piece there
  for (int x = 0; x < BOARD_WIDTH; x++) {
    board->notFilledColumn[x] = board->grid[x][BOARD_HEIGHT - 1] == Spot::Empty;
  }
}

int getMove(Board *board, ControlOptions player) {
  // gets a valid open column based on the ControlOption
  // assumes board is not filled

  int col = 0; // default value to avoid warning
  switch (player) {
  case ControlOptions::Person:
    cout << "Choose column to place piece: ";
    cin >> col;
    col--; // index
    break;
  case ControlOptions::Easy:
    col = rand() % BOARD_WIDTH;
    break;
  case ControlOptions::Hard:
    col = bestMove(board);
    break;
  }

  updateFilledColumns(board);
  for (int x = 0; x < BOARD_WIDTH; x++) {
    // pointer arithmetic
    if (x == col && *(board->notFilledColumn + x)) {
      return col;
    }
  }

  cout << "Invalid move!" << endl;
  return getMove(board, player);
}

void move(Board *board, ControlOptions player) {
  // gets and makes a move and updates the boards columns

  int col = getMove(board, player);
  dropSpot(board, col);

  updateFilledColumns(board);
}

bool boardFilled(Board *board) {
  // true if there are no valid moves left
  for (int x = 0; x < BOARD_WIDTH; x++) {
    // pointer arithmetic
    if (*(board->notFilledColumn + x)) {
      return false;
    }
  }
  return true;
}

bool checkWin(Board *board) {
  // true if someone has won

  // check vertical win
  for (int x = 0; x < BOARD_WIDTH; x++) {
    for (int y = 0; y <= BOARD_HEIGHT - 4; y++) {
      Spot startSpot = board->grid[x][y];
      if (startSpot == Spot::Empty) {
        continue;
      }
      bool allMatching = true;
      for (int i = 1; i < 4; i++) {
        if (board->grid[x][y + i] != startSpot) {
          allMatching = false;
        }
      }
      if (allMatching) {
        return true;
      }
    }
  }

  // check horizontal win
  for (int y = 0; y < BOARD_HEIGHT; y++) {
    for (int x = 0; x <= BOARD_WIDTH - 4; x++) {
      Spot startSpot = board->grid[x][y];
      if (startSpot == Spot::Empty) {
        continue;
      }
      bool allMatching = true;
      for (int i = 1; i < 4; i++) {
        if (board->grid[x + i][y] != startSpot) {
          allMatching = false;
        }
      }
      if (allMatching) {
        return true;
      }
    }
  }

  // check diagonal left
  for (int x = 3; x < BOARD_WIDTH; x++) {
    for (int y = 0; y <= BOARD_HEIGHT - 4; y++) {
      Spot startSpot = board->grid[x][y];
      if (startSpot == Spot::Empty) {
        continue;
      }
      bool allMatching = true;
      for (int i = 1; i < 4; i++) {
        if (board->grid[x - i][y + i] != startSpot) {
          allMatching = false;
        }
      }
      if (allMatching) {
        return true;
      }
    }
  }

  // check diagonal right
  for (int x = 0; x <= BOARD_WIDTH - 4; x++) {
    for (int y = 0; y <= BOARD_HEIGHT - 4; y++) {
      Spot startSpot = board->grid[x][y];
      if (startSpot == Spot::Empty) {
        continue;
      }
      bool allMatching = true;
      for (int i = 1; i < 4; i++) {
        if (board->grid[x + i][y + i] != startSpot) {
          allMatching = false;
        }
      }
      if (allMatching) {
        return true;
      }
    }
  }

  return false;
}

void printGame(Board *board) {
  // show the game

  clearScreen();
  cout << endl;

  for (int y = BOARD_HEIGHT - 1; y >= 0; y--) {
    cout << " | ";
    for (int x = 0; x < BOARD_WIDTH; x++) {
      cout << spotToChar(board->grid[x][y]) << " ";
    }
    cout << "|" << endl;
  }

  cout << " +---------------+" << endl;
  cout << " | 1 2 3 4 5 6 7 |" << endl;
  if (board->turn != Spot::Empty) {
    cout << "Current turn: " << spotToChar(board->turn) << endl;
  } else {
    cout << "Game over!" << endl;
  }
}

ControlOptions setUpPlayer(int playerNum) {
  // get control option for a player

  cout << "Player " << playerNum << ": [P]erson, [E]asy AI, [H]ard AI? ";
  char playerChar;
  cin >> playerChar;

  switch (playerChar) {
  case 'P':
  case 'p':
    return ControlOptions::Person;
  case 'E':
  case 'e':
    return ControlOptions::Easy;
  case 'H':
  case 'h':
    return ControlOptions::Hard;
  }

  cout << "Invalid choice" << endl;
  return setUpPlayer(playerNum);
}

pair<ControlOptions, ControlOptions> setUpPlayers() {
  // get control options for both players

  cout << "Player 1 starts (and is 'X's)" << endl;
  cout << "Player 2 is 'O's\n" << endl;
  ControlOptions player1 = setUpPlayer(1);
  ControlOptions player2 = setUpPlayer(2);
  return make_pair(player1, player2);
}

void saveGameData(Board *board, ControlOptions player1, ControlOptions player2) {
  // write game to a file
  // always uses the same file

  ofstream fout("gameSaves.txt", ios::trunc);

  for (int x = 0; x < BOARD_WIDTH; x++) {
    for (int y = 0; y < BOARD_HEIGHT; y++) {
      fout << spotToChar(board->grid[x][y], true);
    }
    fout << endl;
  }
  fout << player1 << endl;
  fout << player2 << endl;
  fout.close();
}

tuple<Board, ControlOptions, ControlOptions> readSaveGameData() {
  // if there is a save file with an unfinished game, load it
  // else, create a new game

  ifstream saveReader("gameSaves.txt");
  Board board = {{}, {}, Spot::X};
  string line;

  int x = 0;
  while (saveReader.good() && x < BOARD_WIDTH) {
    getline(saveReader, line);
    for (int y = 0; y < BOARD_HEIGHT; y++) {
      board.grid[x][y] = charToSpot(line[y]);
    }
    x++;
  }

  updateFilledColumns(&board);

  bool gameOver = checkWin(&board) || boardFilled(&board);

  ControlOptions player1, player2;
  if (saveReader.good() && x == BOARD_WIDTH && !gameOver) {
    getline(saveReader, line);
    player1 = ControlOptions(stoi(line));

    getline(saveReader, line);
    player2 = ControlOptions(stoi(line));

    Spot currentTurn = Spot::X;
    for (int x = 0; x < BOARD_WIDTH; x++) {
      for (int y = 0; y < BOARD_HEIGHT; y++) {
        Spot boardSpot = board.grid[x][y];
        if (boardSpot != Spot::Empty) {
          currentTurn = nextTurn(currentTurn);
        }
      }
    }
    board.turn = currentTurn;
  } else {
    pair<ControlOptions, ControlOptions> players = setUpPlayers();
    player1 = players.first;
    player2 = players.second;

    // default blank board
    // Spot::Empty is first and is used as the default value for Board.grid
    board = {{}, {true, true, true, true, true, true, true}, Spot::X};
  }

  saveReader.close();

  return make_tuple(board, player1, player2);
}

vector<int> openMoves(Board *board) {
  // list of open columns

  vector<int> validMoves = vector<int>();
  for (int i = 0; i < BOARD_WIDTH; i++) {
    if (board->notFilledColumn[i]) {
      validMoves.push_back(i);
    }
  }
  return validMoves;
}

int simpleScoreBoard(Board *board) {
  int score = 0;


    
  for (int x = 0; x < BOARD_WIDTH; x++) {
    for (int y = 0; y < BOARD_HEIGHT; y++) {
      if (board->grid[x][y] == Spot::X) {
        score += COL_SCORES[x];
      } else if (board->grid[x][y] == Spot::O) {
        score -= COL_SCORES[x];
      }
    }
  }

  return score;
}

int bestMove(Board *board) {
  // to calculate the best move

  vector<int> validMoves = openMoves(board);
  Spot turn = board->turn;
  bool isMaximizing = turn == Spot::X;
  
  vector<int> bestMoves = vector<int>();
  int bestScore = isMaximizing ? INT_MIN : INT_MAX;

  for (int col : validMoves) {
    board->turn = turn;
    dropSpot(board, col);

    int score = minimax(board, 0, INT_MIN, INT_MAX, !isMaximizing);
    // cout << "Score[" << col << "]: " << score << endl;

    undoMove(board, col);

    if (score == bestScore) {
      bestMoves.push_back(col);
    }
    if (isMaximizing) {
      if (score > bestScore) {
        bestMoves.clear();
        bestMoves.push_back(col);
        bestScore = score;
      }
    } else {
      if (score < bestScore) {
        bestMoves.clear();
        bestMoves.push_back(col);
        bestScore = score;
      }
    }
    
  }

  board->turn = turn;

  int bestCol = bestMoves[rand() % bestMoves.size()];
  return bestCol;

  // return bestMoves[0];
}

int minimax(Board *board, int depth, int a, int b, bool isMaximizing) {
  // magic?

  updateFilledColumns(board);

  bool gameWon = checkWin(board);
  // game won on previous turn
  if (gameWon && board->turn == Spot::X) { // X win
    return 1000;
  } else if (gameWon && board->turn == Spot::O) { // O win
    return -1000;
  }

  bool tied = boardFilled(board);
  if (tied) {
    return 0;
  }

  if (depth >= MAX_DEPTH) {
    return simpleScoreBoard(board);
    // return 0;
  }


  if (isMaximizing) {
    int bestScore = INT_MIN;
    vector<int> validMoves = openMoves(board);

    for (int col : validMoves) {

      board->turn = Spot::X;
      dropSpot(board, col);

      int score = minimax(board, depth + 1, a, b, false);

      undoMove(board, col);

      bestScore = MAX(score, bestScore);
      if (bestScore > b) {
        break;
      }
      a = MAX(a, bestScore);
    }
    return bestScore;
  } else { // minimizing
    int bestScore = INT_MAX;
    vector<int> validMoves = openMoves(board);

    for (int col : validMoves) {

      board->turn = Spot::O;
      dropSpot(board, col);

      int score = minimax(board, depth + 1, a, b, true);

      undoMove(board, col);

      bestScore = MIN(score, bestScore);
      if (bestScore < a) {
        break;
      }
      b = MIN(b, bestScore);
    }
    return bestScore;
  }
}

int main() {
  srand(time(NULL));

  tuple<Board, ControlOptions, ControlOptions> saveData = readSaveGameData();
  Board board = get<0>(saveData);
  ControlOptions player1 = get<1>(saveData);
  ControlOptions player2 = get<2>(saveData);

  while (true) { // break when game is over or board is filled
    printGame(&board);

    bool won = checkWin(&board);
    bool isBoardFilled = boardFilled(&board);

    saveGameData(&board, player1, player2);

    if (won || isBoardFilled) {
      if (won) {
        char winner = spotToChar(nextTurn(board.turn));
        cout << "The winner is: " << winner << endl;
      } else {
        cout << "Tie" << endl;
      }
      break; // skip running move()
    }

    ControlOptions player;
    switch (board.turn) {
    case Spot::X:
      player = player1;
      break;
    case Spot::O:
      player = player2;
      break;
    default:
      continue;
    }

    move(&board, player);
    board.turn = nextTurn(board.turn);
  }

  return 0;
}