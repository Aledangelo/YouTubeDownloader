from pytube import YouTube

check = "youtube"
link = input("Enter YouTube link: ")
if check in link:
	print("\nDownloading...")
	video = YouTube(link)
	stream = video.streams.get_highest_resolution()
	stream.download()
else:
	print("\nThis link is not supported")
