#include <stdio.h>
#include <string.h>


int isin(char *array[5], char val[], int lenArray) {
	if(array[0]) {
		for(int i = 0; i<lenArray; i++) {
			if(strcmp(array[i], val) == 0) {
				return 1;
			}
		}
	}
	return 0;
}

int calculateAnswer() {
	int numLines;
	int retVal;
	
	retVal = scanf("%d", &numLines);

	char *seenWords[numLines];
	char thisWord[5];
	
	for(int line_i=0; line_i<numLines;line_i++) {
		retVal = scanf("%s", thisWord);
		
		if(strcmp(thisWord, "->") == 0) {
			retVal = scanf("%s", thisWord);
		} else {
			while(strcmp(thisWord, "->")) {
				if(isin(seenWords, thisWord, numLines) == 0) {
					return line_i+1;
				}
				retVal = scanf("%s", thisWord);
			}
			retVal = scanf("%s", thisWord);
		}
		seenWords[line_i] = strdup(thisWord);
	}
	return 0;
}

int main(void) {
	int ans = calculateAnswer();
	if(ans == 0) {
		printf("correct");
	} else {
		printf("%d", ans);
	}
	return 0;
}