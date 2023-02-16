#include <iostream>
#include <cmath>

using namespace std;

int main() {

	cout << "denominator ratio (k): ";
	double k;
	cin >> k;

	cout << "number of terms (n): ";
	int n;
	cin >> n;

	double sum = 0;
	for (int i = 0; i < n; i++) {
		sum += 1 / pow(k, i);
	}

	cout << "sum: " << sum << endl;


	return 0;
}