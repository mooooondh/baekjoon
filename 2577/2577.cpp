#include<iostream>
using namespace std;

int main() {
	int count[10] = { 0 };

	int a = 0;
	int b = 0;
	int c = 0;

	int mul = 0;

	cin >> a;
	cin >> b;
	cin >> c;

	mul = a * b * c;

	while (mul >= 1) {
		switch (mul % 10) {
		case 0:
			count[0] += 1;
			break;
		case 1:
			count[1] += 1;
			break;
		case 2:
			count[2] += 1;
			break;
		case 3:
			count[3] += 1;
			break;
		case 4:
			count[4] += 1;
			break;
		case 5:
			count[5] += 1;
			break;
		case 6:
			count[6] += 1;
			break;
		case 7:
			count[7] += 1;
			break;
		case 8:
			count[8] += 1;
			break;
		case 9:
			count[9] += 1;
			break;
		}
		mul /= 10;
	}

	for (int i = 0; i <= 9; i++) {
		cout << count[i] << endl;
	}

	return 0;
}