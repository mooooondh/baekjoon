#include <iostream>
using namespace std;

int main() {
	int InputNum = 0;
	int MaxNum = 0;
	int Count = 0;

	for (int i = 0; i < 9; i++) {
		cin >> InputNum;
		if (InputNum > MaxNum) {
			MaxNum = InputNum;
			Count = i;
		}
	}

	cout << MaxNum << endl;
	cout << Count + 1 << endl;

	return 0;
}