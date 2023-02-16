/*
	Description: This program will take a string from the user and print it out
		with the characters 'e', 'l', and 's' replaced with 3, 1, and 5 respectively.
    Author: Millan Kumar
    Date: Febuary 17, 2023
*/

#include <iostream>
#include <string>

using namespace std;


int main() {

	cout << "Enter string: ";

	string text;
	getline(cin, text);

	cout << "Leet version: ";

	for (char& c : text) {
		switch (c) {
			case 'e':
			case 'E':
				cout << '3';
				break;
			case 'l':
			case 'L':
				cout << '1';
				break;
			case 's':
			case 'S':
				cout << '5';
				break;
			default:
				cout << c;
		}
	}
	cout << endl;


	return 0;
}