/*
	Description: This program will take a year from the user and print out whether
		it is a leap year or not.
    Author: Millan Kumar
    Date: Febuary 17, 2023
*/

#include <iostream>
#include <string>

using namespace std;


int main() {

	cout << "Enter a year: ";

	int year;
	cin >> year;

	// if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
	// 	cout << year << " is a leap year." << endl;
	// } else {
	// 	cout << year << " is not a leap year." << endl;
	// }

	if (year % 400 == 0) {
		cout << year << " is a leap year." << endl;
	} else if (year % 100 == 0) {
		cout << year << " is not a leap year." << endl;
	} else if (year % 4 == 0) {
		cout << year << " is a leap year." << endl;
	} else {
		cout << year << " is not a leap year." << endl;
	}


	return 0;
}