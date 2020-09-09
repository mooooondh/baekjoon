#include <iostream>
using namespace std;

int main() {
	int num1 = 0;
	int num2 = 0;
	int count = 7;

	cin >> num1;

	for (int i = 0; i < 7; i++) {
		cin >> num2;
		if (++num1 == num2) {
			count++;
		}
		else if ((num1 - 2) == num2) {
			count--;
		}
		num1 = num2;
	}
	if (count == 14) {
		cout << "ascending" << endl;
	}
	else if (count == 0) {
		cout << "descending" << endl;
	}
	else {
		cout << "mixed" << endl;
	}
}