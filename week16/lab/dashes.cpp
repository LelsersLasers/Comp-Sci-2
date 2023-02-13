/*
	Description: This program will take a string from the user and print it out
		with dashes between each character.
    Author: Millan Kumar
    Date: Febuary 17, 2023
*/

#include <iostream>
#include <string>

using namespace std;


int main() {

	cout << "Enter text: ";

	string text;
	getline(std::cin, text);

	for (char& c : text) {
		cout << "-" << c;
	}
	cout << "-" << endl;


	return 0;
}