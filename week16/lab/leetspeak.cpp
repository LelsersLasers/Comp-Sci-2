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

	string leetedString = "";

	for (char& c : text) {
		switch (c) {
			case 'e':
			case 'E':
				leetedString += "3";
				break;
			case 'l':
			case 'L':
				leetedString += "1";
				break;
			case 's':
			case 'S':
				leetedString += "5";
				break;
			default:
				leetedString += c;
		}
	}
	cout << "Leet version: " << leetedString << endl;


	return 0;
}