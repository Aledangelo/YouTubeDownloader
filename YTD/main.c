#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main() {
	printf("*** YOUTUBE DOWNLOADER ***");
	printf("\n\n");

	system("python3 YTD/ytd.py");

	return 0;
}
