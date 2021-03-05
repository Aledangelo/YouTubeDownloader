all: main.o
	gcc -o YouTubeDownloader main.o
main.o: YTD/main.c
	gcc -c -o main.o YTD/main.c
clean:
	rm -f *.o
	rm -f YouTubeDownloader
