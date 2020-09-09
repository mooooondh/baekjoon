#include <stdio.h>
#include <stdlib.h>

int main() {
	int size = 0;
	int min = 0;
	int max = 0;

	scanf("%d", &size);

	int* GetNum = malloc((sizeof(int)) * size);

	for (int i = 0; i < size; i++) {
		scanf("%d", &GetNum[i]);
	}

	min = GetNum[0];
	max = GetNum[0];
	for (int i = 0; i < size; i++) {
		if (min > GetNum[i]) {
			min = GetNum[i];
		}

		else if (max < GetNum[i]) {
			max = GetNum[i];
		}
	}

	printf("%d %d", min, max);

	return 0;
}